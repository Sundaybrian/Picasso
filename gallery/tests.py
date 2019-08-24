from django.test import TestCase
from .models import Category,Image,Location,tags,Photographer


class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rembrandt= Photographer(first_name = 'Rembrandt', last_name ='Harmenszoon', email ='vanRijn@goldenage.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.rembrandt,Photographer))

        # Testing Save Method
    def test_save_method(self):
        self.rembrandt.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)        


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
        self.sb=Photographer(first_name='omwami',last_name="the great",email='sundaypriest@outlook.com')   
        self.sb.save_photographer()

        self.foota=Category(category_name='Football')
        self.foota.save_category()

        self.lfc=Location(loc_name='Liverpool')
        self.lfc.save_loc()

        #creating a new tag and saving it
        self.new_tag=tags(tag_name='#coyg')
        self.new_tag.save()

        self.new_img=Image(img_name='Lfc Gunned Down',img_desc='Gunners shed Liverpool nightmare to slaughter their counterparts in a 7 goal thriller',img_loc=self.lfc,img_category=self.foota,author=self.sb)
        self.new_img.save()

        self.new_img.tags.add(self.new_tag)  


    def tearDown(self):
        Photographer.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()
        Category.objects.all().delete()

    def test_get_photos(self):
        photos=Image.get_photos()
        self.assertTrue(len(photos)>0)

    def test_delete_photo(self):

        self.new_img.save()
        self.new_img.tags.add(self.new_tag)  

        test_user=Photographer(first_name='olly',last_name="olly",email='test@outlook.com')   
        test_user.save_photographer()

        test_rugby=Category(category_name='Rugby')
        test_rugby.save_category()

        test_nkr=Location(loc_name='Nakuru')
        test_nkr.save_loc()

        #creating a new tag and saving it
        test_rugby_tag=tags(tag_name='#simba')
        test_rugby_tag.save()

        test_img=Image(img_name='Simba Sevens',img_desc='Simba hammers 89-21',img_loc=test_nkr,img_category=test_rugby,author=test_user)
        test_img.save()

        test_img.tags.add(test_rugby_tag)  
        
        images=Image.objects.all()
        test_img.delete_photo()
        self.assertEqual(len(images),1)




