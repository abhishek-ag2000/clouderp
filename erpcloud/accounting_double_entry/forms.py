from django import forms
from accounting_double_entry.models import journal,group1,ledger1,selectdatefield
from company.models import company
import datetime


class group1Form(forms.ModelForm):		
	class Meta:
		model = group1
		fields = ('group_Name', 'Master', 'Nature_of_group1', 'balance_nature', 'Group_behaves_like_a_Sub_Ledger', 'Nett_Debit_or_Credit_Balances_for_Reporting')
		widgets = {
			'group_Name': forms.TextInput(attrs= {'class' : 'form-control'}),
			
		}

	def __init__(self, *args, **kwargs):
		super(group1Form, self).__init__(*args, **kwargs)
		self.fields['Master'].widget.attrs = {'class': 'form-control select2',}
		self.fields['Nature_of_group1'].widget.attrs = {'class': 'form-control select2',}
		self.fields['balance_nature'].widget.attrs = {'class': 'form-control select2',}
		

class DateInput(forms.DateInput):
    input_type = 'date'


class Ledgerform(forms.ModelForm):

	class Meta:
		model = ledger1
		fields = ('Creation_Date', 'name', 'group1_Name', 'Opening_Balance', 'User_Name', 'Address', 'State', 'Pin_Code', 'PanIt_No', 'GST_No')
		widgets = {
            'Creation_Date': DateInput(),
        }

	def __init__(self, *args, **kwargs):
		super(Ledgerform, self).__init__(*args, **kwargs)
		self.fields['Creation_Date'].widget.attrs = {'class': 'form-control',}
		self.fields['name'].widget.attrs = {'class': 'form-control',}
		self.fields['group1_Name'].widget.attrs = {'class': 'form-control select2', 'placeholder':"Select Group",}
		self.fields['Opening_Balance'].widget.attrs = {'class': 'form-control',}
		self.fields['User_Name'].widget.attrs = {'class': 'form-control',}
		self.fields['Address'].widget.attrs = {'class': 'form-control',}
		self.fields['State'].widget.attrs = {'class': 'form-control select2',}
		self.fields['Pin_Code'].widget.attrs = {'class': 'form-control',}
		self.fields['PanIt_No'].widget.attrs = {'class': 'form-control',}
		self.fields['GST_No'].widget.attrs = {'class': 'form-control',}






class journalForm(forms.ModelForm):
	
	class Meta:
		model = journal
		fields = ('Date','By','To','Debit','Credit')
		widgets = {
            'Date': DateInput(),
        }

		def __init__(self, *args, **kwargs):
			super(journalForm, self).__init__(*args, **kwargs)
			self.fields['Debit'].widget.attrs = {'class': 'form-control',}
			self.fields['Credit'].widget.attrs = {'class': 'form-control',}
			self.fields['To'].widget.attrs = {'class': 'form-control select2',}
			self.fields['By'].widget.attrs = {'class': 'form-control select2',}
			self.fields['By'].queryset = ledger1.objects.filter(Company=self.kwargs['pk'])


class DateRangeForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(DateRangeForm, self).__init__(*args, **kwargs)
		self.fields['Start_Date'].widget.attrs = {'class': 'form-control',}
		self.fields['End_Date'].widget.attrs = {'class': 'form-control',}

	class Meta:
		model = selectdatefield
		fields = ('Start_Date', 'End_Date')
		widgets = {
			'Start_Date'  : DateInput(),
			'End_Date'    : DateInput(),
		}








			


