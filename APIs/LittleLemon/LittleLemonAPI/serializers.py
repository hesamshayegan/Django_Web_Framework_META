from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal
from rest_framework.validators import UniqueValidator
import bleach


# class MenuItemSerializer(serializers.Serialize):
    
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()



#class MenuItemSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = MenuItem
#        fields = ['id', 'title', 'price', 'inventory']

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # I need to see category only for GET request 
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        # sanitize data method 2
        attrs['title'] = bleach.clean(attrs['title'])
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)

    # sanitize data
    # def validate_title(self, value):
    #     return bleach.clean(value)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']

        extra_kwargs = {
            'title': {
                'validators': [
                    UniqueValidator(
                        queryset=MenuItem.objects.all()
                    )
                ]
            }       
        }
        

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)