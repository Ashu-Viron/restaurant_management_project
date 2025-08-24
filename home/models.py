from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255, default="Unnamed Restaurant")
    owner_name = models.CharField(max_length=255, default="Unknown Owner")
    email = models.EmailField(unique=True, default="example@example.com")
    phone_number = models.CharField(max_length=20, default="0000000000")
    address = models.TextField(default="Not Provided")
    city = models.CharField(max_length=100, default="St. Louis")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu_items",null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"