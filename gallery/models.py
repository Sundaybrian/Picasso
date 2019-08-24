from django.db import models

# Create your models here.
class Location(models.Model):
    loc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name


class Category:
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
