from django import forms

class SignInForm(forms.Form):
    name = forms.CharField(max_length=20, 
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
    password=forms.CharField(max_length=20, 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
