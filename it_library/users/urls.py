from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user_view, name='user_register'),
    path('login/', login_user_view, name='user_login'),
    path('logout/', logout_user_view, name='logout_user'),
    path('change_password/', change_password_view, name='change_password')
]
