from django.shortcuts import render
from datetime import datetime
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer,RestaurantStaffLoginSerializer,MenuItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password


@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        restaurant_id = request.query_params.get('restaurant_id', None)
        if restaurant_id:
            items = MenuItem.objects.filter(restaurant_id=restaurant_id)
        else:
            items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def menu_item_detail(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['POST'])
def restaurant_staff_login(request):
    serializer = RestaurantStaffLoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            restaurant = Restaurant.objects.get(email=email)
        except Restaurant.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify password
        if check_password(password, restaurant.password):
            return Response({"message": "Login successful", "restaurant_id": restaurant.id}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# POST - Register a new restaurant
@api_view(['POST'])
def create_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET - List all restaurants
@api_view(['GET'])
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


# GET by ID - View details of a single restaurant
@api_view(['GET'])
def get_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)


# PUT - Update a restaurant’s information
@api_view(['PUT'])
def update_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RestaurantSerializer(restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE - Delete a restaurant
@api_view(['DELETE'])
def delete_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

    restaurant.delete()
    return Response({'message': 'Restaurant deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class RestaurantRegistrationView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


def homepage(request):
    restaurant = Restaurant.objects.first()
    context = {
        'restaurant_name': restaurant.name if restaurant else 'Gourmet Manager',
        'restaurant_phone': restaurant.phone_number if restaurant else '+91 98765 43210',
        'welcome_message': restaurant.welcome_message if restaurant else 'Welcome to our restaurant!',
        'year': datetime.now().year
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'about.html', context)

def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    context = {
        'menu_items': menu_items,
        'year': datetime.now().year
    }
    return render(request, 'menu.html', context)

def contact(request):
    restaurant = Restaurant.objects.first()
    contact_info = {
        'phone': restaurant.phone if restaurant else '+91 98765 43210',
        'email': restaurant.email if restaurant else 'info@gourmetmanager.com',
        'address': restaurant.address if restaurant else '123 Food Street, Culinary City'
    }
    context = {
        'contact_info': contact_info,
        'year': datetime.now().year
    }
    return render(request, 'contact.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def reservations(request):
    return render(request, 'reservations.html')

def orders(request):
    return render(request, 'orders.html')

def staff(request):
    return render(request, 'staff.html')

def reports(request):
    return render(request, 'reports.html')

