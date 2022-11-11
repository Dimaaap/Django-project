from django.urls import path

from .views import *

urlpatterns = [
    path('', send_email_request_view, name='send_email'),
    path('reset/<str:token>/', reset_password_view, name='reset_password'),
    path('fail/', fail_token_view, name='fail_token')

]