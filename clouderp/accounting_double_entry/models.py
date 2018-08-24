from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class group1(models.Model):
	group_Name = models.CharField(max_length=32,unique=True)
	Name = (
		('Primary','Primary'),
		('Fixed_Asset','Fixed_Asset'),
		('Current_Assets','Current_Assets'),
		('Liabilities','Liabilities'),
		('Current_Liabilities','Current_Liabilities'),
		('Capital','Capital'),
		('Loans','Loans'),
		('Income','Income'),
		('Expenses','Expenses'),
		)
	
    		
	Master = models.CharField(max_length=32,choices=Name,default='Primary')

	

	Name1 = (
		('Assets','Assets'),
		('Expenses','Expenses'),
		('Income','Income'),
		('Liabilities','Liabilities'),
		('Not Applicable','Not Applicable'),
		)

	Nature_of_group1 = models.CharField(max_length=32,choices=Name1,default='Assets')

	Nature = (
		('Debit','Debit'),
		('Credit','Credit'),
		('Not Applicable','Not Applicable'),
		)

	balance_nature = models.CharField(max_length=32,choices=Nature,default='Debit')
	Group_behaves_like_a_Sub_Ledger = models.BooleanField(default=False)
	Nett_Debit_or_Credit_Balances_for_Reporting = models.BooleanField(default=False)
	
	

	def __str__(self):
		return self.group_Name


	def get_absolute_url(self):
		return reverse("accounting_double_entry:groupdetail", kwargs={'pk':self.pk})


def group1_master1(master1_level):
	if master1_level == "Primary":
		nat = "Assets"
	elif master1_level == "Primary":
		nat = "Expenses"
	elif master1_level == "Primary":
		nat = "Income"
	elif master1_level == "Primary":
		nat = "Liabilities"
	else:
		nat = 'Not Applicable'
	return nat

@receiver(pre_save, sender=group1)
def update_user_Nature_of_group1(sender,instance,*args,**kwargs):
	Nature_of_group1 = group1_master1(instance.Master)
	instance.Nature_of_group1 = Nature_of_group1



def balance_master(master_level):
	if master_level == "Primary":
		bal_nat = "Debit"
	elif master_level == "Fixed_Asset":
		bal_nat = "Debit"
	elif master_level == "Current_Assets":
		bal_nat = "Debit"
	elif master_level == "Liabilities":
		bal_nat = "Credit"
	elif master_level == "Current_Liabilities":
		bal_nat = "Credit"
	elif master_level == "Capital":
		bal_nat = "Credit"
	elif master_level == "Loans":
		bal_nat = "Credit"
	elif master_level == "Income":
		bal_nat = "Credit"
	elif master_level == "Expenses":
		bal_nat = "Debit"
	else:
		bal_nat = 'Not Applicable'
	return bal_nat
	



@receiver(pre_save, sender=group1)
def update_user_balance_nature(sender,instance,*args,**kwargs):
	balance_nature = balance_master(instance.Master)
	instance.balance_nature = balance_nature

	

class ledger1(models.Model):
	Creation_Date = models.DateField(default=datetime.now)
	name = models.CharField(max_length=32,unique=True)
	group1_Name = models.ForeignKey(group1,on_delete=models.CASCADE)
	Opening_Balance = models.DecimalField(max_digits=19,decimal_places=2)	
	User_Name = models.CharField(max_length=100)
	Address = models.TextField()
	State_Name = (
		('Choose','Choose'),
		('Andra Pradesh','Andra Pradesh'),
		('Arunachal Pradesh','Arunachal Pradesh'),
		('Assam','Assam'),
		('Bihar','Bihar'),
		('Chhattisghar','Chhattisghar'),
		('Goa','Goa'),
		('Gujrat','Gujrat'),
		('Haryana','Haryana'),
		('Himachal Pradesh','Himachal Pradesh'),
		('Jammu and Kashmir','Jammu and Kashmir'),
		('Jharkhand','Jharkhand'),
		('Karnataka','Karnataka'),
		('Kerala','Kerala'),
		('Madhya Pradesh','Madhya Pradesh'),
		('Maharasthra','Maharasthra'),
		('Manipur','Manipur'),
		('Meghalaya','Meghalaya'),
		('Mizoram','Mizoram'),
		('Nagaland','Nagaland'),
		('Odisha','Odisha'),
		('Punjab','Punjab'),
		('Rajasthan','Rajasthan'),
		('Sikkim','Sikkim'),
		('Tamil Nadu','Tamil Nadu'),
		('Telengana','Telengana'),
		('Tripura','Tripura'),	
		('Uttar Pradesh','Uttar Pradesh'),
		('Uttarakhand','Uttarakhand'),
		('West Bengal','West Bengal'),
		)
	State = models.CharField(max_length=100,choices=State_Name,default='Choose')
	Pin_Code = models.BigIntegerField()
	PanIt_No = models.CharField(max_length=100,blank=True)
	GST_No = models.CharField(max_length=100,blank=True)
	# Closing_Balance = models.FloatField(blank=True, default=0.0)

	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("accounting_double_entry:ledgerdetail", kwargs={'pk':self.pk})
		

class journal(models.Model):
	Particulars = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='Debitledgers')
	Particulars_Credit = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='Creditledgers')
	Debit = models.DecimalField(max_digits=10,decimal_places=2)
	Credit = models.DecimalField(max_digits=10,decimal_places=2)


	def __str__(self):
		return str(self.Particulars)

	def get_absolute_url(self):
		return reverse("accounting_double_entry:detail", kwargs={'pk':self.pk})

	def clean(self):
		if self.Debit != self.Credit:
			raise ValidationError('Debit Amount Should Be Equal To Credit Amount')
		elif self.Particulars == self.Particulars_Credit:
			raise ValidationError('Paricular Entry Cannot be same')










		




	














