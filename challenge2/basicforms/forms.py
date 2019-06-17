from django import forms
from django.core import validators
from basicforms.models import Users
import re


class UserForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) < 5:
            raise forms.ValidationError("Name is required")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if len(data) == 0:
            raise forms.ValidationError("email is required")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    class Meta:
        model = Users
        fields = '__all__'
