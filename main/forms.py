from django import forms
from .models import ShortURL

class ShortURLForm(forms.ModelForm):
    original_url = forms.URLField(
        label="Your URL Link ",
        max_length=2000,
        widget=forms.URLInput(attrs={'name':'orginal_url', 'id':'orginal_url', 'placeholder':'https://example.com'})
    )
     
    class Meta:
        model = ShortURL
        fields = ['original_url']
