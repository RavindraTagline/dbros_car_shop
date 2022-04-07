from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserForm


class UserSignup(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user/signup.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        else:
            return render(request, 'user/signup.html', {'form': form})


class UserLogin(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/vehicle/home-page/')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('/user/login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/user/login')


def UserLogout(request):
    logout(request)
    return redirect('/vehicle/home-page/')
