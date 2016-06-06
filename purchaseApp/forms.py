from django import forms
from .models import Purchase


class AddPurchaseFrom(forms.ModelForm):
    # title = forms.CharField()
    # price = forms.IntegerField()
    # group = forms.ModelChoiceField(queryset=Group.objects.all(),
    #                                widget=forms.Select(attrs={'id': 'in_purchase_select_group'}))

    def clean(self):
        # pass
        cleaned_data = super(AddPurchaseFrom, self).clean()
        price = cleaned_data.get('price', None)
        group = cleaned_data.get('group', None)
        title = cleaned_data.get('title', None)
        if not price:
            raise forms.ValidationError("قیمت وارد نشده است")
        if not group:
            raise forms.ValidationError("گروه انتخاب نشده است")
        if not title:
            raise forms.ValidationError("عنوان خرید نمیتواند خالی باشد")

    class Meta:
        model = Purchase
        exclude = ['status']
        labels = {
            'title': 'عنوان',
            'price': 'قیمت',
            'group': 'گروه',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'عنوان'}),
            'group': forms.Select(attrs={'id': 'in_purchase_select_group'})
        }

