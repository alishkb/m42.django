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
        return self.initial['password']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    last_name = forms.CharField(label='last name', max_length=100, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter last name'}))
    # email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    phone = forms.CharField(label='phone', max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phone'}))
    password = forms.CharField(label='password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter password'}))
    re_password = forms.CharField(label='confrim password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 're-Enter password'}))

class PhoneLoginForm(forms.Form):
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 0912 123 4567'}))

    #for checking that this number is in db or not:
    def clean_phone(self):
        phone = User.objects.filter(phone=self.cleaned_data['phone'])
        if not phone.exists():
            raise forms.ValidationError('این شماره وجود ندارد')
        return self.cleaned_data['phone']

class VerifyPhoneForm(forms.Form):
    code = forms.IntegerField()