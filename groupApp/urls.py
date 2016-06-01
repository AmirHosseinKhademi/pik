from django.conf.urls import url

from groupApp.views import create_group, MembersAutoComplete

urlpatterns = [
    url(r'^new/$', create_group),
    url(r'^members-autocomplete/$', MembersAutoComplete.as_view(), name='members-autocomplete')
]
