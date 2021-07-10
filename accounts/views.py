from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import manager
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Employees,Manager,StationEmployees

from .forms import UserForm, EmployeesForm, ManagerForm, StationEmployeesForm
# from .models import Profile

# Create your views here.

# show (Form) of all profile data to user
@login_required
def profile(request):
    user_form = UserForm(instance=request.user)
    context = {
      'user_form':user_form
   }
    return render(request, 'profile/profile.html',context)
    



# show (Form) of all profile data to user
@login_required
def profile(request):
   # get profile data to show it in form
   profile = Employees.objects.get(employee=request.user)
   # create emp station or manager
   if profile.emp_type==1:
      print('hi manager')
      print(profile.employee)
      manager = Manager.objects.get(manager=profile)
      print('manager is gahez')
      print(manager.manager)
      print(manager.station)

   else:
      station_emp = StationEmployees.objects.get(station_employee=profile)
      print('I am a station_emp')

   if request.method == 'POST': # when click submit button
      # get request data to check valid and save
      # request.FILES ---> to save uploaded files
      # profile_form = EmployeesForm(request.POST, request.FILES, instance=profile)

      print('post send')


      profile_form = EmployeesForm(request.POST, instance=profile)
      user_form = UserForm(request.POST, instance=request.user)
      # check valid --> save
      if profile_form.is_valid() and user_form.is_valid():
         print('profile+user forms are valid')
         if profile.emp_type==1:
            manager_form = ManagerForm(request.POST, instance=manager)
            if manager_form.is_valid():
               manager_form.save()
            else:
               print('manager form not valid')
               return redirect('/accounts/profile')
         else:
            station_emp_form = StationEmployeesForm(request.POST, instance=station_emp) 
            if station_emp_form.is_valid():
               station_emp_form.save()
            else:
               print('station_emp_form form not valid')
               return redirect('/accounts/profile')
            
         user_form.save()
         myprofile = profile_form.save(commit=False)
         myprofile.user = request.user
         myprofile.save()
      

         # # Go Back to profile.html
         # return redirect('/accounts/profile')

   else: # when open page 
      print('else not POST')
      profile_form = EmployeesForm(instance=profile)
      user_form = UserForm(instance=request.user)
      if profile.emp_type==1:
         manager_form = ManagerForm(instance=manager)
      else:
         station_emp_form = StationEmployeesForm(instance=station_emp)
   
   context = {
      'profile_form':profile_form,
      'user_form':user_form,
   }
   if profile.emp_type==1:
      context['manager_form'] = manager_form
   else:
      context['station_emp_form'] = station_emp_form
   
   return render(request, 'profile/profile.html',context)