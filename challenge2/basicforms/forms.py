from django import forms
from django.core import validators
from basicforms.models import Users


class UserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput, validators=[
                                     validators.MaxLengthValidator(0)]
                                 )

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher

    class Meta:
        model = Users
        fields = '__all__'
