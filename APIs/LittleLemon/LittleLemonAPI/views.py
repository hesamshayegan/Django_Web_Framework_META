from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.core.paginator import Paginator, EmptyPage

# TemplateHTMLRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import renderer_classes

# StaticHTMLRenderer
from rest_framework.renderers import StaticHTMLRenderer

# function baed views with @api_view decorator
# Create your views here.
@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        # to filter queries
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name:
            # I need to use a double underscore between the model and 
            # the field to filter a linked model like a category inside the menu item
            items = items.filter(category__title=category_name)
        if to_price:
            # lte (Less than or equal to) is a conditional operator or fields lookup
            # items = items.filter(price__lte=to_price)

            # to filter for exact price
            items = items.filter(price=to_price)
        # to order
        if ordering:
            # items = items.order_by(ordering)
            # if I have multiple fields to order
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        # to search
            if search:
                items = items.filter(title__startswith=search)
                # case insensitive
                # items = items.filter(title__istartswith=search)

                # to search if characters are anywhere in the title
                # items = items.filter(title__contains=search)
                # case insensitive
                # items = items.filter(title__icontains=search)
            
        # pagination
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        # serialization
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        if serialized_item.is_valid(raise_exception=True):
            serialized_item.save()
            return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)





# TemplateHTMLRenderer
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-item.html')

# StaticHTMLRenderer
@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)