from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template import loader
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages

from .forms import ResetPasswordRequestForm, ResetPasswordForm
from .services import (get_field_from_model_by_fields_service,
                       get_reset_password_token_service, verify_reset_password_token_service,
                       check_form_errors_service)


def send_email_request_view(request):
    if request.method == 'POST':
        form = ResetPasswordRequestForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            user = get_field_from_model_by_fields_service(User, 'email', user_email)
            subject = 'Відновлення паролю'
            token = get_reset_password_token_service(user.id)
            html_message = loader.render_to_string('send_emails/email_text.html', {
                'username': user.username,
                'token': token
            })
            from_email = settings.EMAIL_HOST_USER
            recipients = [user_email]
            message = 'Текстова версія HTML'
            mail = send_mail(subject, message, from_email, recipients, html_message=html_message)
            if mail:
                messages.success(request,
                                 f'Лист на пошту {user_email} було успішно '
                                 f'надіслано,перейдіть туди для отримання подальших вказівок')
            else:
                messages.error(request, f'При надсиланні листа сталась помилка')
    else:
        form = ResetPasswordRequestForm()
    errors = check_form_errors_service(form)
    context = {'form': form, 'errors': errors}
    return render(request, 'send_emails/reset_password_request.html', context)


def reset_password_view(request, token):
    user = verify_reset_password_token_service(token)
    if not user:
        return redirect(fail_token_view)
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            current_user = get_field_from_model_by_fields_service(User, 'username', user.username)
            current_user.set_password(password)
            current_user.save()
            messages.success(request, f'Пароль для користувача {user.username} успішно змінено')
    else:
        form = ResetPasswordForm()
    errors = check_form_errors_service(form)
    context = {'form': form, 'errors': errors}
    return render(request, 'send_emails/reset_password.html', context)


def fail_token_view(request):
    return render(request, 'send_emails/fail_token.html')
