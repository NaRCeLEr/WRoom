from django.contrib.auth import get_user_model
from .models import *
from django.forms import forms, ModelForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password']


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class AuthForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ChangeForm(forms.Form):
    new_username = forms.CharField(max_length=100)
    new_bio = forms.CharField(widget=forms.Textarea(), required=False)
    new_email = forms.EmailField(required=False)
    new_phone = PhoneNumberField(required=False)


class posteditForm(forms.Form):
    new_title = forms.CharField(max_length=100)
    new_image = forms.ImageField(required=False)
    new_text = forms.CharField(widget=forms.Textarea(), required=False)

class PostF(forms.Form):
    user = forms.CharField(required=False)
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
