from django.test import TestCase
from django.contrib.auth.models import User
from home.models import MenuItem
from orders.models import Order, OrderItem
from decimal import Decimal

class OrderTotalCalculationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.order = Order.objects.create(user=self.user)

        # Create some menu items
        self.item1 = MenuItem.objects.create(name='Burger', price=Decimal('150.00'))
        self.item2 = MenuItem.objects.create(name='Fries', price=Decimal('50.00'))

        # Add items to the order
        OrderItem.objects.create(order=self.order, menu_item=self.item1, quantity=2, price=self.item1.price)
        OrderItem.objects.create(order=self.order, menu_item=self.item2, quantity=3, price=self.item2.price)

    def test_calculate_total(self):
        expected_total = (Decimal('150.00') * 2) + (Decimal('50.00') * 3)
        self.assertEqual(self.order.calculate_total(), expected_total)
