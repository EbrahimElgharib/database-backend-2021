from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns= [
   path('profile/', views.profile, name='profile'),
   path('profile/manager/', views.managerView, name='manager'),
   path('profile/driver/', views.driverView, name='driver'),
   path('profile/paramedic/', views.paramedic, name='paramedic'),
]