from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200, default="Gourmet Manager")
    phone = models.CharField(max_length=20, default="+91 98765 43210")
    email = models.EmailField(default="info@gourmetmanager.com")
    address = models.TextField(default="123 Food Street, Culinary City")
    welcome_message = models.TextField(default="Welcome to our restaurant! We serve love on every plate.")
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, default="Main Course")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name