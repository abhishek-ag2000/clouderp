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
	Total_Debit = models.DecimalField(max_digits=10,decimal_places=2)
	Ctotal = models.DecimalField(max_digits=10,decimal_places=2)
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
	Debit = models.DecimalField(max_digits=10,decimal_places=2,)
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



#list conversion of django objects
def list_ledger(listleg):
	listledger = [['','','','']	for x in range(listleg.count())]
	f=0
	for q in listleg:
		k=0
		while k<4:
			if (k==0):
				listledger[f][k] = q.Creation_Date
			elif(k==1):
				listledger[f][k] = q.name
			elif(k==2):
				gn = q.group1_Name
				gn_bn = gn.balance_nature
				listledger[f][k] = gn_bn
			else:
				listledger[f][k] = q.Opening_Balance
			k=k+1
		f=f+1
	return listledger



def list_journal(listjour):
	listjournal= [['','','','',''] for x in range(listjour.count())]
	c=0 
	for i in listjour:
		d=0
		while d<5:
			if (d==0):
				listjournal[c][d] =i.Date
			elif(d==1):
				listjournal[c][d] =i.To
			elif(d==2):
				listjournal[c][d] =i.By
			elif(d==3):
				listjournal[c][d] =i.Debit
			else:
				listjournal[c][d] =i.Credit
			d=d+1
		c=c+1
	return listjournal

# logic = select journal ledgername wise, filter all transactions in 
# which the ledger name exists in by side, thier 'To' sides total
def toside(ledgerlist,journallist,lname):
	for w in ledgerlist:
		sum2 =0
		for i in journallist:
			if(str(i[2]) == w[1]):
				sum2 +=i[3]
		if(str(w[1])==str(lname)):
			return(sum2)



def byside(ledgerlist,journallist,lname):
	for w in ledgerlist:
		sum1 =0
		for i in journallist:
			if(str(i[1]) == w[1]):
				sum1 +=i[4]
		if(str(w[1])==str(lname)):
			return(sum1)


def total_balance(ledgerlist,journallist,ledgername):
	sumby = 0
	sumby+=byside(ledgerlist,journallist,ledgername)
	return sumby

def total_balance_credit(ledgerlist,journallist,ledgername):
	sumto = 0
	sumto+=toside(ledgerlist,journallist,ledgername)
	return sumto


lspre = ledger1.objects.all()
ls = list_ledger(lspre)

jpre = journal.objects.all()
j = list_journal(jpre)


@receiver(pre_save, sender=ledger1)
def update_total_debit(sender,instance,*args,**kwargs):
	Total_Debit = total_balance(ls,j,lspre[1].name)
	instance.Total_Debit = Total_Debit


@receiver(pre_save, sender=ledger1)
def update_total_credit(sender,instance,*args,**kwargs):
	Ctotal = total_balance_credit(ls,j,lspre[1].name)
	instance.Ctotal = Ctotal


@receiver(pre_save, sender=ledger1)
def update_closing_balance(sender,instance,*args,**kwargs):
	Closing_balance = instance.Total_Debit + instance.Opening_Balance - instance.Ctotal
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










		




	














