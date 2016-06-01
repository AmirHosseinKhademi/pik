"""pik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from UserApp.views import index
from theme import urls as theme_url
from groupApp import urls as group_url
from UserApp import urls as user_url
# from purchase import urls as purchase_url
from .libraries import request
urlpatterns = [
    url(r'^user/', include(theme_url)),#why user?!
    url(r'^admin/', admin.site.urls),
    url(r'^group/', include(group_url)),
    url(r'^users/', include(user_url)),
    # url(r'^purchases/', include(purchase_url)),
    url(r'^api/', request.api, name="api"),
    url(r'^$', 'UserApp.views.index', name='index')

]
