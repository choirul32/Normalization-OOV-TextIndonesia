from django import forms

class TextForm(forms.Form):
	your_text = forms.CharField(label='Your text', max_length=100)