from django import forms


class StringTableForm(forms.Form):
	string_key = forms.CharField(max_length=50)
	string_content = forms.CharField()
