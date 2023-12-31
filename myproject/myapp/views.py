from django.shortcuts import render
from django.http import HttpResponse 
from myapp.forms import LogForm, BookingForm
from django.shortcuts import render 
from .models import Menu


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

def index(request):
    context = {"name": 'alex'}
    return render(request, 'hello.html', context)


def menuitem(request):
    newmenu = {'mains': [
        {'name': 'falafel', 'price': '12'},
        {'name': 'shawarma', 'price': '20'},
        {'name': 'gyro', 'price': '30'},
        {'name': 'humus', 'price': '5'},
    ]}
    return render(request, 'menuitem.html', newmenu)


def menu(request):
    menuitems = Menu.objects.all()
    items_dict = {'menu': menuitems}

    return render(request, 'menu.html', items_dict)