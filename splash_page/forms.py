from django import forms

class EmailPostForm(forms.Form):
	to = forms.EmailField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':"Your email address",
		'size':'50', 'type':'email'}), label='')
	class Meta:
  		fields = ['Email']