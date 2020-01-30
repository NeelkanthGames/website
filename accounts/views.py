from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserProfileInfoForm, UserForm
from django.contrib import messages
import pages.views as pages_v
urls_to_avoid = ('/user_login/','/user_register/','/user_logout/')

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                next = request.POST.get('next','/')
                if next in urls_to_avoid:
                    return pages_v.homepage(request)
                return HttpResponseRedirect(next)
            else:
                messages.error(request, 'Account has been inactivated', extra_tags='login')
                next = request.POST.get('next', '/')
                if next in urls_to_avoid:
                    return pages_v.homepage(request)
                return HttpResponseRedirect(next)
        else:
            messages.error(request, 'Invalid credentials',extra_tags='login')
            next = request.POST.get('next', '/')
            print(next)
            if next in urls_to_avoid:
                return pages_v.homepage(request)
            return HttpResponseRedirect(next)
    else:
        return render(request,'pages/homepage.html')

def user_registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.profile_pic = request.FILES.get('profile_pic', False)
            user.save()
            profile.save()
            login(request,user)
            next = request.POST.get('next', '/')
            print (next)
            if next in urls_to_avoid:
                return pages_v.homepage(request)
            return HttpResponseRedirect(next)
        else:
            messages.error(request,'Profile not created.', extra_tags='register')
            return render(request,r'accounts/register_user.html', {'user_form': UserForm(request.POST), 'profile_form': UserProfileInfoForm(request.POST,request.FILES)})

    else:
        return render(request,r'accounts/register_user.html', {'user_form': UserForm(), 'profile_form': UserProfileInfoForm()})


def user_logout(request):
    logout(request)
    return pages_v.homepage(request)
