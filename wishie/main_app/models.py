from django.db import models
from django.forms import ModelForm


class Item(models.Model):
    desc = models.CharField(max_length=500)
