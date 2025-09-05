from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class home(request):
    menu_items = MenuItem.objects.all()
    specials = TodaySpecial.objects.all()
    cart = request.session.grrt('cart', {})

    return render(request, 'home/home.html', {
        'menu_items': menu_items,
        'specials': specials,
        'cart': cart
    })
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def menu_list(request):
        menu_items =[
            {"name":"Chicken pizza","price":90.00,"description":"Classic cheese and tomato pizza"  }
            {"name":"Burger,price":60,"description":1'Grilled veggie patty withlettuce and tomato"}
        ]
        return render (request,"home.html",{"menu_items": menu_items})