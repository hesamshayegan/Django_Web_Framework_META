from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def my_error_handler(request): 
    # ... 
    if (2 == 2) == True: 
        return HttpResponseNotFound('<h1>Testing Error Handler</h1>') 
    else: 
        return HttpResponse('<h1>Page was found</h1>') 