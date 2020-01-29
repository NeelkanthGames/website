from django import forms
from .models import Videos, CurrentProject, CurrentProjectImages, News, Reviews

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


class CurrentProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CurrentProjectForm, self).__init__(*args, **kwargs)

    desc = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = CurrentProject
        fields = ('title', 'desc')

    def clean(self):
        super(CurrentProjectForm,self).clean()
        return self.cleaned_data

class CurrentProjectImageForm(forms.ModelForm):
    class Meta:
        model = CurrentProjectImages
        fields = ('image',)
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple':True})
        }

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = News
        fields = ('title', 'body')

    def clean(self):
        super(NewsForm, self).clean()
        return self.cleaned_data

class ReviewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewsForm, self).__init__(*args, **kwargs)

    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Reviews
        fields = ('full_name', 'organisation','body')

    def clean(self):
        super(ReviewsForm, self).clean()
        return self.cleaned_data