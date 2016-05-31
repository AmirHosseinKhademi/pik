from django import forms

from groupApp.models import Group, UserGroup


class CreateGroupForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عنوان گروه'}))

    class Meta:
        model = Group
        exclude = ['creation_datetime']


class AddMemberForm(forms.ModelForm):

    class Meta:
        model = UserGroup
        exclude = ['join_datetime']