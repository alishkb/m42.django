from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    password = forms.CharField(label='password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter password'}))
    re_password = forms.CharField(label='confrim password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 're-Enter password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('This email already exists')
        return email

    def clean(self):
        clean_data = super().clean()
        p = clean_data.get('password')
        rp =clean_data.get('re_password')
        if p and rp:
            if p != rp:
                raise forms.ValidationError('passwords must match')
