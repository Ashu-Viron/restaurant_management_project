from django.shortcuts import render
from datetime import datetime
from .models import Restaurant, MenuItem

def homepage(request):
    restaurant = Restaurant.objects.first()
    context = {
        'restaurant_name': restaurant.name if restaurant else 'Gourmet Manager',
        'restaurant_phone': restaurant.phone if restaurant else '+91 98765 43210',
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