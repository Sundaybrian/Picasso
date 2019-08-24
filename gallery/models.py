from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    loc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name


class Category:
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Image(models.Model):
    img_name=models.CharField(max_length=100)
    img_desc=models.TextField()   
    img_loc=models.ForeignKey(Location)
    img_category=models.ForeignKey(Category)
    pub_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
       
       def __str__(self):
           return f'Image{self.img_name}-{self.img_loc}-{self.img_category}'
