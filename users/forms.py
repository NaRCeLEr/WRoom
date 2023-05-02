from django.contrib.auth import get_user_model
from django.forms import forms, ModelForm
from django import forms

User = get_user_model()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password', 'is_superuser', 'is_active', 'is_staff']

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