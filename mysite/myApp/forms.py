from django import forms
from .models import UploadOrderFileModel

class UploadOrderFileModel(forms.ModelForm):
    class Meta:
        model = UploadOrderFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False