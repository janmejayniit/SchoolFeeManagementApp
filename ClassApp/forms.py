from dataclasses import fields
from django import forms
from .models import ClassMaster


class ClassMasterForm(forms.ModelForm):
    class Meta:
        model= ClassMaster
        fields = ['name']
        widgets = {
                    'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
                  }