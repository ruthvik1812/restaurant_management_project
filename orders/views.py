from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from .serializers import UserProfileSerializer
from django.http import JsonResponse
from .utils import send_email
from rest_framework.response import Response

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
# ---------- Order Detail API ----- #
class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
    
    def order_confirmation(request):
        user_email = "customer@example.com"
        subject = "Order Confirmation"
        message = "Thank you for the your order! "
        
        if send_email(user_email, subject, message):
            return JsonResponse({"status": "success", "message": "Email sent successfully"})
        else:
            return JsonResponse({"status": "error", "message": "Failed to send email"})
# -------------- Order view -------------- #
class OrderViewSet(viewsets.viewSet):
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk=None):
        """
        Cancel an order by updating its status to 'Cancelled'.
        only the user who placed the order can cancel it.
        """
        order = get_object_or_404(Order, pk=pk)

        if order.user != request.user:
            return Response(
                {"error":"You are not authorized to cancel this order."},
                status=status.HTTP_403_FORBIDDEN
            )
        if order.status in ['Completed', 'Cancelled']:
            return Response(
                {"error":f"Order cannot be cancelled as it is already {order.status.lower()."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = 'Cancelled'
        order.save()

        serializer = OrderSerializer(order)
        return Response(
            {"message":"Order cancelled successfully.", "order": serializer.data},
            status=status.HTTP_200_OK
        )
# -----------UserProfileUpdateView ----- #

class UserProfileUpdateView(APIView):
    
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request, partial=True)
        if serializer.is_Valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'errors': serializer.errors}, status=status_400_BAD_REQUEST)
