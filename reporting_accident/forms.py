from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from . models import Accident, Reporter, Hospital

class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = ['reporter_name','phone_number', 'national_number','accident']



class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = ['accident_description', 'accident_volume', 'special_case_1', 'special_case_2', 'special_case_3', 'special_case_4', 'place_lat', 'place_long','accident_time','hospital']  