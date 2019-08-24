from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    loc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name

    
    def save_loc(self):

        '''
        method to save a category to db
        '''
        self.save() 

    def delete_loc(self):
        '''
        method to delete a category from db
        '''   
        self.delete() 


class Category(models.Model):
    category_name=models.CharField(max_length=50)


    def __str__(self):
        return self.category_name

    def save_category(self):

        '''
        method to save a category to db
        '''
        self.save() 

    def delete_category(self):
        '''
        method to delete a category from db
        '''
        self.delete()   

class Image(models.Model):
    img_name=models.CharField(max_length=100)
    img_desc=models.TextField()   
    img_loc=models.ForeignKey(Location,on_delete=models.CASCADE)
    img_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

       
    def __str__(self):
        return f'Image{self.img_name}-{self.img_loc}-{self.img_category}'
