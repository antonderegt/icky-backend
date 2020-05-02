from django.contrib import admin

# Register your models here.
from problems.models import Problem
from problems.models import Category
from problems.models import Item

admin.site.register(Problem)
admin.site.register(Category)
admin.site.register(Item)