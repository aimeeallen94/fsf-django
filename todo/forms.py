from django import forms
from .models import Item


# Using Djangos pre built features for form 

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
