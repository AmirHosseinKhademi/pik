from django.conf.urls import include, url
from django.contrib import admin
from .views import CheckCredential, RegisterUser, user_profile, change_password, logout_user

urlpatterns = [
    url(r'^login$', CheckCredential, name ='loginUser'),
    url(r'^register$', RegisterUser, name ='registerUser'),
    url(r'^profile$', user_profile, name='user_profile'),
    url(r'^changepassword$', change_password, name='change_password'),
    url(r'^logout$', logout_user, name='logout_user'),
]