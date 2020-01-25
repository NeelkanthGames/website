from django import forms
from .models import Videos

class VideosToUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VideosToUploadForm, self).__init__(*args, **kwargs)
    active_flag = forms.BooleanField(required=False)
    desc = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Videos
        fields = ('title','videofile','desc','active_flag')
    def clean(self):
        super(VideosToUploadForm,self).clean()
        return self.cleaned_data
    def __str__(self):
        return str(self.title)