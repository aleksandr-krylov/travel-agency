from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile
from datetime import date


def get_years(start_year, end_year):
    year_range = [start_year + delta for delta in range(end_year - start_year + 1)]
    return year_range


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True) # add an additional field to custom User form


    class Meta:
        # define a model that will be affected 
        model = User
        # specify the fields and their order we wanna put on the form 
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name', 'email']

         widgets = {
             'username': forms.TextInput(attrs={'class': 'form-control'}),
             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
         }


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = [
            'date_of_birth',
            'phone'
        ]
         
        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=get_years(1945, date.today().year),
                attrs={'class': 'form-control'}
                ),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (XXX) XXX-XX-XX'})
        }


class PassportForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = [
            'passport',
            'starts_date',
            'expires_date'
        ]

        widgets =  {
            'passport': forms.TextInput(attrs={'class': 'form-control'}),
            'starts_date':  forms.SelectDateWidget(
                years=get_years(1960, date.today().year),
                attrs={'class': 'form-control'}
                ),
            'expires_date':  forms.SelectDateWidget(
                years=get_years(date.today().year, date.today().year + 20),
                attrs={'class': 'form-control'}
                ),
        }



class ManagerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'is_staff'
        ]

        labels = {
            'is_staff': 'Статус менеджера'
        }

        widgets = {
            'is_staff': forms.CheckboxInput(attrs={'checked' : 'checked'})
        }