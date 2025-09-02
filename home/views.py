from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Feedback, Staff, MenuItem, RestaurantLocation
from .forms import ContactForm, FeedbackForm


# ====== Home Page View ====== #
def home(request):
    restaurant = RestaurantLocation.objects.first()
    query = request.GET.get("q", "")
    menu_items = MenuItem.objects.filter(name__icontains=query) if query else MenuItem.objects.all()

    cart_count = request.session.get("cart_count", 0)

    faqs = [
        {"question": "What are your opening hours?", "answer": "We are open daily from 10:00 AM to 11:00 PM."},
        {"question": "Do you offer home delivery?", "answer": "Yes, we provide free home delivery within 5 km."},
        {"question": "Can I book a table online?", "answer": "Absolutely! Use our 'Book a Table' feature on the homepage."},
    ]

    return render(request, "home.html", {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
        "cart_count": cart_count,
        "faqs": faqs,
        "current_datetime": timezone.now(),
    })


# ====== Contact Page View ====== #
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect("contact")
    return render(request, "home.html", {"form": form})


# ====== Menu Page ====== #
def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, "home.html", {"menu_items": menu_items})


# ====== Add to Cart ====== #
def add_to_cart(request, item_id):
    menu_item = MenuItem.objects.get(id=item_id)
    cart = request.session.get("cart", {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session["cart"] = cart
    request.session.modified = True
    return redirect("home")


# ====== Reservation Page ====== #
def reservations(request):
    return render(request, "reservation.html")


# ====== Feedback Submission ====== #
def submit_feedback(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        if comment.strip():
            Feedback.objects.create(comment=comment)
            return render(request, "feedback_home.html", {"success": "Thank you for your feedback!"})
        return render(request, "feedback_home.html", {"error": "Feedback cannot be empty!"})
    return render(request, "feedback_home.html")


# ====== Staff Login API ====== #
@api_view(['POST'])
def staff_login(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        staff = Staff.objects.filter(email=email).first()
        if staff and check_password(password, staff.password):
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ====== Order Page ====== #
def order_page(request):
    return render(request, "order.html")
