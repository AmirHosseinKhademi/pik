from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render

from UserApp.models import CustomizedUser
from groupApp.forms import CreateGroupForm, AddMemberForm

from dal import autocomplete


@login_required
def create_group(request):
    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST, prefix='create_group')
        member_form = AddMemberForm(request.POST, prefix='add_member')

        if create_form.is_valid() and member_form.is_valid():

            admin = request.user
            create_form_obj = create_form.save(commit=False)
            create_form_obj.admin = admin
            create_form_obj.save()

            member_form_obj = member_form.save(commit=False)
            member_form_obj.group = create_form.instance
            member_form_obj.save()
            member_form.save_m2m()

        return render(request, 'CreateGroup.html', {'create_form': CreateGroupForm(), 'member_form': AddMemberForm()})

    else:
        create_form = CreateGroupForm(prefix='create_group')
        member_form = AddMemberForm(prefix='add_member')
        return render(request, 'CreateGroup.html', {'create_form': create_form, 'member_form': member_form})


class MembersAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CustomizedUser.objects.all()
        if self.q:
            qs = qs.filter(Q(title__contains=self.q))
        return qs
