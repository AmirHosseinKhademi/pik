import json
from apt_pkg import Group

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.gis import serializers
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from UserApp.models import CustomizedUser
from groupApp.forms import CreateGroupForm

from dal import autocomplete

from groupApp.models import Group


@login_required
def create_group(request):
    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST)

        if create_form.is_valid():

            print(create_form.cleaned_data['member'])

            admin = request.user.id
            create_form_obj = create_form.save(commit=False)
            create_form_obj.admin = admin
            create_form_obj.save()
            create_form.save_m2m()
        return render(request, 'CreateGroup.html', {'create_form': CreateGroupForm(), 'create': True})

    else:
        create_form = CreateGroupForm()
        # print(create_form)
        return render(request, 'CreateGroup.html', {'create_form': create_form, 'create': True})


class MembersAutoComplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CustomizedUser.objects.all()
        if self.q:
            qs = qs.filter(Q(email__contains=self.q))
        return qs


@login_required
def edit_groups(request):

    if request.method == 'GET':
        # print(request.user)
        groups = Group.objects.filter(admin=request.user.id)
        # print(groups)

        forms = modelformset_factory(Group, exclude=('creation_datetime', 'admin',), widgets={
            'member': autocomplete.ModelSelect2Multiple(url='members-autocomplete')
        })
        formset = forms(queryset=Group.objects.filter(admin=request.user.id))
        print(formset[-1].is_valid())
        # edit_form = []
        # for group in groups:
        #     edit_form.append(CreateGroupForm(instance=group))
        #     print(edit_form[0])

        # print(formset[-1]['member'])
        return render(request, 'CreateGroup.html', {'edit_group_form': formset, 'edit': True})

    else:
        pass


@login_required
def edit_group(request, id):

    if request.method == 'GET':
        group = Group.objects.get(id=id)
        edit_group_form = CreateGroupForm(instance=group)

        # print(edit_group_form)
        return render(request, 'CreateGroup.html', {'edit_group_form': edit_group_form, 'edit_group': True})

    elif request.method=='POST':
        instance = get_object_or_404(Group, id=id)
        edit_group_form = CreateGroupForm(request.POST, instance=instance)
        print(edit_group_form)

        if edit_group_form.is_valid():
            edit_group_form.save()
            return redirect(reverse('edit-groups'))


    return HttpResponse('ok')


@login_required
def get_members(request, id):
    group = Group.objects.filter(id=id)
    members = CustomizedUser.objects.filter(group__in=group)
    a = serializers.serialize('json', members)
    return HttpResponse(a, content_type='application/json')