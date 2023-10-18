# from django import forms
# from .models import steganography

# class SteganographyForm(forms.ModelForm):
#     class Meta:
#         model = steganography
#         fields = ['image', 'message', 'password']

from django import forms

class EncodeImageForm(forms.Form):
    image = forms.ImageField()
    message = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    dest = forms.CharField(initial='encoded_image.png')
