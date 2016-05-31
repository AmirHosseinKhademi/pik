from django.contrib.auth import authenticate, login
from django.shortcuts import render

from groupApp.forms import CreateGroupForm, AddMemberForm
from groupApp.models import Group, UserGroup


def create_group(request):

    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST, prefix='create_group')
        member_form= AddMemberForm(request.POST, prefix='add_member')

        if create_form.is_valid():# and member_form.is_valid():
            create_form_cd = create_form.cleaned_data
            # member_form_cd = member_form.cleaned_data
            group = Group(title=create_form_cd['title'])#, admin=create_form_cd['admin'])
            print(group)
            # members = UserGroup(group=group, )
            group.save()
        print(create_form)
        print(member_form)
        return render(request, 'CreateGroup.html', {'create_form': CreateGroupForm(), 'member_form': AddMemberForm()})
    else:
        create_form = CreateGroupForm(prefix='create_group')
        member_form = AddMemberForm(prefix='add_member')
        # print(create_form)
        return render(request, 'CreateGroup.html', {'create_form': create_form, 'member_form': member_form})