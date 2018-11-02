from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
import datetime


from django.contrib.auth import get_user_model
User = get_user_model()



class company(models.Model):
	User = models.ForeignKey(User,related_name="Company_Owner",on_delete=models.CASCADE,null=True,blank=True)
	Name = models.CharField(max_length=50,blank=False)
	types = (   ('Individual','Individual'),
				('HUF','HUF'),
				('Partnership','Partnership'),
				('Trust','Trust'),
				('Private Company','Private Company'),
				('Public Company','Public Company'),
				('LLP','LLP'),
				#('',''),
			)
	Business_nature_Service_Provider = models.BooleanField(default=False)
	Business_nature_Retail = models.BooleanField(default=False)
	Business_nature_Wholesale = models.BooleanField(default=False)
	Business_nature_Works_Contract  = models.BooleanField(default=False)
	Business_nature_Leasing = models.BooleanField(default=False)
	Business_nature_Factory_Manufacturing = models.BooleanField(default=False)
	Business_nature_Bonded_Warehouse = models.BooleanField(default=False)
	Business_nature_Other = models.BooleanField(default=False)
	Please_specify = models.BooleanField(default=False)
	Type_of_company = models.CharField(max_length=32,choices=types,default='Individual')
	Shared_Users = models.CharField(max_length=32,default="Current User only") # company data sharing
	Address = models.TextField()
	Country = models.CharField(max_length=32,default='India')
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
	Pincode = models.CharField(max_length=32)
	Telephone_No = models.BigIntegerField(blank=True,null=True)
	Mobile_No = models.BigIntegerField(blank=True,null=True)
	Financial_Year_From = models.DateField(default=datetime.date(2018,4,1), blank=False)
	Books_Begining_From = models.DateField(default=datetime.date(2018,4,1), blank=False)
	gst  = models.CharField(max_length=20)
	pan  = models.CharField(max_length=18)


	def __str__(self):
		return self.Name

	def clean(self):
		if self.Books_Begining_From < self.Financial_Year_From:
			raise ValidationError('Books Begining year cannot be less than starting of the Financial year')

	class Meta:
		ordering = ["Name"]
		



 










# def create_company(sender, **kwargs):
# 	if kwargs['created']:
# 		Company_Name = companyowner.objects.create(Company=kwargs['instance'])


# post_save.connect(create_user, sender=company)



