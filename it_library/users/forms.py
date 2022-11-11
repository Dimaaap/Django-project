from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from books.services import filter_objects_from_db_service


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Ім'я користувача: ",
        error_messages={'required': ''},
        help_text='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    email = forms.EmailField(
        label='Email: ',
        error_messages={'required': ''},
        help_text='',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    password1 = forms.CharField(
        label="Пароль: ",
        error_messages={'required': ''},
        help_text='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    password2 = forms.CharField(
        label="Пароль(повторно): ",
        error_messages={'required': ''},
        help_text='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if filter_objects_from_db_service(User, 'email', email):
            raise ValidationError('Користувач з таким email вже існує')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if filter_objects_from_db_service(User, 'username', username):
            raise ValidationError("Таке ім'я користувача вже використовується")
        return username


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Ваш username: ',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'autocomplete': 'off'})
                               )
    email = forms.EmailField(label='Ваш email: ',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'autocomplete': 'off'}))
    password = forms.CharField(label='Введіть пароль: ',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'autocomplete': 'off'}))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Ваш старий пароль ',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'autocomplete': 'off'}))
    password1 = forms.CharField(label='Ваш новий пароль ',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'autocomplete': 'off'}))
    password2 = forms.CharField(label='Повторіть пароль ',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'autocomplete': 'off'}))

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if all([i.isdigit() for i in password1]) or all([i.isalpha() for i in password1]):
            raise ValidationError('Пароль має містити цифри і букви')
        return password1

    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']
        if not old_password:
            raise ValidationError('Заповніть всі поля')
        return old_password
