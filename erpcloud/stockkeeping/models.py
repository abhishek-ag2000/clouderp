from django.db import models
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from company.models import company
from django.conf import settings
from django.core.exceptions import ValidationError
import datetime
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.db.models.functions import Coalesce
from django.db.models import Value
from django.db.models import F
from sorl.thumbnail import ImageField, get_thumbnail
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
	Date 		= models.DateField(default=datetime.date.today,blank=False, null=True)
	daterange	= models.ForeignKey(selectdatefield,on_delete=models.CASCADE,null=True,blank=True,related_name='stockrange')
	stock_name  = models.CharField(max_length=32,unique=True)
	batch_no	= models.PositiveIntegerField(blank=True, null=True)
	bar_code 	= ImageField(upload_to='stockmanagement', null=True, blank=True)
	mnf_date	= models.DateField(blank=True, null=True)
	exp_date	= models.DateField(blank=True, null=True)
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

	def save(self, *args, **kwargs):
		if self.bar_code:
			self.bar_code = get_thumbnail(self.bar_code, '128x128', quality=150, format='JPEG').url
		super(Stockdata, self).save(*args, **kwargs)


class Purchase(models.Model):
	User         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company      = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	date         = models.DateField(default=datetime.date.today,blank=False, null=True)
	ref_no       = models.PositiveIntegerField()
	Party_ac     = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='partyledger')
	purchase     = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='purchaseledger')
	billname     = models.CharField(max_length=32,default='Supplier')
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
	Total_Purchase = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)

	def __str__(self):
		return str(self.Party_ac)

@receiver(post_save, sender=Purchase)
def create_purchase_journal(sender, instance, created, **kwargs):
	if created:
		journal.objects.create(User=instance.User,Company=instance.Company,By=instance.Party_ac,To=instance.purchase,Debit=instance.Total_Purchase,Credit=instance.Total_Purchase)


class Sales(models.Model):
	User         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company      = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	ref_no       = models.PositiveIntegerField()
	Party_ac     = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='partyledgersales')
	sales        = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='saleledger')
	billname     = models.CharField(max_length=32,default='Customer')
	date         = models.DateField(default=datetime.date.today,blank=False, null=True)
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
	Total_Amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)

	def __str__(self):
		return str(self.Party_ac)


class Stock_Total(models.Model):
	purchases   = models.ForeignKey(Purchase,on_delete=models.CASCADE,null=True,blank=False,related_name='purchasetotal') 
	stockitem   = models.ForeignKey(Stockdata,on_delete=models.CASCADE,null=True,blank=True,related_name='purchasestock') 
	Quantity_p  = models.PositiveIntegerField()
	rate_p		= models.DecimalField(max_digits=10,decimal_places=2)
	Disc_p    	= models.DecimalField(max_digits=10,decimal_places=2,default=0)
	gst_rate_p  = models.DecimalField(max_digits=4,decimal_places=2,default=5)
	Total_p     = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def __str__(self):
		return str(self.purchases)


class Stock_Total_sales(models.Model):
	sales       = models.ForeignKey(Sales,on_delete=models.CASCADE,null=True,blank=False,related_name='saletotal')
	stockitem   = models.ForeignKey(Stockdata,on_delete=models.CASCADE,null=True,blank=True,related_name='salestock') 
	Quantity    = models.PositiveIntegerField()
	rate		= models.DecimalField(max_digits=10,decimal_places=2)
	Disc    	= models.DecimalField(max_digits=10,decimal_places=2,default=0)
	gst_rate    = models.DecimalField(max_digits=4,decimal_places=2,default=5)
	Total 		= models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

	def __str__(self):
		return str(self.sales)

@receiver(pre_save, sender=Stock_Total)
def update_gst_rate_purchase(sender, instance, *args, **kwargs):
	instance.gst_rate_p = instance.stockitem.gst_rate

@receiver(pre_save, sender=Stock_Total)
def update_amount_purchase(sender, instance, *args, **kwargs):
	instance.Total_p = instance.rate_p * instance.Quantity_p * (1 - (instance.Disc_p/100))

@receiver(pre_save, sender=Stock_Total_sales)
def update_gst_rate(sender, instance, *args, **kwargs):
	instance.gst_rate = instance.stockitem.gst_rate

@receiver(pre_save, sender=Stock_Total_sales)
def update_amount(sender, instance, *args, **kwargs):
	instance.Total = instance.rate * instance.Quantity * (1 - (instance.Disc/100))
	
	
@receiver(pre_save, sender=Purchase)
def update_total(sender,instance,*args,**kwargs):
	total = instance.purchasetotal.aggregate(the_sum=Coalesce(Sum('Total_p'), Value(0)))['the_sum']
	instance.Total_Purchase = total

@receiver(pre_save, sender=Sales)
def update_total_sales(sender,instance,*args,**kwargs):
	total1 = instance.saletotal.aggregate(the_sum=Coalesce(Sum('Total'), Value(0)))['the_sum']
	instance.Total_Amount = total1

@receiver(post_save, sender=Stock_Total)
def trigger_pre_save_purchase(sender, instance, *args, **kwargs):
	instance.purchases.save()

@receiver(post_save, sender=Stock_Total_sales)
def trigger_pre_save_sale(sender, instance, *args, **kwargs):
	instance.sales.save()


@receiver(post_delete, sender=Stock_Total_sales)
def trigger_post_save_sale(sender, instance, *args, **kwargs):
	instance.sales.save()

# for stock calculations in stock summary

	
	# FIFO - first in first out
	#totalpur = 0 # till starting date
	#totalpurquan = 0 # till starting date
	#avgrate1 = 0 # purchaserate startdate
	#avgquant = 0 # quantity till startdate

	# for date in daterange(strtdate to enddate):
		#for purc in purchaseinvoices
			#if date == purc.date:
				#totalpur+= purch.total
				#totalpurquan+=purch.quant
				
				#avgrate = (purch.rate*purch.quant + avgrate*avgquant)/(purch.quant+avgquant)
				#avgquant+=purch.quant

		#for sale in saleinvoices
			#if date == salei.date:
			 	#totalpur-= purch.total - Sale.quant*avgrate
				#totalpurquan-=sale.qty
				
				#avgrate = (avgrate*sale.quant + avgrate*avgquant)/(sale.quant+avgquant)
				#avgquant-=sale.qty

		# test results:
		# total qty == avgquant
		# avgrate
		# totalpur == (avg rate * avgquantity or totalpurquan)





	

