from django import forms

class SignupForm(forms.Form):
    receipent = forms.CharField(label="Email-ID", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

