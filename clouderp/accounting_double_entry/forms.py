from django import forms
from django.forms import ModelForm, Textarea


from accounting_double_entry.models import journal,group1



class group1Forms(forms.ModelForm):

	class Meta:
		models = group1
		fields = ('group_Name', 'Master', 'Nature_of_group1', 'balance_nature', 'Group_behaves_like_a_Sub_Ledger', 'Nett_Debit_or_Credit_Balances_for_Reporting')
		widgets = {'group_Name': Textarea(attrs={'cols': 80, 'rows': 20})}
	
		

		def clean(self):
			cleaned_data = super(group1Forms, self).clean()
			group_Name = cleaned_data.get('group_Name')


class journalForm(forms.ModelForm):

	class Meta:
		model = journal
		fields = ('Particulars','Particulars_Credit','Debit','Credit')



		def clean(self):
			cleaned_data = super(journalForm, self).clean()  #simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
			Particulars_Credit = cleaned_data.get('Particulars_Credit')
			Particulars = cleaned_data.get('Particulars')

			


