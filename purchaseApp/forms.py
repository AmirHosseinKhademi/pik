from django import forms
from .models import Purchase
from django.utils.translation import ugettext_lazy as _


class AddPurchaseFrom(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ['status']
        labels = {
            'title': _('title'),
            'price': _('price'),
            'group': _('group'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('title')})
        }

