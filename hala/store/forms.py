from django import forms
from .models import Doners,DonationItems,RequestDonation

class CreateDonersForm(forms.ModelForm):
    class Meta:
        model = Doners
        fields = ['donrName','donrAddress','donrMobile','donrtype']
        widgets = {
            'donrName': forms.TextInput(attrs={ 'class':'form-control','placeholder':'enter your name'} ),
            'donrAddress': forms.TextInput(attrs={'class':'form-control'} ),
            'donrMobile': forms.TextInput(attrs={'class':'form-control'}),
            'donrtype': forms.Select(attrs={'class':'form-control'} ),
        }


class EditDonersform(forms.ModelForm):
    class Meta:
        model = Doners
        fields = ['donrName','donrAddress','donrMobile','donrtype']
        widgets = {
            'donrName': forms.TextInput(attrs={ 'class':'form-control','placeholder':'enter your name'} ),
            'donrAddress': forms.TextInput(attrs={'class':'form-control'} ),
            'donrMobile': forms.TextInput(attrs={'class':'form-control'}),
            'donrtype': forms.Select(attrs={'class':'form-control'} ),
        }

class CreateDonationItemsForm(forms.ModelForm):
    class Meta:
        model = DonationItems
        fields = ['ditmType','ditmDescription','ditmQuantity','ditmStatus','ditmDoner']
        widgets = {
            'ditmType': forms.Select(attrs={'class':'form-control'} ),
            'ditmDescription': forms.TextInput(attrs={ 'class':'form-control','placeholder':'enter your name'} ),
            'ditmQuantity': forms.TextInput(attrs={'class':'form-control'} ),
            'ditmStatus': forms.Select(attrs={'class':'form-control'}),
            'ditmDoner': forms.Select(attrs={'class':'form-control'} ),#need to modifiy
        }

class EditDonationItemsForm(forms.ModelForm):
    class Meta:
        model = DonationItems
        fields = ['ditmType','ditmDescription','ditmQuantity','ditmStatus','ditmDoner']
        widgets = {
            'ditmType': forms.Select(attrs={'class':'form-control'} ),
            'ditmDescription': forms.TextInput(attrs={ 'class':'form-control','placeholder':'enter your name'} ),
            'ditmQuantity': forms.TextInput(attrs={'class':'form-control'} ),
            'ditmStatus': forms.Select(attrs={'class':'form-control'}),
            'ditmDoner': forms.Select(attrs={'class':'form-control'} ),
            
        }

