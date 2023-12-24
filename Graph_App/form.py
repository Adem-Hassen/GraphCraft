from django import forms

class Expression(forms.Form):
    expressionb=forms.CharField(label="",max_length=50,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
