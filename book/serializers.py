from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','name','description','count','authors']
class DetailBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['name','description','count','authors']