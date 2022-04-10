from rest_framework import serializers
from .models import CustomUser
from order.models import Order
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','first_name', 'middle_name', 'last_name', 'email','password','role','is_active']
class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['first_name', 'middle_name', 'last_name', 'email','password','is_active']


class OrderByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['user','id','created_at']
