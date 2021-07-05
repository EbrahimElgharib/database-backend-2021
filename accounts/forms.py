from django import forms
# from .models import Profile
from django.contrib.auth.models import User
              

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['username','email','first_name','last_name'] 
      # fields = ['email','first_name','last_name'] 

# class ProfileForm(forms.ModelForm):
#    image = forms.ImageField(error_messages={'invalid':("Image Files Only!")}, widget=forms.FileInput)
#    class Meta:
#       model = Profile
#       # fields = ['image', 'phone_number','country', 'address','education']
#       fields = ['image','phone_number','country']
#       # fields = ['user','phone_number','address','image']