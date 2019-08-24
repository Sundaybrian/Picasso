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
