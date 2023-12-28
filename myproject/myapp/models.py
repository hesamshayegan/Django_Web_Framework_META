from django.db import models
from django import forms

# Menu Category
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

# Menu
class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete = models.PROTECT, default=None)


# Drinks Category
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


# Drinks
class Drinks(models.Model):
    drink = models.CharField(max_length = 200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete = models.PROTECT, default=None)

class Customer(models.Model):
    name = models.CharField(max_length = 200)
    reservation_day = models.CharField(max_length = 200)
    seats = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Logger(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log= models.TimeField()


class Booking(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count= models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)


class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField()

    # def __str__(self): 
    #     return f"{self.last_name}, {self.first_name}"

    