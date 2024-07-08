from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'registration.html', context)


class UserLoginView(LoginView):
    template_name = 'login.html'
    form = AuthenticationForm


def logout_user(request):
   logout(request)
   return redirect("login")


@login_required
def update_profile(request):
   if request.method == 'POST':
       form = ProfileForm(request.POST, instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('tasks')
   else:
       form = ProfileForm(instance=request.user.profile)
  
   context = {'form': form}
   return render(request, 'update-profile.html', context)