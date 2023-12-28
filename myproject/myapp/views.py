from django.shortcuts import render
from django.http import HttpResponse 
from myapp.forms import LogForm, BookingForm



# Create your views here.
def drinks(request, drink_name):
    drinks = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = drinks[drink_name]

    return HttpResponse(f"<h2> {drink_name} </h2> " + choice_of_drink )

def home(request):
    return HttpResponse('Welcome to Little Lemon!')

def about(request):
    return HttpResponse('About')

def menu(request):
    return HttpResponse('Menu')

def book(request):
    return HttpResponse('Make a booking')

def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()        
    context = {"form": form}
    return render(request, "home.html", context)


def booking_form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)