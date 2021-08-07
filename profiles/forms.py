from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ('username','first_name','last_name', )
