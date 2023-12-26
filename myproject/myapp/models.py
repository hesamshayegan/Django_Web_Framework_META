from django.db import models

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
