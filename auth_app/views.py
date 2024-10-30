from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout 

from .models import UserProfile
from .forms import RegisterForm , LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            UserProfile.objects.create(user=User.objects.get(username=form.cleaned_data['username']))

            return redirect('home')
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
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # print(form.cleaned_data)
        # exit()
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'auth_app/login.html', {'form': form,'error': form.errors})
    
    return render(request, 'auth_app/login.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('home')
