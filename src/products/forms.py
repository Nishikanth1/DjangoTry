from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='',  widget=forms.TextInput(attrs={"placeholder":"Your title placeholder"}))
    email       = forms.EmailField()
    description = forms.CharField(
                                  required=False,
                                  widget=forms.Textarea(
                                         attrs={
                                             "class": "new-class-name two",
                                             "id": "my-id-for-textarea",
                                             "rows": 20,
                                             "cols": 70
                                         }
                                  ))
    price       = forms.DecimalField(initial=199.22)

    class Meta:
        model = Product
        fields = ['title',
                  'description',
                  'price'

                  ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "cfe" in title:
            raise forms.ValidationError("title does not contain CFE")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("email does not have edu")
        return email



class RawProductForm(forms.Form):
    title       = forms.CharField(label='',  widget=forms.TextInput(attrs={"placeholder":"Your title placeholder"}))
    description = forms.CharField(
                                  required=False,
                                  widget=forms.Textarea(
                                         attrs={
                                             "class": "new-class-name two",
                                             "id": "my-id-for-textarea",
                                             "rows": 20,
                                             "cols": 70
                                         }
                                  ))
    price       = forms.DecimalField(initial=199.22)