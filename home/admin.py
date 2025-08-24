from django.contrib import admin
from .models import Restaurant, MenuItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'email', 'phone_number', 'city', 'created_at')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'restaurant']
    search_fields = ['name', 'description']

