from django import forms
from .models import CommunicationEmails


class CommunicationsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommunicationsForm, self).__init__(*args, **kwargs)

    message = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = CommunicationEmails
        fields = ('category','from_email','subject','message')

    def clean(self):
        super(CommunicationsForm,self).clean()
        return self.cleaned_data