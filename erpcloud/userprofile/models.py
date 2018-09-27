from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.

class Profile(models.Model):
	Date = models.DateTimeField(auto_now_add=True)
	Full_Name = models.CharField(max_length=32,blank=True)
	Name = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	E_mail = models.EmailField(max_length=70,blank=True)
	Qualification = models.CharField(max_length=32,blank=True)
	Permanant_Address = models.TextField(blank=True)
	District = models.CharField(max_length=32,blank=True)
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
	
    		
	State = models.CharField(max_length=100,choices=State_Name,default='Choose',blank=True)
	Country = models.CharField(max_length=32,blank=True)
	Phone_no = models.BigIntegerField(null=True,blank=True)
	Skills = models.TextField(blank=True)
	image = models.ImageField(upload_to='user_images', null=True, blank=True)

	def __str__(self):
		return str(self.Name)


	def get_absolute_url(self):
		return reverse("userprofile:profiledetail")

	def save(self, *args, **kwargs):
		imageTemproary = Image.open(self.image)
		outputIoStream = BytesIO()
		imageTemproaryResized = imageTemproary.resize( (128,128) ) 
		imageTemproaryResized.save(outputIoStream , format='JPEG', quality=150)
		outputIoStream.seek(0)
		self.image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
		super(Profile, self).save(*args, **kwargs)


	

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_created(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(Name=instance)