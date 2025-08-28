from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ContactForm, FeedbackForm
from .models import Feedback, Staff, MenuItem, RestaurantLocation, Restaurant


#========== Home Page View ==========#
def home(request):
    # Fetch restaurant details
    restaurant = Restaurant.objects.first()

    # Handle search functionality
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

    # Calculate cart count from session
    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())

    # Fetch restaurant location dynamically
    location = RestaurantLocation.objects.first()

    return render(request, "home.html", {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
        "cart_count": cart_count,
        "location": location,
        "opening_hours": restaurant.opening_hours if restaurant else {},
    })


#========== About Page View ==========#
def about(request):
    context = {
        "restaurant_name": "RR Restaurant",
        "history": "Founded in 2010, RR Restaurant has been serving delicious dishes crafted with passion and love. Over the years, we’ve grown from a small family-owned eatery to one of the most loved dining spots in town.",
        "mission": "To bring joy to every customer by serving fresh, high-quality, and tasty food while providing exceptional customer service.",
        "vision": "To be the most trusted and loved restaurant brand, creating unforgettable dining experiences for everyone.",
        "values": ["Fresh Ingredients", "Customer Satisfaction", "Quality Service", "Sustainability"],
    }
    return render(request, "about.html", context)


#========== Add to Cart View ==========#
def add_to_cart(request, item_id):
    menu_item = MenuItem.objects.get(id=item_id)

    # Get cart from session or create a new one
    cart = request.session.get("cart", {})

    # Add or update item quantity
    if str(item_id) in cart:
        cart[str(item_id)] += 1
    else:
        cart[str(item_id)] = 1

    # Save updated cart to session
    request.session["cart"] = cart
    request.session.modified = True

    return redirect("home")


#========== Contact Form View ==========#
def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Email Notification
            subject = f"New Contact Submission from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.RESTAURANT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Thank you! Your message has been sent successfully.")
            except BadHeaderError:
                messages.error(request, "Invalid header found. Email not sent.")

            return redirect("home")

    return render(request, "contact.html", {"form": form})


#========== Reservation Page View ==========#
def reservations(request):
    return render(request, "reservation.html")


#========== Feedback Submission View ==========#
def submit_feedback(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        if comment.strip():
            Feedback.objects.create(comment=comment)
            return render(request, "feedback_home.html", {"success": "Thank you for your feedback!"})
        else:
            return render(request, "feedback_home.html", {"error": "Feedback cannot be empty!"})

    return render(request, "feedback_home.html")


#========== Staff Login API ==========#
@api_view(['POST'])
def staff_login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        staff = Staff.objects.filter(email=email).first()
        if staff and check_password(password, staff.password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#========== Menu API ==========#
@api_view(['GET'])
def get_menu(request):
    menu_items = MenuItem.objects.all()

    menu = []
    for item in menu_items:
        menu.append({
            "name": item.name,
            "description": item.description,
            "price": str(item.price),
            "image": item.image.url if item.image else None,
        })

    return Response({"menu": menu})


#========== Dedicated Menu Page View ==========#
def menu_page(request):
    menu_items = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menu_items": menu_items})

