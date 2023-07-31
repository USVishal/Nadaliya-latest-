from django.db import models
from django.contrib.auth.hashers import make_password
# User Registration Section

SEMESTER_CHOICES = (
    ("Approved", "Approved"),
    ("Declin", "Declin"),
   
)
ROLE_CHOICES = (
    ("user1", "Staff"),
    ("user2", "User"),
   
)
CATG_CHOICES = (
    ("Wrap", "Wrap"),
    ("Icecreem", "Iceceem"),
    ("Shake", "Shake"),
   
)
class User_Registration(models.Model):
    
    name = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    nickname = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    role = models.CharField(max_length = 255,choices = ROLE_CHOICES,blank=True,null=True)    
    username = models.CharField(max_length=255,blank=True,null=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    status =models.CharField(max_length = 255,choices = SEMESTER_CHOICES,blank=True,null=True)
    banner_access = models.BooleanField(default=False)
    add_item_access = models.BooleanField(default=False)
    view_order_access = models.BooleanField(default=False)
    edit_item_access = models.BooleanField(default=False)
    def _str_(self):
        return self.nickname
    
    def get_email_field_name(self):
        return 'email'

# Create Artist Profile
class Profile_User(models.Model):
    user = models.ForeignKey(User_Registration, on_delete=models.SET_NULL, null=True, blank=True)
    firstname = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    phonenumber = models.CharField(max_length=20)
    secondnumber = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    gender = models.CharField(max_length=255,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    address =  models.TextField(blank=True,null=True)
    pro_pic = models.ImageField(upload_to='images/', default='static/images/default.png')


    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class category(models.Model):
    category_name=  models.CharField(max_length=255,blank=True,null=True)
    image = models.FileField(upload_to='images/category-banner', default='static/images/default.png')

class item(models.Model):
    user = models.ForeignKey(User_Registration, on_delete=models.SET_NULL, null=True, blank=True)
    category= models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=255,blank=True,null=True)
    title_description = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    rating = models.FloatField()
    buying_count = models.IntegerField()
    offer = models.FloatField(blank=True,null=True)
    image = models.FileField(upload_to='images/items', default='static/images/default.png')
   

