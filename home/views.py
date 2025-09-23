from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.core.paginator import paginator
import random
from .models import Feedback, Staff, MenuItem,TodaySpecial, RestaurantLocation
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ContactForm, FeedbackForm
from .models import RestaurantInfo
from .models import chef
from .models import NewsletterForms
from .models import NewsletterSubscriber
from .rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics , permissions, viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.

#==========Home page View==========#
def home(request):
    restaurant = Restaurant.objects.first()
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    paginator = paginator(menu_list, 6)
    page_number = request.GET.get("page")
    menu_items = paginator.get_page(page_number)
    
    # Get cart items from session
    specials = TodaySpecial.objects.all()
    cart = request.session.get("cart", {})
    total_items = sum(cart.values())

    # Handle login form submission
    if request.method == "POST" and "login" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenicate(request, username=username, password=password)
    if user:
        login(request, user)
        messages.success(request, "Login successful!")
        return redirect("home")
    else:
        messages.error(request, "Invalid username or password.")

    # Fetch restaurant details
    restaurant = RestaurantLocation.objects.first()
    # Handle search functionality
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    
    cart_count = request.session.get("cart_count", 0)
    
    current_date = timezone.now()

    faqs=[
        {"question":"What are your opening hours?","answer":"We are opening daily from 10:00Am to 11:00pm."},
        {"question":"Do you offer home delivery?","answer":"Yes, we provide free home delivery within 5 km."},
        {"question":"Can I table online?","answer":"Ansolutely! Use our 'Book a Table' feature on the homepage."},
    ]
    
    # Check for order confirmation
    order_number = None
    if request.GET.get("confirmed") == "true":
        order_number = random.randint(1000, 9999)
   opening_hours = {
    "Monday":"10:00 AM - 10:00 PM",
    "Tuesday": "10:00 AM - 10:00 PM",
    "Wednesday": "10:00 AM - 10:00 PM",
    "Thursday": "10:00 AM - 10:00PM",
    "FRIDAY" : "09:00 AM - 10:00 PM",
    "Saturday": "09:00 AM - 10:00 PM",
    "Sunday": "9:00 AM - 11:00PM",
   } 
   # Newsletter Form
   if request.method =="POST" and "newsletter" in request.POST:
    form = NeewsletterForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "home.html",{
        "form" :NewsletterForm(),
        "success": "You have subscribed successfully!",
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
        "specials" = specials,
        "cart_count": cart_count,
        "faqs": faqs,
        "current_datetime": current_datetime,
        "order_number": order_number,
        "opening_hours": opening_hours,
    })
    else:
        form = NewsletterForm()
    return render(reequest, "home.html", 
    {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
        "specials": specials,
        "cart_count": cart_count,
        "faqs": faqs,
        "current_datetime": timezone.now(),
        "order_number": order_number,
        "opening_hours": opening_hours,
        "form": form,
    })
# ========== API ViewSet for Menu Items ====== #
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]
    
# ====== Order Page (Redirects to Home with confirmation)===== #
def order_page(request):
    return redirect("/?confirmed=true")
    
