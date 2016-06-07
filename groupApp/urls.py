from django.conf.urls import url

from groupApp.views import create_group, MembersAutoComplete, edit_group, get_members, groups_list

urlpatterns = [
    url(r'^new/$', create_group, name='create-group'),
    url(r'^members-autocomplete/$', MembersAutoComplete.as_view(), name='members-autocomplete'),
    url(r'^all/$', groups_list, name='groups-list'),
    url(r'^edit/(?P<id>\d+)$', edit_group, name='edit_group'),
    url(r'^(?P<id>\d+)/members$', get_members, name='get-members')
]
