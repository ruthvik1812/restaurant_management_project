from django.shortcuts import render
from django.conf import settings
from .forms import FeedbackForm
# Create your views here.

#home page
def home(request):
    return render(request,'home.html',{
    'restaurant_name':settings.RESTAURANT_NAME,
    'phone_number':settings.ReSTAURANT_PHONE
    })
# reservation page
def reservarions(request):
    return render(request,"reservation.html")
def submit_feedback(request):
    if request.method =="POST":
        comment = request.POST.grt("comment")
        Feedback.objects.create(comment=comment)
        return render(request, "feedback_home.html",{"success":"Thank you for your feedback!"})


#staff login ApI
@api_view(['post'])
def staff_login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')


        if not email or not password:
            return Response(
                {'error':'Email and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
            staff = Staff.objects.filter(email=email).first()
            if staff and check_password(password,staff.password):
                return Response({'message':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Responce({'error':'Invalid credintials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exeception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)