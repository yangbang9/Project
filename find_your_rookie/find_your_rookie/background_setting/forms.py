from socket import fromshare
from django import forms

class ForwardForm(forms.Form):
    Goals = forms.BooleanField(label='Goals', required=False)
    Assists1 = forms.BooleanField(label='Assists1', required=False)
    SpG = forms.BooleanField(label='SpG', required=False)
    KeyP1 = forms.BooleanField(label='KeyP1', required=False)
    Drb = forms.BooleanField(label='Drb', required=False)    
       
class MidfielderForm(forms.Form):
    Assists2 = forms.BooleanField(label='Assists2', required=False)
    KeyP2 = forms.BooleanField(label='KeyP2', required=False)
    AvgP = forms.BooleanField(label='AvgP', required=False)
    Crosses = forms.BooleanField(label='Crosses', required=False)
    LongB = forms.BooleanField(label='LongB', required=False)
    
class DefenderForm(forms.Form):
    Tackles = forms.BooleanField(label='Tackles', required=False)
    Inter = forms.BooleanField(label='Inter', required=False)
    Clear = forms.BooleanField(label='Clear', required=False)
    Blocks = forms.BooleanField(label='Blocks', required=False)