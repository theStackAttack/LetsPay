from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import PayUser, Promos


class UserSignUp(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = PayUser
        exclude = ('user', )

class PromosForm(forms.ModelForm):
    class Meta:
        model = Promos
        fields = ('phone', 'email', 'amount', 'active', )

class PromoWithdraw(forms.ModelForm):
    class Meta:
        model = Promos
        fields = ('phone', 'email', 'promoCode', )
            


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
