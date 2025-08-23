from django.shortcuts import render
from django.conf import settings
from .forms import FeedbackForm
from .models import Feedback, Staff
from django.contrib.auth.hashers import check_password


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ContactForm
# Create your views here.

#Home page
def home(request):
    api_url ="http://127.0.0.1:8000/api/menu"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        menu_data = response.json()
        menu_items = menu_data.get("menu",[])
    except Exeception:
        menu_items = []
    
    # Contact form Logic
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    # fetch restaurant Location dynamically
    location = RestaurantLocation.objects.first()
    

    return render(request,'home.html', {
    "restaurant_name": settings.RESTAURANT_NAME,
    "phone_number": settings.RESTAURANT_PHONE,
    "menu_items": menu_items,
    "forms": form,
    "location": location,
    })

# reservation page
def reservarions(request):
    return render(request,"reservation.html")


def submit_feedback(request):
    if request.method =="POST":
        comment = request.POST.grt("comment")
        Feedback.objects.create(comment=comment)
        return render(request, "feedback_home.html",{"success":"Thank you for your feedback!"})

    return render(request, "feedback_home.html")


#  Staff login ApI
@api_view(['post'])
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
                return Responce({'error':'Invalid credintials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exeception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_menu(request):
    menu = [
        {
            "name":"panner Butter Masala",
            "description":"Rich, creamy, and flavouaful panner curry.",
            "price":250
        },
        {
            "name":"choclalate Lava Cake",
            "description": "Soft  chocolate cake with gooey molten center.",
            "price":150
        },
        {
            "name":"chicken Biryani",
            "description":"Spicy, aromatic, and perfectly cooked rice with chicken."
            "price":300
        },
    ](
    return Responce({"menu": menu})
 # Dedicated Menu Page View

 def menu_page(request):
     """
     Fetches menu items from the API and renders them on the menu page.
     
     """
     api_url = "https://127.0.0.1:8000/api/menu"
     try:
        response = requests.get(api_url)
        response.raise_for_status()
        menu_data = response.json()
        menu_items = menu_data.get("menu",[])
    except Execption:
        menu_items = []
    return render(request, "menu_list.html", {"menu_items": menu_items})