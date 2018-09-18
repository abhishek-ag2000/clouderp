from django import forms
from userprofile.models import Profile

class profileform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(profileform, self).__init__(*args, **kwargs)
		self.fields['E_mail'].widget.attrs = {'class': 'form-control',}
		self.fields['Qualification'].widget.attrs = {'class': 'form-control',}
		self.fields['Phone_no'].widget.attrs = {'class': 'form-control',}
		self.fields['Skills'].widget.attrs = {'class': 'form-control',}
		self.fields['Full_Name'].widget.attrs = {'class': 'form-control',}
		self.fields['Permanant_Address'].widget.attrs = {'class': 'form-control',}
		self.fields['District'].widget.attrs = {'class': 'form-control',}
		self.fields['State'].widget.attrs = {'class': 'form-control',}
		self.fields['Country'].widget.attrs = {'class': 'form-control',}




	class Meta:
		model = Profile
		fields = ('Full_Name', 'E_mail','Qualification','Permanant_Address','District','State','Country', 'Phone_no', 'Skills', 'image')


	def clean(self):
		cleaned_data = super(profileform, self).clean()
		E_mail = cleaned_data.get('E_mail')
		Phone_no = cleaned_data.get('Phone_no')
