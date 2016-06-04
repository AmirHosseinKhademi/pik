from django.conf.urls import include, url
from django.contrib import admin

from UserApp.views import CheckCredential, RegisterUser, user_profile

urlpatterns = [
    url(r'^login$', CheckCredential, name ='loginUser'),
    url(r'^register$', RegisterUser, name ='registerUser'),
    url(r'^profile$', user_profile, name='user_profile'),
]