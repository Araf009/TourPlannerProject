from django import forms

class GuideRegInfoForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    userID=forms.CharField(max_length=100, required=True)
    email=forms.EmailField(required=True)
    address=forms.CharField(max_length=300, required=True)
    phone=forms.CharField(max_length=11)
    CHOICES= [('1', 'Male'), ('2', 'Female')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)