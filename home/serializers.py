from rest_framework import serializers
from .models import Restaurant,MenuItem

class RestaurantStaffLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Restaurant name must be at least 3 characters long.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits.")
        return value

    def validate_email(self, value):
        if not value.endswith(".com"):
            raise serializers.ValidationError("Email must end with '.com'")
        return value

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'