# from socket import fromshare
from typing import List
from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["id", "item", "completed"]