from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse


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
		return reverse("double_entry:groupdetail", kwargs={'pk':self.pk})


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
	

# def balance_master1(master2_level):
# 	if master2_level == "Assets":
# 		bal_nat1 = "Debit"
# 	elif master2_level == "Expenses":
# 		bal_nat1 = "Debit"
# 	elif master2_level == "Income":
# 		bal_nat1 = "Credit"
# 	elif master2_level == "Liabilities":
# 		bal_nat1 = "Credit"
# 	else:
#  		bal_nat1 = 'Not Applicable'
# 	return bal_nat1


@receiver(pre_save, sender=group1)
def update_user_balance_nature(sender,instance,*args,**kwargs):
	balance_nature = balance_master(instance.Master)
	# balance_nature = balance_master1(instance.Nature_of_group1)
	instance.balance_nature = balance_nature

# pre_save.connect(update_user_balance_nature, sender=group1)




# def balance_master1(master2_level):
# 	if master2_level == "Assets":
# 		bal_nat1 = "Debit"
# 	elif master2_level == "Expenses":
# 		bal_nat1 = "Debit"
# 	elif master2_level == "Income":
# 		bal_nat1 = "Credit"
# 	elif master2_level == "Liabilities":
# 		bal_nat1 = "Credit"
# 	else:
# 		bal_nat1 = 'Not Applicable'
# 	return bal_nat1

# @receiver(pre_save, sender=group1)
# def update_user_balance_nature1(sender,instance,*args,**kwargs):
# 	balance_nature = balance_master1(instance.Nature_of_group1)
# 	instance.balance_nature = balance_nature




		





	














