from django.urls import path

from . import views

app_name = 'reporting_accident'

urlpatterns = [
        path('', views.accident_report),
        

        

]


