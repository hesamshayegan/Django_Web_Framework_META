from django.contrib import admin
from .models import Drinks, Menu, MenuCategory, DrinksCategory, Customer

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Customer)