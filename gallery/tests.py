from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.
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

