from django.shortcuts import render
from datetime import datetime
from .models import Restaurant
def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html', {'restaurant_name': restaurant.name if restaurant else 'My Restaurant'})


from django.conf import settings
from django.shortcuts import render

def home(request):
    restaurant_name = "My Restaurant"  
    phone_number = settings.RESTAURANT_PHONE_NUMBER
    return render(request, "home.html", {
            "restaurant_name": restaurant_name,
            "phone_number": phone_number
    })

