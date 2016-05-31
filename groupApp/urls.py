from django.conf.urls import url

from groupApp.views import create_group

urlpatterns = [
    url(r'^new$', create_group)
]