from django.contrib import admin

# Register your models here.
from problems.models import Problem
from problems.models import Category
from problems.models import Item

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    inlines = [ItemInline]

class ProblemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['problem']}),
        # ('Date info', {'fields': ['createdAt']}),
    ]
    inlines = [CategoryInline]
    list_filter = ['createdAt']
    search_fields = ['problem']

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Item)