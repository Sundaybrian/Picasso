from django.db import models
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    
    def save_photographer(self):
        self.save()

class tags(models.Model):
    '''
    models to create #tags to bind to photos
    '''
    tag_name=models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


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

    @classmethod
    def fetch_category_id(cls,search_term):

        try:
            category=cls.objects.filter(category_name=search_term).first()
            return category.id
            
        except ObjectDoesNotExist:
            return None
            
        



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
    img_loc=models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    img_category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    pub_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Photographer,on_delete=models.CASCADE)
    tags=models.ManyToManyField(tags)
    image=models.ImageField(upload_to='images/',default='')

       
    def __str__(self):
        return f'Image{self.img_name}-{self.img_loc}-{self.img_category}-{self.pub_date}'

    @classmethod
    def get_photos(cls):
        '''
        method that fetches photos with date published
        '''
        photos=cls.objects.order_by('pub_date')

        return photos

    @classmethod
    def search_by_category(cls,search_term_id):
        photos=cls.objects.filter(img_category_id=search_term_id)
        return photos    


