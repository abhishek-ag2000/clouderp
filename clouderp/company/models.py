from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save


from django.contrib.auth import get_user_model
User = get_user_model()

# from django import template
# register = template.Library()


class company(models.Model):
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
	Type_of_company = models.CharField(max_length=32,choices=types,default='Individual')

	Business_nature_Service_Provider = models.BooleanField(default='False')
	Business_nature_Retail = models.BooleanField(default='False')
	Business_nature_Wholesale = models.BooleanField(default='False')
	Business_nature_Works_Contract = models.BooleanField(default='False')
	Business_nature_Leasing = models.BooleanField(default='False')
	Business_nature_Factory_Manufacturing = models.BooleanField(default='False')
	Business_nature_Import = models.BooleanField(default='False')
	Business_nature_Bonded_Warehouse = models.BooleanField(default='False')
	Business_nature_Bonded_Warehouse = models.BooleanField(default='False')
	Business_nature_Other = models.BooleanField(default='True')
	Please_specify = models.CharField(max_length=32)

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
	Mobile_No = models.BigIntegerField()
	Financial_Year_From = models.DateTimeField(default=datetime.now, blank=False)
	Books_Begining_From = models.DateTimeField(default=datetime.now, blank=False)

	def __str__(self):
		return self.Name

	def save(self,*args,**kwargs):
		self.User_Email = User.email
		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse("company:Dashboard",kwargs={'pk':self.pk})

	class Meta:
		ordering = ["Name"]





class companyowner(models.Model):
	Company = models.ForeignKey(company,related_name="Company_Name",on_delete=models.CASCADE)
	user = models.ForeignKey(User,related_name="Company_Owner",on_delete=models.CASCADE)


	def __str__(self):
		return self.user.username

	class Meta:
		unique_together = ['Company', 'user']





# def create_company(sender, **kwargs):
# 	if kwargs['created']:
# 		Company_Name = companyowner.objects.create(Company=kwargs['instance'])


# post_save.connect(create_user, sender=company)



