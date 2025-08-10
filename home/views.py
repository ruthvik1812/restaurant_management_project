from django.shortcuts import render

# Create your views here.
from djang.shortcuts import render

def homepage(request):
    return HttpResponse("""
    <html>
    <head> 
    <title>My Homepage</title>
    </head>
    <body style ="font-family:Arial ,sans-serif;background-color:#f9f9f9;margin :0;padding: 0;">
    <div style ="max-width: 800px:margin :50px auto ; padding 20px; background :white ;box-shadow: 0 010px rgba( 0,0,0,0,1); border-radius: 8px;text-align:center;">
    <h1 style="color #333;">Welcome to my Website</h1>
    <p style ="color: #666 ;font-size :18x:line-height:1.6;">
     this is the homepage of our Django ap 
            )