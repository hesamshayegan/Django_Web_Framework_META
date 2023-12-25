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

def home(request):
    path = request.path
    address = request.META['REMOTE_ADDR']
    scheme = request.scheme
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg =   f""" <br>
        <br> Path {path}
        <br> Adress {address}
        <br> Scheme {scheme}
        <br> User Agent {user_agent}
        <br> Path Info {path_info}
        <br> Response Headers {response.headers}

        """
    return HttpResponse(msg, content_type = 'text/html', charset='utf-8')

def menuitems(request, dish):
    items = {
        'Pasta': 'Pasta is an italian dish',
        'Falafel': 'Flafel is a Lebonese dish'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)