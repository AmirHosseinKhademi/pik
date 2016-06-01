from dal import autocomplete
from django import forms

from groupApp.models import Group, UserGroup


class CreateGroupForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عنوان گروه'}))

    # title = forms.ModelMultipleChoiceField(
    #     queryset=Group.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(
    #         url='members-autocomplete'
    #     )
    # )

    class Meta:
        model = Group
        exclude = ['creation_datetime']


class AddMemberForm(forms.ModelForm):

    # member = forms.ModelMultipleChoiceField(
    #     queryset=Users.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='members-autocomplete')
    # )

    class Meta:
        model = UserGroup
        exclude = ['join_datetime']