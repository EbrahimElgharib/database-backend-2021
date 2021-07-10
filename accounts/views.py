from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import manager
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Employees,Manager,StationEmployees, Crew

from .forms import CrewForm, UserForm, EmployeesForm, ManagerForm, StationEmployeesForm
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
   # test for sure it is emp or admin ?
   try:
      profile = Employees.objects.get(employee=request.user)
   except:
      return redirect('/')

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



def managerView(request):
   profile = Employees.objects.get(employee=request.user)
   manager = Manager.objects.get(manager=profile)

   # test
   print('here ___>>>')
   print(manager.manager.employee_name)
   print(manager.station.station_id)


   # return all crew
   crews = Crew.objects.filter(station=manager.station.station_id)
   # test
   print('crews after')
   for crew in crews:   
      print(crew.crew_status)

   context = {
      'manager' : manager,
      'crews' : crews,

   }
   return render(request, 'profile/manager.html',context)
   
   








   
def driverView(request):
   profile = Employees.objects.get(employee=request.user)
   station_emp = StationEmployees.objects.get(station_employee=profile)

   # test
   print('here ___>>>')
   print(station_emp.station.station_id)
   print(station_emp.crew.crew_id)


   if request.method == 'POST': # when click submit button
      # get request data to check valid and save
      # request.FILES ---> to save uploaded files
      # profile_form = EmployeesForm(request.POST, request.FILES, instance=profile)

      print('post send')
      crew_form = CrewForm(request.POST, instance=station_emp)
      # check valid --> save
      if crew_form.is_valid():
         print('station_emp_form is valid')
         # myprofile = crew_form.save(commit=False)
         # myprofile.crew_id = station_emp.crew
         crew_form.save()
         print('myprofile is saved')
         return redirect('/accounts/profile/driver')
      else:
         print('crew_form not valid')
         return redirect('/accounts/profile/driver')

   else: # when open page 
      print('else not POST')
      crew = Crew.objects.get(crew_id=station_emp.crew.crew_id)
      print('hi')
      print(crew.crew_id)
      crew_form = CrewForm(instance=crew)
      
   context = {
      'station_emp' : station_emp,
      'crew_form' : crew_form,

   }
   return render(request, 'profile/driver.html',context)




def paramedic(request):
   context = {}
   return render(request, 'profile/paramedic.html',context)