from .models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','book','user','plated_end_at']
class DetailOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['book','user','plated_end_at']