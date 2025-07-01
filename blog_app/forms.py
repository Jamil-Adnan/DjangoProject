from django import forms
from .models import Blogpost
    
class BlogpostForm(forms.ModelForm):
    
    class Meta:
        model = Blogpost
        fields = ["author","image","post"]
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name (max 12 chars)', 'maxlength': 12}),
            'post': forms.Textarea(attrs={'maxlength': 200, 'rows': 4, 'cols': 40, 'placeholder': 'Write a short post...'}),
        }
