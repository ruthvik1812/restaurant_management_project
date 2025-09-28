import secrets
import string
import logging
import django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from orders.models import Coupon, Order   # make sure you have a Coupon model defined

logger = logging.getLogger(__name__)


def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    :param length: Length of the coupon code (default 10)
    :return: Unique coupon code (string)
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        # Generate a random alphanumeric string
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Ensure uniqueness by checking existing codes in DB
        if not Coupon.objects.filter(code=code).exists():
            if order:
                Coupon.objects.create(
                    code=code,
                    order=order,
                    discount_amount=discount_amount
                )
            return code

def send_order_confirmation_email(order, include_coupon=False, coupon_length=10,discount_amount=10):
    """
    Sends an order confirmation email with optional code.
    :param order: Order instance
    :param include_coupon: If True, generate and include a coupon code
    :param discount_amount: Optional discount value for the coupon
    :return: dict with 'sucess' and 'message'
    """
    subject = f"Order Confirmation - Order #{order.id}"

    item_lines = [
        f"{item.quantity} x {item.priduct.name} - ${item.product.price * item.quantity:.2f}"
        for item in order.items.all()
    ]
    items_text = "\n".join(item_lines)
    message = f"""
    Hello {order.customer.username}, 

    Thank you for your order! Here are your order details:

    Order ID: {order.id}
    Status: {order.status}
    Total Amount: ${order.total_amount:.2f}

    Items:
    {item_text}
    """
    if include_coupon:
        coupon_code = generate_coupon_code(length=coupon_length, order=order, discount_amount)
        message +=f"\nAs a thank you, here is your coupon code for next purchase: {coupon_code} (Discount: ${discount_amount})\n"
        message += "\nWe appreciate your business and hope you enjoy your order!\n\nBest regards,\nYour Company Name"

        recipient_list = [order.customer.email