# ====== About Page View ============#
def about(request):
    restaurant  = RestaurantInfo.objects.first()
    return render(request, "about.html",{"restaurant": restaurant})

    }
    #========== Add to Cart View ============#

    def add_to_cart(request, item_id):
        item = get_objects_or_404(MenuItem, id=item_id)
        cart = request.session.get("cart", {})

        # If item already exists, increase quantity
        if str(item_id) in cart:
            cart[str(item_id)] +=1
        else:
            cart[str(item_id)] = 1
        # Save updated cart to session
        request.session["cart"] = cart
        request.session.modified = True
        return redirect("home")
    # --------------- REMOVE FROM CART ------------ #
    def remove_from_cart(request, item_id):
        cart = request.session.get("cart",{})

        if str(item_id) in cart:
            del cart[str(item_id)]
        request.session["cart"] = cart
    return redirect("home")

    # ------------ UPDATE CART (QUANTITY) -------------- #
    def update_cart(request, item_id):
        cart = request.session.get("cart",{})
        new_quantity = int(request.POST.get("quantity", 1))
        
        if str(item_id) in cart:
            if new_quantity > 0:
                cart[str(item_id)] = new_quantity
            else:
                del cart[str(item_id)]
            request.session["cart"] = cart
            return redirect("home")
    #===== Contact Form ==========#
    def contact(requst):
        form = ContactForm()
        if request.method == "POST":
           form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        # Email Notification
        subject = f"New Contact Submission from {contact.name}"
        message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\{contact.message}"
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.RESTAURANT_EMAIL],
                fail_silently=False
            )
            messages.success(request, "Thank you! Your message has been sent successfully.")
        except BadHeaderError:
            messages.error(request, "Invalid header found. Email not sent.")

            return redirect("Contact")
            # Redirect to Thank you page
            return redirect("thank_you")
        else:
            form = ContactForm()
        return render(request, "contact.html", {"form": form})
   
    # fetch restaurant Location dynamically
    location = RestaurantLocation.objects.first()
    

    return render(request,'home.html', {
    "restaurant_name": settings.RESTAURANT_NAME,
    "phone_number": settings.RESTAURANT_PHONE,
    "menu_items": menu_items,
    "form": form,
    "location": location,
    "specials": specials,
    "opening_hours":restaurant.opening_hours if restaurant else {},
    "query": query,
    "cart": cart
    })

#=== reservation page ====#
def reservations(request):
    return render(request,"reservation.html")


def submit_feedback(request):
    if request.method =="POST":
        comment = request.POST.get("comment")
        Feedback.objects.create(comment=comment)
        return render(request, "feedback_home.html",{"success":"Thank you for your feedback!"})

    return render(request, "feedback_home.html")


# =========Staff login ApI================== #
@api_view(['POST'])
def staff_login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')


        if not email or not password:
            return Response(
                {'error':'Email and password are required'},
                status=status.HTTP_400_BAD_REQUEST,
            )
            staff = Staff.objects.filter(email=email).first()
            if staff and check_password(password,staff.password):
                return Response({'message':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Respone({'error':'Invalid credintials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ===== FEEDBACK SUBMISSION ======#
def submit_feedback(request):
    if request.method =="POST":
        comment = request.POST.get("comment")
        if comment.strip():
            Feedback.objects.create(comment=coment)
            return render(request, "feedback_home.html", {"success: Thank you for your Feedback!"})
        else:
            return render(request, "feedback_home.html",{"error feedback caanot be empty!"})
    return render(request, "feedback_home.html")

# =============== MENU API ==============#
@api_view(['GET'])
def get_menu(request):
    menu_items = MenuItem.objects.all()

    menu = []
    for item in menu_items:
        menu.append({
            "name": item.name,
            "description": item.description,
            "price": str(item.price),
            "image":item.image.url if item.image else None
        })
    return Response({"menu": menu})
def menu_items_by_category(request):
    category_name = request.GET.get("category")
    if category_name:
        items = MenuItem.objects.filter(category__category_name__iexact=category_name)
    else:
        items = MenuItem..objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data, status=status..HTTP_200_OK)
# =========== Menu Search API =============
class MenuItemSearchView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q","")
        if query:
            return MenuItem.objects.filter(name__icontains=query)
        return MenuItem.objects.all()

 # =============== Dedicated Menu Page View ===========

 def menu_page(request):
    menu_items = MenuItem.objects.all()
    
    return render(request, "menu_list.html", {"menu_items": menu_items})
 # ===== Order Page ====== #
 def order_page(request):
    return render(request, "home.html")
# ======= ABOUT CHEF ========= #
def chef(request):
    chefs = chef.objects.all()
    return render(request, 'chef.html',{'chefs': chefs})
