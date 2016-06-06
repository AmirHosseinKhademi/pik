from .models import AccountingModel
from django.forms import ModelForm
from django.forms import TextInput, EmailInput


class ChargeAccountForm(ModelForm):
    class Meta:
        model = AccountingModel
        fields = ['amount']
        widgets = {
            'amount' : TextInput(attrs={'placeholder': 'مقدار شارژ به ریال', 'value': ''})
        }

    # def save(self, commit=True):
    #     data = self.cleaned_data
    #     self.

class CheckoutForm(ModelForm):
    class Meta:
        model = AccountingModel
        fields = ['amount']
        widgets = {
            'amount' : TextInput(attrs={'placeholder': 'مقدار تسویه به ریال'})
        }