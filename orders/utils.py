import secrets
import string
from orders.models import Coupon   # make sure you have a Coupon model defined


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
            return code
