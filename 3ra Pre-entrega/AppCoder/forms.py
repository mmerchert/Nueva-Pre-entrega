from django import forms 


class CompraFormulario(forms.Form):

    producto = forms.CharField()
    numero = forms.IntegerField()