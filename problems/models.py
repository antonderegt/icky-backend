from django.db import models

class Problems(models.Model):
    problem = models.CharField("Problem name", max_length=255)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.problem

class Categories(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    category = models.CharField("Category name", max_length=255)

    def __str__(self):
        return self.category

class Items(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    item = models.CharField("Item name", max_length=255)

    def __str__(self):
        return self.item