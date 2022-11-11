from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .services import *
from .forms import UserRegisterForm, LoginUserForm, ChangePasswordForm
from books.services import filter_objects_from_db_service


def register_user_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ви успішно реєструвались і авторизувались')
            return redirect('index_page')
    else:
        form = UserRegisterForm()
    errors = check_form_errors_service(form)
    context = {'title': 'Реєстрація', 'form': form, 'errors': errors}
    return render(request, 'users/register_user.html', context)


def login_user_view(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Ви авторизовані')
            return redirect('index_page')
    else:
        form = LoginUserForm()
    errors = check_form_errors_service(form)
    context = {'title': 'Авторизація', 'form': form, 'errors': errors}
    return render(request, 'users/login_user.html', context)


@login_required(login_url='/users/login')
def logout_user_view(request):
    logout(request)
    context = {'title': 'Розавторизація'}
    return render(request, 'users/logout_user.html', context)


@login_required(login_url='/users/login')
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user_old_password = form.cleaned_data['old_password']
            user_new_password = form.cleaned_data['password1']
            if user_new_password == user_old_password:
                messages.success(request, 'Пароль успішно змінено')

            user = filter_objects_from_db_service(User, 'password', user_old_password)
            if not user:
                messages.error(request, 'Неправильний пароль')
            else:
                user.set_password(user_new_password)
                user.save()
                messages.success(request, 'Пароль змінено успішно')
    else:
        form = ChangePasswordForm()
    errors = check_form_errors_service(form)
    context = {'title': 'Зміна паролю', 'form': form, 'errors': errors}
    return render(request, 'users/change_password.html', context)