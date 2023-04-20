from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.hashers import check_password


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')



class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email not found')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        print(check_password(password ,CustomUser.objects.get(email=self.cleaned_data.get('email')).password))
        if not check_password(password, CustomUser.objects.get(email=self.cleaned_data.get('email')).password):
            raise forms.ValidationError('Password is incorrect')
        return password
