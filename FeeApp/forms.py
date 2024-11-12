from django import forms
from .models import FeeMaster, StudentFee


class FeeForm(forms.ModelForm):
    class Meta:
        model = FeeMaster
        fields = ['fee_name','is_active']
        widgets = {
                'fee_name':forms.TextInput(attrs={'class':'form-control', 'id':'fee_name'}),
                'is_active':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
            }


class StudentFeeFrom(forms.ModelForm):
    class Meta:
        model = StudentFee
        fields=['session','class_id','student','fee','amount']
        widgets = {
                'session':forms.Select(attrs={'class':'form-control', 'id':'fee_name'}),
                'class_id':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
                'student':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
                'fee':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
                'amount':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
            }