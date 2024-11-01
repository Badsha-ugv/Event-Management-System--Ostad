import django.db
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.forms import AuthenticationForm

import django.urls
from .models import UserProfile
from .forms import RegisterForm 

from event.models import Event

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            UserProfile.objects.create(user=User.objects.get(username=form.cleaned_data['username']))

            return redirect('login')
        else:
            return render(
                request, "auth_app/register.html", {"form": form}
            )
    form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'auth_app/register.html',context)


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        # form = AuthenticationForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print('form data', form)
        print(username, password)
        
        # print(form.cleaned_data)
        # exit()
        if username and password:
            
            user = authenticate(request, username=username, password=password)

            print('user', user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('user not found')
                return render(request, 'auth_app/login.html', {'error':'username or password is incorrect'})

    return render(request, 'auth_app/login.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request, user_id=None):
    user = User.objects.get(id=user_id)
    my_events = Event.objects.filter(author=user)
    if user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
        context = {
            'profile': profile,
            'my_events': my_events
        }
        return render(request, 'auth_app/profile.html', context)
    else:
        return redirect('home')

def update_profile(request, user_id= None):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)

    if request.user == user and request.user.is_authenticated:
        if request.method == 'POST':
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')

            avatar = request.FILES.get('avatar')
            
            user.first_name = f_name
            user.last_name = l_name
            user.email = email
            user.save()
            profile.phone = phone
            profile.address = address
            if avatar:
                profile.avatar = avatar
            profile.save()
            return redirect(reverse('profile', args=(user.id,)))
