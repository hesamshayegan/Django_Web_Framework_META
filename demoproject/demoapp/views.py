from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

def say_hello(request):
    return HttpResponse('Hello World')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)