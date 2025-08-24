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
]