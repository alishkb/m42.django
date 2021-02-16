from django import forms
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    re_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'phone', 'last_name')

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] and cd['re_password'] and cd['password'] != cd['re_password']:
            raise forms.ValidationError('passwords must match')
        return cd['re_password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'
    
    def clean_password(self):
        return self.initial('password')


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    password = forms.CharField(label='password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter password'}))
    re_password = forms.CharField(label='confrim password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 're-Enter password'}))

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     user = User.objects.filter(email=email)
    #     if user.exists():
    #         raise forms.ValidationError('This email already exists')
    #     return email

    # def clean(self):
    #     clean_data = super().clean()
    #     p = clean_data.get('password')
    #     rp =clean_data.get('re_password')
    #     if p and rp:
    #         if p != rp:
    #             raise forms.ValidationError('passwords must match')
