from django import forms
from lista.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"