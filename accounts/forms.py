from django import forms
# from .models import Profile
from django.contrib.auth.models import User
from .models import Crew, Employees, Manager, StationEmployees,Casualties
              

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['username',]
      # fields = ['email','first_name','last_name'] 

class EmployeesForm(forms.ModelForm):
   class Meta:
      model = Employees
      fields = ['employee_name', 'national_number','phone_number', 'address','birth_date','emp_type']


class ManagerForm(forms.ModelForm):
   class Meta:
      model = Manager
      fields = ['station', ]

class StationEmployeesForm(forms.ModelForm):
   class Meta:
      model = StationEmployees
      fields = ['station','crew', 'job_title' , 'number_of_accidents']

class CrewForm(forms.ModelForm):
   class Meta:
      model = Crew
      fields = ['crew_status',]


class CasualtiesForm(forms.ModelForm):
   class Meta:
      model = Casualties
      fields = '__all__'





