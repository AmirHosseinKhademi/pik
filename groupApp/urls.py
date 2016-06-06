from django.conf.urls import url

from groupApp.views import create_group, MembersAutoComplete, edit_groups, edit_group, get_members

urlpatterns = [
    url(r'^new/$', create_group),
    url(r'^members-autocomplete/$', MembersAutoComplete.as_view(), name='members-autocomplete'),
    url(r'^edit$', edit_groups, name='edit-groups'),
    url(r'^edit/(?P<id>\d+)$', edit_group, name='edit_group'),
    url(r'^(?P<id>\d+)/members$', get_members, name='get-members')
]
