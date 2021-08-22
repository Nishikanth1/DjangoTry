from django import forms

from .models import  Articles

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            'title',
            'content',
            'active',
        ]

    #def clean_title