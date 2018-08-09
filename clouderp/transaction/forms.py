from django import forms
from django.db.models import Sum

from transaction.models import ledger1,transaction,journal

class transactionForm(forms.ModelForm):
	target = forms.ChoiceField(label='Particulars')
	class Meta:
		model = transaction
		fields = (
			'Creation_Date',
			'target',
			'Debit',
			)

	def clean(self):
		target = self.cleaned_data.get('target')
		if target:
			target = target.split()
			self.cleaned_data['By1'] = ledger1.objects.get(pk=target[0])

		return self.cleaned_data



transactionFormSet = forms.inlineformset_factory(ledger1,transaction,form=transactionForm,extra=1)


class journalForm(forms.ModelForm):
	target1 = forms.ChoiceField(label='Particulars')
	class Meta:
		model = journal
		fields = (
			'Creation_Date',
			'target1',
			'Credit',
			)

		def clean(self):
			target1 = self.cleaned_data.get('target1')
			if target1:
				target1 = target1.split()
				self.cleaned_data['To1'] = ledger1.objects.get(pk=target1[0])

			return self.cleaned_data


journalFormSet = forms.inlineformset_factory(ledger1,journal,form=journalForm,extra=1)