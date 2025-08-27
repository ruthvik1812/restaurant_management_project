from django.shortcuts import render
from django.conf import settings
from .models import Feedback, Staff
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ContactForm, FeedbackForm
from .models import Feedback, Staff, MenuItem, RestaurantLocation
# Create your views here.

#==========Home page View==========#
def home(request):
    # Fetch restaurant details
    restaurant = Restaurant.objects.first()
    # Handle search functionality
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
    else:
        menu_items = MenuItem.objects.all()
   
    # Contact form Logic
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
                settingss.DEFAULT_FROM_EMAIL,
                [settings.RESTAURANT_EMAIL],
                fail_silently=False
            )
            messages.sucess(request, "Thank you! Your message has been sent successfully.")
        except BadHeaderError:
            messages.error(request, "Invalid header found. Email not sent.")

            return redirect('home')
   
    # fetch restaurant Location dynamically
    location = RestaurantLocation.objects.first()
    

    return render(request,'home.html', {
    "restaurant_name": settings.RESTAURANT_NAME,
    "phone_number": settings.RESTAURANT_PHONE,
    "menu_items": menu_items,
    "form": form,
    "location": location,
    "opening_hours":restaurant.opening_hours if restaurant else {},
    "query": query,
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
 # Dedicated Menu Page View

 def menu_page(request):
    menu_items = MenuItem.objects.all()
    
    return render(request, "menu_list.html", {"menu_items": menu_items})