from django.shortcuts import render

# Create your views here.


def profile(request):
    context = {}
    return render(request, 'profile/profile.html',context)
    