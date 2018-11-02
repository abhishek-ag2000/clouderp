from django import forms
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase,Sales,Stock_Total
import datetime
from django.db.models import Q
from django.forms import inlineformset_factory
from accounting_double_entry.models import ledger1

class DateInput(forms.DateInput):
    input_type = 'date'

class Stockgroup_form(forms.ModelForm):
	class Meta:
		model   = Stockgroup
		fields  = ('name', 'under', 'quantities')

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Stockgroup_form, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs       = {'class': 'form-control',}
		self.fields['under'].queryset 	       = Stockgroup.objects.filter(User= self.User,Company = self.Company)
		self.fields['under'].widget.attrs      = {'class': 'form-control select2',}


class Simpleunits_form(forms.ModelForm):
	class Meta:
		model   = Simpleunits
		fields  = ('symbol', 'formal')

	def __init__(self, *args, **kwargs):
		super(Simpleunits_form, self).__init__(*args, **kwargs)
		self.fields['symbol'].widget.attrs = {'class': 'form-control',}
		self.fields['formal'].widget.attrs = {'class': 'form-control',}

class Compoundunits_form(forms.ModelForm):
	class Meta:
		model   = Compoundunits
		fields  = ('firstunit', 'conversion','secondunit')

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Compoundunits_form, self).__init__(*args, **kwargs)
		self.fields['firstunit'].queryset = Simpleunits.objects.filter(User= self.User,Company = self.Company)
		self.fields['firstunit'].widget.attrs = {'class': 'form-control select2',}
		self.fields['conversion'].widget.attrs = {'class': 'form-control',}
		self.fields['secondunit'].queryset = Simpleunits.objects.filter(User= self.User,Company = self.Company)
		self.fields['secondunit'].widget.attrs = {'class': 'form-control select2',}


class Stockdata_form(forms.ModelForm):
	class Meta:
		model  = Stockdata
		fields = ('stock_name', 'under', 'unitsimple', 'unitcomplex', 'gst_rate', 'hsn')

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Stockdata_form, self).__init__(*args, **kwargs)
		self.fields['stock_name'].widget.attrs  = {'class': 'form-control',}
		self.fields['under'].queryset = Stockgroup.objects.filter(User= self.User,Company = self.Company)
		self.fields['under'].widget.attrs       = {'class': 'form-control select2',}
		self.fields['unitsimple'].queryset = Simpleunits.objects.filter(User= self.User,Company = self.Company)
		self.fields['unitsimple'].widget.attrs  = {'class': 'form-control select2',}
		self.fields['unitcomplex'].queryset = Compoundunits.objects.filter(User= self.User,Company = self.Company)
		self.fields['unitcomplex'].widget.attrs = {'class': 'form-control select2',}
		self.fields['gst_rate'].widget.attrs        = {'class': 'form-control',}
		self.fields['hsn'].widget.attrs         = {'class': 'form-control',}

class Purchase_form(forms.ModelForm):
	class Meta:
		model  = Purchase
		fields = ('date','Address','GSTIN','PAN','State','Contact','DeliveryNote','Supplierref','Mode', 'ref_no', 'Party_ac', 'purchase', 'Total_Amount')
		widgets = {
            'date': DateInput(),
        }

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Purchase_form, self).__init__(*args, **kwargs)
		self.fields['date'].widget.attrs     = {'class': 'form-control',}
		self.fields['ref_no'].widget.attrs   = {'class': 'form-control',}
		self.fields['Party_ac'].queryset = ledger1.objects.filter(Q(User= self.User),Q(Company = self.Company) , Q(group1_Name__group_Name__icontains='Sundry Creditors') | Q(group1_Name__group_Name__icontains='Bank Accounts') | Q(group1_Name__group_Name__icontains='Cash-in-hand'))
		self.fields['Party_ac'].widget.attrs = {'class': 'form-control select2',}
		self.fields['purchase'].queryset = ledger1.objects.filter(User= self.User,Company = self.Company,group1_Name__group_Name__icontains='Purchase Accounts')
		self.fields['purchase'].widget.attrs = {'class': 'form-control select2',}
		self.fields['Total_Amount'].widget.attrs = {'class': 'form-control',}
		self.fields['Address'].widget.attrs = {'class': 'form-control',}
		self.fields['GSTIN'].widget.attrs = {'class': 'form-control',}
		self.fields['PAN'].widget.attrs = {'class': 'form-control',}
		self.fields['State'].widget.attrs = {'class': 'form-control',}
		self.fields['Contact'].widget.attrs = {'class': 'form-control',}
		self.fields['DeliveryNote'].widget.attrs = {'class': 'form-control',}
		self.fields['Supplierref'].widget.attrs = {'class': 'form-control',}
		self.fields['Mode'].widget.attrs = {'class': 'form-control',}

