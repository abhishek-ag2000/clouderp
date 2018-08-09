from django.db import models

# Create your models here.

from datetime import datetime
from django.urls import reverse

# Create your models here.
from double_entry.models import group1

class ledger1(models.Model):
	Creation_Date = models.DateTimeField(default=datetime.now, blank=True)
	name = models.CharField(max_length=32,unique=True)
	group1_Name = models.ForeignKey(group1,on_delete=models.CASCADE)
	Opening_Balance = models.DecimalField(max_digits=19,decimal_places=4)
	Inventory_Values_are_affected = models.BooleanField(default=False)
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
		return reverse("ledger:ledgerdetail", kwargs={'pk':self.pk})



class transaction(models.Model):
	Creation_Date = models.DateTimeField(default=datetime.now, blank=True)
	By1 = models.ForeignKey(ledger1,on_delete=models.CASCADE)
	Debit = models.DecimalField(max_digits=10,decimal_places=2)
	Total_Amount_Debited = models.DecimalField(max_digits=10,decimal_places=2)
	


	def __str__(self):
		return self.By



class journal(models.Model):
	Creation_Date = models.DateTimeField(default=datetime.now, blank=True)
	To1 = models.ForeignKey(ledger1,on_delete=models.CASCADE)
	Credit = models.DecimalField(max_digits=10,decimal_places=2)
	Total_Amount_Credited = models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.To

