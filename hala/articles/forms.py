from django import forms
from .models import Employee,Department

class CreateDepartmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['DName']
        widgets = {
            'DName': forms.TextInput(attrs={'class':'form-control'} ),
           

        }



class CreateEmployeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['cusName','cusLastname','cusphone','dep']
        widgets = {
            'cusName': forms.TextInput(attrs={ 'class':'form-control','placeholder':'enter your name'} ),
            'cusLastname': forms.TextInput(attrs={'class':'form-control'} ),
            'cusphone': forms.TextInput(attrs={'class':'form-control'}),
            'dep': forms.Select(attrs={'class':'form-control'} ),

        }

class editemployeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['cusName','cusLastname','cusphone','dep']
        widgets = {
            'cusName': forms.TextInput(attrs={'class':'form-control'} ),
            'cusLastname': forms.TextInput(attrs={'class':'form-control'} ),
            'cusphone': forms.TextInput(attrs={'class':'form-control'}),
            'dep': forms.Select(attrs={'class':'form-control'} )

        }
        