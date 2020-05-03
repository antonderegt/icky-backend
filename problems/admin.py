from django.contrib import admin
from problems.models import Problem
from problems.models import Category
from problems.models import Item

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0

class ProblemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['problem']}),
        (None,          {'fields': ['description']}),
        # ('Date info',   {'fields': ['createdAt']}),
    ]
    inlines = [CategoryInline]
    list_filter = ['createdAt']
    search_fields = ['problem']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['category']}),
    ]
    inlines = [ItemInline]

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Category, CategoryAdmin)