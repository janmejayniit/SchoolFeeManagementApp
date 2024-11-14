from django import forms
from .models import FeeMaster, StudentFee, FeeInvoice
# from SessionApp.models import StudentSession, SessionMaster
# from ClassApp.models import ClassMaster

class FeeForm(forms.ModelForm):
    class Meta:
        model = FeeMaster
        fields = ['fee_name','is_active']
        widgets = {
                'fee_name':forms.TextInput(attrs={'class':'form-control', 'id':'fee_name'}),
                'is_active':forms.TextInput(attrs={'type':'checkbox', 'class':'form-control', 'id':'is_active'}),
            }

class FeeInvoiceForm(forms.ModelForm):
    class Meta:
       model = FeeInvoice
       fields=['session','class_id','student','payment_amount','gst_percentage','total_amount']
       widgets = {
                'session':forms.Select(attrs={'class':'form-control','id':'session'},choices=[]),
                'class_id':forms.Select(attrs={'class':'form-control','id':'class_id'}, choices=[]),
                'student':forms.Select(attrs={'class':'form-control','id':'student'}),
                'payment_amount':forms.TextInput(attrs={'class':'form-control', 'id':'payment_amount'}),
                'gst_percentage':forms.TextInput(attrs={'class':'form-control', 'id':'gst_percentage'}),
                'total_amount':forms.TextInput(attrs={'class':'form-control', 'id':'total_amount'}),
                # 'payment_date':forms.DateTimeInput(attrs={'class':'form-control', 'id':'payment_date'}),
            }
         

class StudentFeeFrom(forms.ModelForm):
    class Meta:
        model = StudentFee
        fields=['fee','amount']
        widgets = {
                'fee':forms.Select(attrs={'class':'form-control fee'}, choices=[]),
                'amount':forms.TextInput(attrs= {'class':'form-control amount'}),
            }

        # def clean(self):
        #     cleaned_data = super().clean()
            
        #     fees = self.data.getlist('fee',[])
        #     amounts = self.data.getlist('amount',[])
        #     invoice = cleaned_data.get('invoice')  

        #     if len(fees) != len(amounts):
        #         raise forms.ValidationError("The number of fees and amounts must match.")
        
        #     for fee, amount in zip(fees, amounts):
        #         StudentFee.objects.create(invoice=invoice, fee=fee, amount=amount)
        
        #     return cleaned_data