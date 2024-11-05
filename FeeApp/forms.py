from django import forms
from .models import FeeMaster


class FeeForm(forms.ModelForm):
    class Meta:
        model = FeeMaster
        fields = ['fee_name','is_active']
        widgets = {
                'fee_name':forms.TextInput(attrs={'class':'form-control', 'id':'fee_name'}),
                'is_active':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
            }