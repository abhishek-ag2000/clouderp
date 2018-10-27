from django.db import models
from accounting_double_entry.models import group1,ledger1,journal
from company.models import company
from django.conf import settings
from django.core.exceptions import ValidationError
import datetime


# Create your models here.

class Stockgroup(models.Model):
	User       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company    = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	name       = models.CharField(max_length=32)
	under      = models.ForeignKey(group1,on_delete=models.CASCADE,related_name='Stock_group',blank=True,null=True)
	quantities = models.BooleanField(default=False)

	def __str__(self):
		return self.name


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
		return self.firstunit

	def clean(self):
		if self.firstunit == self.secondunit:
			raise ValidationError('First Unit Should Not Be Equal To Second Unit')


class Stockdata(models.Model):
	User        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company     = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	stock_name  = models.CharField(max_length=32)
	under       = models.ForeignKey(Stockgroup,on_delete=models.CASCADE,related_name='stocks')
	unitsimple  = models.ForeignKey(Simpleunits,on_delete=models.CASCADE,null=True,blank=True,related_name='firsts_unit')
	unitcomplex = models.ForeignKey(Compoundunits,on_delete=models.CASCADE,null=True,blank=True,related_name='seconds_unit')
	rate        = models.DecimalField(max_digits=5,decimal_places=2)
	hsn         = models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.stock_name

	def clean(self):
		if unitsimple != None and unitcomplex != None:
			raise ValidationError({'unitcomplex':["You are not supposed to select both units!"]})

class Purchase(models.Model):
	User        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Company     = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
	date        = models.DateField(default=datetime.date.today,blank=True, null=True)
	ref_no      = models.PositiveIntegerField()
	Party_ac    = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='partyledger')
	purchase    = models.ForeignKey(ledger1,on_delete=models.CASCADE,related_name='purchaseledger')
	Name        = models.ForeignKey(Stockgroup,on_delete=models.CASCADE,related_name='purchases')
	Quantity    = models.PositiveIntegerField()
	rate		= models.DecimalField(max_digits=5,decimal_places=2)

	def __str__(self):
		return self.Name





	

