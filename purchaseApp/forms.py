from django import forms
from django.core.exceptions import ValidationError
from groupApp.models import Group


class AddPurchaseFrom(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'عنوان خرید'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 0, 'placeholder': 'کل هزینه'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   widget=forms.Select(attrs={'id': 'in_purchase_select_group'}))


    def __init__(self, *args, **kwargs):
        group_admin = kwargs.pop('group_admin', None)
        super(AddPurchaseFrom, self).__init__(*args, **kwargs)
        if group_admin:
            self.fields['group'].queryset = Group.objects.filter(admin=group_admin)

    # def save(self):
    #     pass

    def clean(self):
        cleaned_data = super(AddPurchaseFrom, self).clean()
        price = cleaned_data.get('price', None)
        if not price or price < 0:
            raise ValidationError('قیمت به صورت صحیح وارد نشده است')

    class Meta:
        # model = Purchase
        # exclude = ['status']
        labels = {
            'title': 'عنوان',
            'price': 'قیمت',
            'group': 'گروه',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'عنوان'}),
            'group': forms.Select(attrs={'id': 'in_purchase_select_group'})
        }

