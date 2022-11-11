from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ResetPasswordRequestForm(forms.Form):
    email = forms.CharField(label='Ваш email: ', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if not user:
            raise ValidationError('Неправильно введений email')
        return email


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label='Ваш новий пароль: ', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторіть пароль: ', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if all([i.isdigit() for i in password1]) or all([i.isalpha() for i in password1]):
            raise ValidationError('Пароль має містити букви і цифри')
        return password1
