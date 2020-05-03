from rest_framework import serializers
from .models import Problem, Category

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('pk','problem', 'description', 'createdAt')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'category')