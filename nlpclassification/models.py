from django.db import models
from django import forms


# Create your models here.


class NameForm(forms.Form):
    question = forms.CharField(label='question', max_length=100)
    sentence = forms.CharField(label='sentence')


class FillMask(forms.Form):
    sentence = forms.CharField(label='sentence')
