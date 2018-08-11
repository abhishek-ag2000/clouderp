
# Just For Testing Purpose For Journal Entry

from django.db import models
from django.db.models import Value
from datetime import datetime
from django.db.models.signals import pre_delete,pre_save
from django.dispatch import receiver
# Create your models here.


class logic(models.Model):
	Name1 = (
		('By','By'),
		('To','To'),
		('Not Applicable','Not Applicable'),
		)
	To_or_By = models.CharField(max_length=32,choices=Name1,default='By')
	Particulars = models.CharField(max_length=32)
	Debit = models.DecimalField(max_digits=10,decimal_places=2)
	Credit = models.DecimalField(max_digits=10,decimal_places=2)
	Total_Amount_Debited = models.DecimalField(max_digits=10,decimal_places=2)
	Total_Amount_Credited = models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.Particulars









# def balance_master1(master_level1):
# 	if master_level1 == 'To':
# 		bal1 = 0.00
# 	return bal1

# @receiver(pre_save, sender=logic)
# def update_user_Credit(sender,instance,*args,**kwargs):
# 	Debit = balance_master1(instance.To)
# 	instance.Debit = Debit


# def balance_master1(master_level1):
# 	if master_level1 == 'To':
# 		bal1 = 0.00
# 	return bal1
	
# @receiver(pre_save, sender=logic)
# def update_user_Debit(sender,instance,*args,**kwargs):
# 	Debit = balance_master1(instance.To_or_By)
# 	instance.Debit = Debit