class Sales_form(forms.ModelForm):
	class Meta:
		model  = Sales
		fields = ('date','Address','GSTIN','PAN','State','Contact','DeliveryNote','Supplierref','Mode', 'ref_no', 'Party_ac', 'sales', 'Total_Amount')
		widgets = {
            'date': DateInput(),
        }

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Sales_form, self).__init__(*args, **kwargs)
		self.fields['date'].widget.attrs     = {'class': 'form-control',}
		self.fields['ref_no'].widget.attrs   = {'class': 'form-control',}
		self.fields['Party_ac'].queryset = ledger1.objects.filter(Q(User= self.User),Q(Company = self.Company) , Q(group1_Name__group_Name__icontains='Sundry Debtors') | Q(group1_Name__group_Name__icontains='Bank Accounts') | Q(group1_Name__group_Name__icontains='Cash-in-hand'))
		self.fields['Party_ac'].widget.attrs = {'class': 'form-control select2',}
		self.fields['sales'].queryset = ledger1.objects.filter(User= self.User,Company = self.Company,group1_Name__group_Name__icontains='Sales Account')
		self.fields['sales'].widget.attrs = {'class': 'form-control select2',}
		self.fields['Total_Amount'].widget.attrs = {'class': 'form-control',}
		self.fields['Address'].widget.attrs = {'class': 'form-control',}
		self.fields['GSTIN'].widget.attrs = {'class': 'form-control',}
		self.fields['PAN'].widget.attrs = {'class': 'form-control',}
		self.fields['State'].widget.attrs = {'class': 'form-control',}
		self.fields['Contact'].widget.attrs = {'class': 'form-control',}
		self.fields['DeliveryNote'].widget.attrs = {'class': 'form-control',}
		self.fields['Supplierref'].widget.attrs = {'class': 'form-control',}
		self.fields['Mode'].widget.attrs = {'class': 'form-control',}



class Stock_Totalform(forms.ModelForm):
	class Meta:
		model  = Stock_Total
		fields = ('stockitem', 'Quantity', 'rate', 'Disc', 'Total')

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Stock_Totalform, self).__init__(*args, **kwargs)
		self.fields['stockitem'].widget.attrs = {'class': 'form-control select2',}
		self.fields['Quantity'].widget.attrs = {'class': 'form-control',}
		self.fields['rate'].widget.attrs     = {'class': 'form-control',}
		self.fields['Disc'].widget.attrs = {'class': 'form-control',}
		self.fields['Total'].widget.attrs = {'class': 'form-control',}

Purchase_formSet = inlineformset_factory(Purchase, Stock_Total,
                                            form=Stock_Totalform, extra=6)


class Stock_Totalformsales(forms.ModelForm):
	class Meta:
		model  = Stock_Total
		fields = ('stockitem', 'Quantity', 'rate', 'Disc', 'Total_sales')

	def __init__(self, *args, **kwargs):
		self.User = kwargs.pop('User', None)		
		self.Company = kwargs.pop('Company', None)
		super(Stock_Totalformsales, self).__init__(*args, **kwargs)
		self.fields['stockitem'].widget.attrs = {'class': 'form-control select2',}
		self.fields['Quantity'].widget.attrs = {'class': 'form-control',}
		self.fields['rate'].widget.attrs     = {'class': 'form-control',}
		self.fields['Disc'].widget.attrs = {'class': 'form-control',}
		self.fields['Total_sales'].widget.attrs = {'class': 'form-control',}

Sales_formSet =  inlineformset_factory(Sales, Stock_Total,
                                            form=Stock_Totalformsales, extra=6)		


 
