from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render

from UserApp.models import CustomizedUser
from groupApp import admin
from groupApp.forms import CreateGroupForm, AddMemberForm
from groupApp.models import Group, UserGroup

from dal import autocomplete


@login_required
def create_group(request):
    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST, prefix='create_group')
        member_form = AddMemberForm(request.POST, prefix='add_member')

        if create_form.is_valid and member_form.is_valid():
            admin = request.user
            create_form_obj = create_form.save(commit=False)
            create_form_obj.admin = admin
            create_form_obj.save()
            member_form_obj = member_form.save(commit=False)
            member_form_obj.group = create_form_obj
            member_form_obj.save()
            # create_form_cd = create_form.cleaned_data
            # member_form_cd = member_form.cleaned_data
            # group = Group(title=create_form_cd['title'], admin=create_form_cd['admin'])
            # members = UserGroup(group=group, )
            # group.save()
        # return render(request, 'CreateGroup.html', {'create_form': CreateGroupForm()})
        return render(request, 'CreateGroup.html', {'create_form': CreateGroupForm(), 'member_form': AddMemberForm()})
    else:
        create_form = CreateGroupForm(prefix='create_group')
        member_form = AddMemberForm(prefix='add_member')
        # print(create_form)
        # return render(request, 'CreateGroup.html', {'create_form': create_form})
        return render(request, 'CreateGroup.html', {'create_form': create_form, 'member_form': member_form})


class MembersAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CustomizedUser.objects.all()
        if self.q:
            qs = qs.filter(Q(title__contains=self.q))
        return qs
