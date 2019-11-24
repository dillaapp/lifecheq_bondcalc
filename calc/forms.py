from django import forms

from .models import Bondinfo

class Bondinfoform(forms.ModelForm):
    class meta:
        model = Bondinfo
        fields = [

               
               'House_price', 
               'Deposit',
               'Interest_rate',
               'Loan_term'
               
               ]
        
      