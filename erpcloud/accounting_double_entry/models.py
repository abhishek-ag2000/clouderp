from django.conf import settings
from django.db import models
import datetime
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models import Sum
from company.models import company
from django.shortcuts import get_object_or_404
from django.utils import timezone


class selectdatefield(models.Model):
	User       = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="Users",on_delete=models.CASCADE,null=True,blank=True)
	Start_Date = models.DateField(default=datetime.date(2018,4,1),blank=True, null=True)
	End_Date   = models.DateField(default=datetime.date(2019,3,31),blank=True, null=True)

	def __str__(self):
		return str(self.Start_Date)

	def clean(self):
		if self.Start_Date > self.End_Date:
			raise ValidationError({'Start_Date':["Start Date Cannot Be Greater Than End Date"],'End_Date':["Start Date Cannot Be Greater Than End Date"]})


class group1(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	group_Name = models.CharField(max_length=32)
	Company = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True,related_name='Company_group')  		
	Master = models.ForeignKey("self",on_delete=models.CASCADE,related_name='master_group',null=True)

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

	balance_nature = models.CharField(max_length=32,choices=Nature,default='Debit',blank=False)
	Group_behaves_like_a_Sub_Group = models.BooleanField(default=False)
	Nett_Debit_or_Credit_Balances_for_Reporting = models.BooleanField(default=False)
	
	

	def __str__(self):
		return self.group_Name


	def get_absolute_url(self, **kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		return reverse("accounting_double_entry:groupdetail", kwargs={'pk2':self.pk, 'pk1':company_details.pk})

@receiver(post_save, sender=company)
def create_default_groups1(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Primary',Nature_of_group1='Not Applicable',balance_nature='Not Applicable',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups2(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Branch/Divisions',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Liabilities',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups3(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Capital A/c',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Liabilities',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups4(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Current Assets',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Assets',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups5(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Current Liabilities',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Liabilities',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups6(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Direct Expenses',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Expenses',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups7(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Direct Incomes',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Income',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups8(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Fixed Assets',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Assets',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups9(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Indirect Income',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Income',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=True)

@receiver(post_save, sender=company)
def create_default_groups10(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Indirect Expense',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Expenses',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=True)


@receiver(post_save, sender=company)
def create_default_groups11(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Investments',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Assets',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups12(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Loans (Liability)',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Liabilities',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups13(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Misc Expenses (ASSET)',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Assets',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups14(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Purchase Accounts',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Expenses',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups15(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Sales Account',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Income',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups16(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Suspense A/c',Master=instance.Company_group.get(group_Name='Primary'),Nature_of_group1='Liabilities',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups17(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Bank Accounts',Master=instance.Company_group.get(group_Name='Current Assets'),Nature_of_group1='Not Applicable',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups18(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Bank OD A/c',Master=instance.Company_group.get(group_Name='Loans (Liability)'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups19(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Cash-in-hand',Master=instance.Company_group.get(group_Name='Current Assets'),Nature_of_group1='Not Applicable',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False),

@receiver(post_save, sender=company)
def create_default_groups20(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Deposits(Asset)',Master=instance.Company_group.get(group_Name='Current Assets'),Nature_of_group1='Not Applicable',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False),

@receiver(post_save, sender=company)
def create_default_groups21(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Duties & Taxes',Master=instance.Company_group.get(group_Name='Current Liabilities'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False),

@receiver(post_save, sender=company)
def create_default_groups22(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Loans & Advances(Asset)',Master=instance.Company_group.get(group_Name='Current Assets'),Nature_of_group1='Not Applicable',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups23(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Provisions',Master=instance.Company_group.get(group_Name='Current Liabilities'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups24(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Reserves & Surplus',Master=instance.Company_group.get(group_Name='Capital A/c'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups25(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Secured Loans',Master=instance.Company_group.get(group_Name='Loans (Liability)'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups26(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Stock-in-hand',Master=instance.Company_group.get(group_Name='Current Assets'),Nature_of_group1='Not Applicable',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)

@receiver(post_save, sender=company)
def create_default_groups27(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Sundry Creditors',Master=instance.Company_group.get(group_Name='Current Liabilities'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups28(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Sundry Debtors',Master=instance.Company_group.get(group_Name='Current Assets'),Nature_of_group1='Not Applicable',balance_nature='Debit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


@receiver(post_save, sender=company)
def create_default_groups30(sender, instance, created, **kwargs):
	if created:
		group1.objects.create(User=instance.User,Company=instance,group_Name='Unsecured Loans',Master=instance.Company_group.get(group_Name='Loans (Liability)'),Nature_of_group1='Not Applicable',balance_nature='Credit',Group_behaves_like_a_Sub_Group=False,Nett_Debit_or_Credit_Balances_for_Reporting=False)


# def balance_master(master_level):
# 	if master_level == "Fixed Assets":
# 		bal_nat = "Debit"
# 	elif master_level == "Current Assets":
# 		bal_nat = "Debit"
# 	elif master_level == "Current Liabilities":
# 		bal_nat = "Credit"
# 	elif master_level == "Capital A/c":
# 		bal_nat = "Credit"
# 	elif master_level == "Loans (Liability)":
# 		bal_nat = "Credit"
# 	elif master_level == "Direct Incomes":
# 		bal_nat = "Credit"
# 	elif master_level == "Indirect Incomes":
# 		bal_nat = "Credit"
# 	elif master_level == "Indirect Expenses":
# 		bal_nat = "Debit"
# 	elif master_level == "Direct Expenses":
# 		bal_nat = "Debit"
# 	else:
# 		bal_nat = "Not Applicable"
# 	return bal_nat
	

# @receiver(pre_save, sender=group1)
# def update_user_balance_nature(sender,instance,*args,**kwargs):
# 	balance_nature = balance_master(instance.Master)
# 	instance.balance_nature = balance_nature



class ledger1(models.Model):
	User 			= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company 		= models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True,related_name='Companys')
	Creation_Date	= models.DateField(default=datetime.date.today,blank=True, null=True)
	name 			= models.CharField(max_length=32)
	group1_Name 	= models.ForeignKey(group1,on_delete=models.CASCADE,null=True,related_name='ledgergroups')
	Opening_Balance = models.DecimalField(default=0.00,max_digits=19,decimal_places=2,null=True)
	Balance_opening = models.DecimalField(default=0.00,max_digits=19,decimal_places=2,null=True)
	User_Name 		= models.CharField(max_length=100,blank=True)
	Address 		= models.TextField(blank=True)
	State_Name 		= (
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
	State 			= models.CharField(max_length=100,choices=State_Name,default='Choose',blank=True)
	Pin_Code 		= models.BigIntegerField(blank=True,null=True)
	PanIt_No 		= models.CharField(max_length=100,blank=True)
	GST_No 			= models.CharField(max_length=100,blank=True)
	Closing_balance = models.DecimalField(default=0.00,max_digits=10,decimal_places=2,blank=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self, **kwargs):
		company_details = get_object_or_404(company, pk=kwargs['pk'])
		return reverse("accounting_double_entry:ledgerdetail", kwargs={'pk2':self.pk, 'pk1':company_details.pk})

		
@receiver(post_save, sender=company)
def create_default_ledger(sender, instance, created, **kwargs):
	if created:
		ledger1.objects.bulk_create([
			ledger1(User=instance.User,Company=instance,Creation_Date=instance.Books_Begining_From,group1_Name=instance.Company_group.get(group_Name='Primary'),name='Cash',Opening_Balance=0),
			ledger1(User=instance.User,Company=instance,Creation_Date=instance.Books_Begining_From,group1_Name=instance.Company_group.get(group_Name='Primary'),name='Profit & Loss A/c',Opening_Balance=0),
			])

	
		
class journal(models.Model):
	User       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company    = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True,related_name='Companyname')
	Date       = models.DateField(default=datetime.date.today)
	By         = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='Debitledgers')
	To         = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='Creditledgers')
	Debit      = models.DecimalField(max_digits=10,decimal_places=2,null=True)
	Credit     = models.DecimalField(max_digits=10,decimal_places=2,null=True)
	narration  = models.TextField(blank=True)


	def __str__(self):
		return str(self.By)

	def get_absolute_url(self):
		return reverse("accounting_double_entry:detail", kwargs={'pk':self.pk})

	def clean(self):
		if self.Debit != self.Credit:
			raise ValidationError('Debit Amount Should Be Equal To Credit Amount')
		elif self.To == self.By:
			raise ValidationError('Paricular Entry Cannot be same')


