from django import forms
from .models import User_Registration
from django.core.exceptions import ValidationError
import re
from django.core.validators import EmailValidator
from django.contrib import messages

from django.core.validators import RegexValidator

########################################################<<<<<<<<< Creator Userform >>>>>>>>>>>>>>>>>

from django import forms
from .models import item
from .models import User_Registration

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['user', 'category', 'name', 'title_description', 'description', 'price', 'rating', 'buying_count', 'offer', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the 'image' field not required
        self.fields['image'].required = False
################################################################
class User_RegistrationForm(forms.ModelForm):

        gender = forms.ChoiceField(choices=[
            ('Gender', 'Gender'),
            ('Female', 'Female'),
            ('Male', 'Male'),
            ('Other', 'Other'),
        ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'Gender', 'placeholder': 'Gender'}))
        
        # profession = forms.ChoiceField(choices=[
        #     ('Profession', 'Profession'),
        #     ('Actor', 'Actor'),
        #     ('Costume_Designer', 'Costume_Designer'),
            
        # ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'profession', 'placeholder': 'Profession'}))
        
        date_of_birth = forms.DateField(
             widget=forms.DateInput(attrs={'class': 'form-control item', 
                                           'id': 'birthday', 'placeholder': 'Date of Birth',
                                           'type': 'date',}))

        class Meta:
            model = User_Registration
            fields = '__all__'
        
            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Firstname'}),
                'lastname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Lastname'}),
                'nickname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Nickname'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Phone number','pattern': "^(0|\+91)?(?!6789)[6-9]\d{9}$",
    'message': "Enter a valid phone number"}),
 

                'email': forms.EmailInput(attrs={'class': 'form-control item','placeholder':'Email','id':'email','pattern':"[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$"}),
                # 'experience': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Experience'}),
                'role': forms.HiddenInput(attrs={'value': 'PREFIX_VALUE','id': 'role-field'}),
                # 'profileimage' : forms.FileField()

                }
            
          
            
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].required = False
            self.fields['password'].required = False

################################bannerimage##########################
from django import forms

class ImageForm(forms.Form):
    image_1 = forms.ImageField(label='Image 1')
    label_1 = forms.CharField(label='Label 1', max_length=100)

    image_2 = forms.ImageField(label='Image 2')
    label_2 = forms.CharField(label='Label 2', max_length=100)

    image_3 = forms.ImageField(label='Image 3')
    label_3 = forms.CharField(label='Label 3', max_length=100)

    image_4 = forms.ImageField(label='Image 4')
    label_4 = forms.CharField(label='Label 4', max_length=100)

    image_5 = forms.ImageField(label='Image 5')
    label_5 = forms.CharField(label='Label 5', max_length=100)


# #####################admin Add item#############################
class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['user', 'category', 'name', 'title_description', 'description', 'price', 'rating', 'buying_count', 'offer', 'image']
# ##################admin add staff #####################
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User_Registration
        fields = '__all__'
# ########################admin staff list #################
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User_Registration
        fields = '__all__'