from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reservations/', views.reservations, name='reservations'),
    path('orders/', views.orders, name='orders'),
    path('staff/', views.staff, name='staff'),
    path('reports/', views.reports, name='reports'),
    path('restaurants/register/', views.RestaurantRegistrationView.as_view(), name='restaurant-register'),
    path('restaurants/', views.list_restaurants, name='restaurant-list'),
    path('restaurants/create/', views.create_restaurant, name='restaurant-create'),
    path('restaurants/<int:pk>/', views.get_restaurant, name='restaurant-detail'),
    path('restaurants/<int:pk>/update/', views.update_restaurant, name='restaurant-update'),
    path('restaurants/<int:pk>/delete/', views.delete_restaurant, name='restaurant-delete'),
    path("restaurants/login/", views.restaurant_staff_login, name="restaurant-login"),
    path('menu-items/', views.menu_items, name='menu_items'),
    path('menu-items/<int:pk>/', views.menu_item_detail, name='menu_item_detail'),
]