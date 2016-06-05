from django import forms
from .models import CustomizedUser

class LoginForm (forms.Form):
    username = forms.CharField(max_length = 30, help_text=('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'), widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(max_length= 128 , widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))


class UserForm(forms.Form):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'placeholder': 'آدرس ایمیل'}))
    #debit_card = forms.IntegerField()
    password = forms.CharField(max_length= 20 , widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))
    password_confirmation = forms.CharField(max_length= 20 , widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه'}))

    def save(self):
        data = self.cleaned_data
        user = CustomizedUser(email=data['email'], name=data['name'])
        user.set_password(self.cleaned_data["password"])
        user.save()

