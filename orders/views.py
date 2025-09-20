from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

# Create your views here
# ------ Home view ----- #
def home(request):
    menu_items = MenuItem.objects.all()
    
    # Get cart from session

    cart = request.session.get('cart',{})
    cart_items = []
    total = 0
    for item_id, quantity in cart.items():
        item = get_object_or_404(MenuItem, id=item_id)
        cart_items.append({
            'id': item.id,
            'price': item.price,
            'quantity': quantity,
            'total_price': item.price * quantity
        })
        total += item..price * quantity
    
    context = {
        'menu_items': menu_items,
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'home.html', context)

    # Add item to cart
def add_to_cart(request, item_id):
    cart = request.session.get('cart',{})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
return redirect('home')

# Update item quantity in cart
def update_cart(request, item_id):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart',{})
    if quantity > 0:
        cart[str(item_id)] = quantity
    else: 
        cart.pop(str(item_id), None)
    request.session['cart'] = cart
return redirect('home')

class OrderHistoryView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by("-created_at")