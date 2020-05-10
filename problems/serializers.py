from rest_framework import serializers
from .models import Problem, Category, Item

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('pk','problem', 'description', 'createdAt')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'category')
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('pk', 'item')

class CategoryItemSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Category
        fields = ('pk', 'category','items')

class ProblemCategoryItemSerializer(serializers.ModelSerializer):
    categories = CategoryItemSerializer(many=True)
    class Meta:
        model = Problem
        fields = ('pk', 'problem', 'categories')