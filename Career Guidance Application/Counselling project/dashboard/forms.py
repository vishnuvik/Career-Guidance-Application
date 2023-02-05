from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['Rank', 'India', 'Ethiopia','Nepal', 'Tenth', 'Twelth']
