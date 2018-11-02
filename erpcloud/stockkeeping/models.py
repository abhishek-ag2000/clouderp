from django.db import models
from accounting_double_entry.models import group1,ledger1,journal
from company.models import company
from django.conf import settings
from django.core.exceptions import ValidationError
import datetime
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import Value
from django.db.models import F
# Create your models here.

class Stockgroup(models.Model):
	User       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company    = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	name       = models.CharField(max_length=32)
	under      = models.ForeignKey("self",on_delete=models.CASCADE,related_name='Stock_group',null=True)
	quantities = models.BooleanField(default=False)

	def __str__(self):
		return self.name

@receiver(post_save, sender=company)
def user_created(sender, instance, created, **kwargs):
	if created:
		Stockgroup.objects.create(User=instance.User,Company=instance,name='Primary',quantities=False)


class Simpleunits(models.Model):
	User       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company    = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	symbol     = models.CharField(max_length=32)
	formal     = models.CharField(max_length=32)

	def __str__(self):
		return self.symbol

class Compoundunits(models.Model):
	User       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company    = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	firstunit  = models.ForeignKey(Simpleunits,on_delete=models.CASCADE,related_name='firsts')
	conversion = models.DecimalField(max_digits=19,decimal_places=2)
	secondunit = models.ForeignKey(Simpleunits,on_delete=models.CASCADE,related_name='seconds')

	def __str__(self):
		return str(self.firstunit) +  '  of  '  + str(self.secondunit)

	def clean(self):
		if self.firstunit == self.secondunit:
			raise ValidationError('First Unit Should Not Be Equal To Second Unit')


class Stockdata(models.Model):
	User        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company     = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	stock_name  = models.CharField(max_length=32,unique=True)
	under       = models.ForeignKey(Stockgroup,on_delete=models.CASCADE,related_name='stocks')
	unitsimple  = models.ForeignKey(Simpleunits,on_delete=models.CASCADE,null=True,blank=True,related_name='firsts_unit')
	unitcomplex = models.ForeignKey(Compoundunits,on_delete=models.CASCADE,null=True,blank=True,related_name='seconds_unit')
	gst_rate    = models.DecimalField(max_digits=4,decimal_places=2,default=5)
	hsn         = models.PositiveIntegerField()

	def __str__(self):
		return self.stock_name

	def clean(self):
		if self.unitsimple != None and self.unitcomplex != None:
			raise ValidationError({'unitcomplex':["You are not supposed to select both units!"],'unitsimple':["You are not supposed to select both units!"]})


class Purchase(models.Model):
	User         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company      = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	date         = models.DateField(default=datetime.date.today,blank=True, null=True)
	Address		 = models.CharField(max_length=32,blank=True)
	GSTIN        = models.CharField(max_length=32,blank=True)
	PAN          = models.CharField(max_length=32,blank=True)
	State_Name 	 = (
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
	State 		 = models.CharField(max_length=100,choices=State_Name,default='Choose')
	Contact      = models.BigIntegerField(blank=True,null=True)
	DeliveryNote = models.CharField(max_length=32,blank=True)
	Supplierref  = models.CharField(max_length=32,blank=True)
	Mode         = models.CharField(max_length=32,blank=True)
	ref_no       = models.PositiveIntegerField()
	Party_ac     = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='partyledger')
	purchase     = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='purchaseledger')
	Total_Amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)

	def __str__(self):
		return str(self.Party_ac)


class Sales(models.Model):
	User         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company      = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	date         = models.DateField(default=datetime.date.today,blank=True, null=True)
	Address		 = models.CharField(max_length=32,blank=True)
	GSTIN        = models.CharField(max_length=32,blank=True)
	PAN          = models.CharField(max_length=32,blank=True)
	State_Name 	 = (
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
	State 		 = models.CharField(max_length=100,choices=State_Name,default='Choose')
	Contact      = models.BigIntegerField(blank=True,null=True)
	DeliveryNote = models.CharField(max_length=32,blank=True)
	Supplierref  = models.CharField(max_length=32,blank=True)
	Mode         = models.CharField(max_length=32,blank=True)
	ref_no       = models.PositiveIntegerField()
	sales        = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='salesledger')
	Party_ac     = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='partyledgersales')
	Total_Amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)

	def __str__(self):
		return str(self.Party_ac)



class Stock_Total(models.Model):
	purchases   = models.ForeignKey(Purchase,on_delete=models.CASCADE,null=True,blank=True,related_name='purchasetotal')
	sales       = models.ForeignKey(Sales,on_delete=models.CASCADE,null=True,blank=True,related_name='salestotal')
	stockitem   = models.ForeignKey(Stockdata,on_delete=models.CASCADE,null=True,blank=True,related_name='purchasestock') 
	Quantity    = models.PositiveIntegerField()
	rate		= models.DecimalField(max_digits=10,decimal_places=2)
	Disc    	= models.DecimalField(max_digits=10,decimal_places=2,default=0)
	gst_rate    = models.DecimalField(max_digits=4,decimal_places=2,default=5)
	Total 		= models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	Total_sales = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def __str__(self):
		return str(self.purchases)

@receiver(pre_save, sender=Stock_Total)
def update_gst_rate(sender, instance, *args, **kwargs):
	instance.gst_rate = instance.stockitem.gst_rate

@receiver(pre_save, sender=Stock_Total)
def update_amount(sender, instance, *args, **kwargs):
	instance.Total_sales = instance.rate * instance.Quantity * (1 - (instance.Disc/100))

@receiver(pre_save, sender=Stock_Total)
def update_amount(sender, instance, *args, **kwargs):
	instance.Total = instance.rate * instance.Quantity * (1 - (instance.Disc/100))

@receiver(pre_save, sender=Purchase)
def update_total(sender,instance,*args,**kwargs):
	total = instance.purchasetotal.aggregate(the_sum=Coalesce(Sum('Total'), Value(0)))['the_sum']
	instance.Total_Amount = total

@receiver(pre_save, sender=Sales)
def update_total(sender,instance,*args,**kwargs):
	total = instance.salestotal.aggregate(the_sum=Coalesce(Sum('Total_sales'), Value(0)))['the_sum']
	instance.Total_Amount = total



@receiver(post_save, sender=Purchase)
def create_purchase_journal(sender, instance, created, **kwargs):
	total1 = instance.purchasetotal.aggregate(the_sum=Coalesce(Sum('Total'), Value(0)))['the_sum']
	if created:
		journal.objects.create(User=instance.User,Company=instance.Company,By=instance.Party_ac,To=instance.purchase,Debit=total1,Credit=total1)
		
@receiver(post_save, sender=Sales)
def create_purchase_journal(sender, instance, created, **kwargs):
	total2 =  instance.salestotal.aggregate(the_sum=Coalesce(Sum('Total'), Value(0)))['the_sum']
	if created:
		journal.objects.create(User=instance.User,Company=instance.Company,By=instance.sales,To=instance.Party_ac,Debit=total2,Credit=total2)


	

