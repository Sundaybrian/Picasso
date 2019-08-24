from django.test import TestCase
from .models import Category,Image,Location,tags
from django.contrib.auth.models import User

class CategoryTestClass(TestCase):

    #set up method
    def setUp(self):
        self.food=Category(category_name='Food')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))   

     #Testing save method
    def test_save_method(self):
        self.food.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)  

    #Testing save multiple
    def test_save_multiple_categories(self):
        self.food.save_category()

        test_dog=Category(category_name='Dogs')
        test_dog.save_category()

        categories=Category.objects.all()
        self.assertEqual(len(categories),2)


    #Testiing delete method
    def test_delete_method(self):
        self.food.save_category()

        test_dog=Category(category_name='Dogs')
        test_dog.save_category()

        test_dog.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),1)


#Location Test
class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        self.nrb=Location(loc_name='Nairobi')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nrb,Location))   

     #Testing save method
    def test_save_method(self):
        self.nrb.save_loc()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)  

    #Testing save multiple
    def test_save_multiple_locations(self):
        self.nrb.save_loc()

        test_mbs=Location(loc_name='Mombasa')
        test_mbs.save_loc()

        locations=Location.objects.all()
        self.assertEqual(len(locations),2)


    #Testiing delete method
    def test_delete_method(self):
        self.nrb.save_loc()

        test_mbs=Location(loc_name='Mombasa')
        test_mbs.save_loc()

        test_mbs.delete_loc()
        locations=Location.objects.all()
        self.assertEqual(len(locations),1)


# Image tests

class ImageTestClass(TestCase):

    def setUp(self):
        #creating me as picasso
        self.sb=User(username='omwamithegreat',email='sundaypriest@outlook.com')   
        self.sb.save_author()

        self.foota=Category(category_name='Football')
        self.foota.save_category()

        #creating a new tag and saving it
        self.new_tag=tags(tag_name='#coyg')
        self.new_tag.save()

        self.new_img=Image(img_name='Lfc Gunned Down',img_desc='Gunners shed Liverpool nightmare to slaughter their counterparts in a 7 goal thriller',img_loc='Liverpool',img_category=self.foota,author=self.sb)
        self.new_img.save()

        self.new_img.tags.add(self.new_tag)     

