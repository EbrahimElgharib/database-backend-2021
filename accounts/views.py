from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import UserForm
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
    



# # show (Form) of all profile data to user
# @login_required
# def profile(request):
#    # get profile data to show it in form
#    profile = Profile.objects.get(user=request.user)

#    if request.method == 'POST': # when click submit button
#       # get request data to check valid and save
#       # request.FILES ---> to save uploaded files
#       profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
#       user_form = UserForm(request.POST, instance=request.user)
#       print('post send')
#       # check valid --> save
#       if profile_form.is_valid() and user_form.is_valid():
#          print('is valid')
#          user_form.save()
#          myprofile = profile_form.save(commit=False)
#          myprofile.user = request.user
#          myprofile.save()
      
#          # # Go Back to profile.html
#          # return redirect('/accounts/profile')

#    else: # when open page 
#       print('else not valid')
#       profile_form = ProfileForm(instance=profile)
#       user_form = UserForm(instance=request.user)
   
#    context = {
#       'profile_form':profile_form,
#       'user_form':user_form
#    }
#    return render(request, 'profile/profile.html',context)