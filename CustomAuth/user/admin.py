from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

User = get_user_model()

class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(label='password')
    password2 = forms.CharField(label='Confirm password')

    class Meta:
        model = User
        fields = {'email'}

    def clean_password(self):
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords do not match")
        return password2
    
    def save(self, commit=True):
        user = super.save(commit=False)
        user.set_password(self.password1)
        if commit:
            user.save()
        return user


#class UpdateUserForm(forms.ModelForm):


class UserAdmin(admin.ModelAdmin):
    search_field = ['email']

    class Meta:
        model = User

