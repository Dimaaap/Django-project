import jwt
from time import time
from django.conf import settings
from django.contrib.auth.models import User

from books.filters import ValuesFilter


def check_form_errors_service(form: callable):
    for i in form.errors:
        return form.errors[i][0]


def filter_field_from_model_service(model: callable, field, value):
    field_filter = ValuesFilter()
    return model.objects.filter(**field_filter(field, value))


def get_field_from_model_by_fields_service(model: callable, field, value):
    field_filter = ValuesFilter()
    return model.objects.get(**field_filter(field, value))


def get_reset_password_token_service(user_id, expires_in=600):
    return jwt.encode(
        {
            'reset_password': user_id, 'exp': time() + expires_in
        }, settings.SECRET_KEY, algorithm='HS256'
    ).decode('utf-8')


def verify_reset_password_token_service(token):
    try:
        user_id = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])['reset_password']
    except:
        return
    return User.objects.get(id=user_id)
