from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib import messages
from .forms import RegisterForm, UserLogin
from django.contrib.auth import login, logout


# регистрация пользователя
def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировалаись!')
        else:
            messages.error(request, 'Ошибка регистрации')
            form = RegisterForm()
    return render(request, 'register_user/register.html', {"form": form})


# вход в пользователя
def user_login(request):
    form = UserLogin(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при входе в аккаунт,\nпроверте все ли условия соблюдены.')
            form = UserLogin()
    return render(request, 'register_user/login.html', {'form': form})

# Выход из пользователя

def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('home')
