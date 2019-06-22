from django import forms
from django.forms import ModelForm
from django.contrib import auth

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('desc',)
