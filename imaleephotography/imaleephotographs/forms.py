from django import forms
from .models import Messages
class messageForm(forms.ModelForm):
    class Meta:
        model=Messages
        fields=['name','email','subject','Message']