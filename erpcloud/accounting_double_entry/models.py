from django.conf import settings
from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models import Sum
from company.models import company

class group1(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	group_Name = models.CharField(max_length=32,unique=True,error_messages={'unique':"This Group Name has already been registered"})
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
		('Not Applicable','Not Applicable'),# to be removed
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
	if master_level == "Fixed_Asset":
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
	User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True,related_name='Companys')
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
	Closing_balance = models.DecimalField(max_digits=10,decimal_places=2)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("accounting_double_entry:ledgerdetail", kwargs={'pk':self.pk})



		
class journal(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True,related_name='Companyname')
	Date = models.DateField()
	By = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='Debitledgers')
	To = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='Creditledgers')
	Debit = models.DecimalField(max_digits=10,decimal_places=2)
	Credit = models.DecimalField(max_digits=10,decimal_places=2)


	def __str__(self):
		return str(self.By)

	def get_absolute_url(self):
		return reverse("accounting_double_entry:detail", kwargs={'pk':self.pk})

	def clean(self):
		if self.Debit != self.Credit:
			raise ValidationError('Debit Amount Should Be Equal To Credit Amount')
		elif self.To == self.By:
			raise ValidationError('Paricular Entry Cannot be same')

# check passed dates - if strting date == ledger creation date && closing date == ledger creation date:
#							return opening balance + debit count - credit count (on that date only)
#							return debit count on strting date							
#							return credit count on strting date

#						elif(strting date not equal to ledger creation date):
#							return opening balance + debit count - credit count (till that opening date only)
#							return debit count from strting date to ending date
#							return credit count from strting date to closing date
#							calculate closing balance = opn balanace + debit count + credit count
#


	def debitsum(self):#2date range arguements # validation strting date cannot be greater than ending date
		Debitcount = ledger1.objects.annotate(debitsum=Sum('Debitledgers__Debit')).values_list('name','debitsum')
		# filter with the date range
		return Debitcount


	def creditsum(self):
		Creditcount = ledger1.objects.annotate(creditsum=Sum('Creditledgers__Credit')).values_list('name','creditsum')
		return Creditcount



@receiver(pre_save, sender=ledger1)
def update_user_closing_balance(sender,instance,*args,**kwargs):
	debit = instance.Debitledgers.aggregate(debit=Sum('Debit'))['debit']
	credit = instance.Creditledgers.aggregate(credit=Sum('Credit'))['credit']
	Closing_balance = instance.Opening_Balance + debit - credit
	instance.Closing_balance = Closing_balance	






# class closing_balance:
# 	name=
# 	date= # TILL TODAY
# 	balance = #EACH DAYS BALANCE


# 	def calculation:# signal
# 	use functions
# 	get_or_create (data_from_functions)
# 	pass

# class difference_in_opening_balance:
	
# 	date = 
# 	balance =
# 	def calculation:# signal
# 	use functions
# 	get_or_create (data_from_functions)
# 	pass


# class netprofit:
# 	date=
# 	balance=
# 	def 
# 	def calculation:# signal
# 	use functions
# 	get_or_create (data_from_functions)
# 	pass










		




	














