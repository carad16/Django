from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))