from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','gender','email','parents_mobile','aadhar_number','address','profile_pic','admission_date']
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control', 'id':'first_name'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control', 'id':'last_name'}),
                    'gender':forms.Select(attrs={'class':'form-control', 'id':'gender'}, choices=['Male','Female','Others']),
                    'email':forms.EmailInput(attrs={'class':'form-control', 'id':'email'}),
                    'parents_mobile':forms.NumberInput(attrs={'class':'form-control', 'id':'email'}),
                    'aadhar_number':forms.NumberInput(attrs={'class':'form-control', 'id':'aadhar_number'}),
                    'address':forms.Textarea(attrs={'class':'form-control','id':'address','rows':'10'}),
                    'profile_pic':forms.FileInput(attrs={'class':'form-control', 'id':'profile_pic'}),
                    'admission_date':forms.TextInput(attrs={'type':'date','class':'form-control', 'id':'admission_date'})
                  }
        
        error_messages = {
            "first_name": {
                "reqired": "First Name is required",
            },
            "last_name": {
                "reqired": "Last Name is required",
            },
           "email":{
               "reqired": "Last Name is required",
               "maxlength":"Email should be not more than 250",
           }
        }
