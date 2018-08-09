from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


class group(models.Model):

	Name = (
		('Fixed_Asset','Fixed_Asset'),
		('Current_Assets','Current_Assets'),
		('Liabilities','Liabilities'),
		('Current_Liabilities','Current_Liabilities'),
		('Capital','Capital'),
		('Loans','Loans'),
		('Income','Income'),
		('Expenses','Expenses'),
		)
	
    		
	Master = models.CharField(max_length=32,choices=Name,default='Fixed_Asset')

	Nature = (
		('Debit','Debit'),
		('Credit','Credit'),
		('Not Applicable','Not Applicable'),
		)

	balance_nature = models.CharField(max_length=32,choices=Nature,default='Debit')
	
	Group_Name = models.CharField(max_length=32,unique=True)

	def __str__(self):
		return self.Group_Name


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


@receiver(pre_save, sender=group)
def update_user_balance_nature(sender,instance,*args,**kwargs):
	balance_nature = balance_master(instance.Master)
	instance.balance_nature = balance_nature

# pre_save.connect(update_user_balance_nature, sender=group)






class ledger(models.Model):
	Creation_Date = models.DateTimeField(default=datetime.now, blank=True)
	name = models.CharField(max_length=32,unique=True)
	Group_Name = models.ForeignKey(group,on_delete=models.CASCADE)
	Opening_Balance = models.FloatField(blank=False, default=0.0)
	Closing_Balance = models.FloatField(blank=True, default=0.0)

	
	def __str__(self):
		return self.name


	
class contact(models.Model):
	Name = models.CharField(max_length=100,blank=False)
	Address_Line_1 = models.CharField(max_length=256,blank=False)
	Address_Line_2 = models.CharField(max_length=256)
	City = models.CharField(max_length=100,blank=False)
	State = models.CharField(max_length=40,blank=False)
	Phone_No = models.PositiveIntegerField(blank=False)
	Email = models.EmailField(max_length=100)


	def __str__(self):
		return self.Name


class transaction(models.Model):
	Transaction_id = models.AutoField(primary_key=True)
	Date = models.DateTimeField(default=datetime.now, blank=True)
	Memo_1 = models.CharField(max_length=256)
	Name = models.ForeignKey(contact,on_delete=models.CASCADE)
	ref = models.CharField(max_length=256,blank=True)

	
	def __str__(self):
		return str(self.Transaction_id)
		

class line_Item(models.Model):
	line_ItemID = models.AutoField(primary_key=True)
	Transaction_id = models.ForeignKey(transaction,on_delete=models.CASCADE)
	Amount = models.PositiveIntegerField(blank=False)
	Memo_2 = models.CharField(max_length=256) 

	
	def __str__(self):
 		return str(self.line_ItemID)


class account(models.Model):
	Account_ID = models.AutoField(primary_key=True)
	line_ItemID = models.ForeignKey(line_Item,on_delete=models.CASCADE)
	Account_Name = models.CharField(max_length=256,blank=False)
	Account_Type = models.CharField(max_length=256,blank=False)


	def __str__(self):
		return self.Account_Name














