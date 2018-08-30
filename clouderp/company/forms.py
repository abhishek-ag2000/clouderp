from django import forms
from company.models import company




class DateInput(forms.DateInput):
    input_type = 'date'




class companyform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(companyform, self).__init__(*args, **kwargs)
		self.fields['Name'].widget.attrs = {'class': 'form-control',}
		self.fields['Type_of_company'].widget.attrs = {'class': 'form-control',}
		self.fields['Shared_Users'].widget.attrs = {'class': 'form-control',}
		self.fields['Address'].widget.attrs = {'class': 'form-control',}
		self.fields['Country'].widget.attrs = {'class': 'form-control',}
		self.fields['State'].widget.attrs = {'class': 'form-control',}
		self.fields['Pincode'].widget.attrs = {'class': 'form-control',}
		self.fields['Telephone_No'].widget.attrs = {'class': 'form-control',}
		self.fields['Mobile_No'].widget.attrs = {'class': 'form-control',}
		self.fields['Financial_Year_From'].widget.attrs = {'class': 'form-control',}
		self.fields['Books_Begining_From'].widget.attrs = {'class': 'form-control',}


	class Meta:
		model = company
		fields = ('Name', 'Type_of_company','Shared_Users','Address','Country','State','Pincode','Telephone_No','Mobile_No','Financial_Year_From','Books_Begining_From')
		widgets = {
            'Financial_Year_From': DateInput(),
            'Books_Begining_From': DateInput(),
        }
