from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class categories(models.Model):
	Title = models.CharField(max_length=40, default='GST')

	def __str__(self):
		return self.Title



class Blog(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Date = models.DateTimeField(default=datetime.now)
	Blog_title = models.CharField(max_length=255)
	Description = RichTextUploadingField(blank=True, null=True,config_name='special')
	Blog_image = models.ImageField(upload_to='blog_image', null=True, blank=True)
	Category = models.ForeignKey(categories,on_delete=models.CASCADE,related_name='Categories')


	def __str__(self):
		return self.Blog_title

	def get_absolute_url(self):
		return reverse("blog:blogdetail", kwargs={'pk':self.pk})

	def get_count(self):
		return self.Categories.all().count()



