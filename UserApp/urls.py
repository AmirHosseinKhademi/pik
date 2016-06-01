from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login$', 'UserApp.views.CheckCredential', name ='loginUser'),
    url(r'^register$', 'UserApp.views.RegisterUser', name ='registerUser'),

]