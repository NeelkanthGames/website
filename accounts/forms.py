from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

global email

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'data-toggle':'password'}))
    username = forms.CharField(help_text=None)

    class Meta():
        model = User
        fields = ('username', 'password', 'email')

    def clean(self):
        super(UserForm, self).clean()
        print (self.cleaned_data.get('password'))
        global email
        email = self.cleaned_data.get('email')
        return self.cleaned_data


class UserProfileInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)

    is_subscribed = forms.BooleanField(required=False)
    class Meta():
        model = UserProfileInfo
        fields = ('full_name', 'country', 'profile_pic', 'is_subscribed')

    def clean(self):
        super(UserProfileInfoForm, self).clean()
        full_name = self.cleaned_data.get('full_name')
        is_subscribed = self.cleaned_data.get('is_subscribed')
        if full_name:
            if not all(ch.isalpha() or ch.isspace() for ch in full_name):
                self._errors['full_name'] = self.error_class([
                    'Only letters and spaces allowed in first name'])
        if is_subscribed:
            global email
            print (email)
            if not email:
                self._errors['is_subscribed'] = self.error_class([
                    'Can only subscribe if email is provided'])

        return self.cleaned_data
