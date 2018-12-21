from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Count,F
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from sorl.thumbnail import ImageField, get_thumbnail
# Create your models here.



class categories(models.Model):
	Title = models.CharField(max_length=40, default='GST')

	
	def __str__(self):
		return self.Title



class Blog(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	Date = models.DateTimeField(default=datetime.now)
	Blog_title = models.CharField(max_length=255,unique=True)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='likes',blank=True)
	Description = RichTextUploadingField(blank=True, null=True,config_name='special')
	Blog_image = ImageField(upload_to='blog_image', null=True, blank=True)
	Category = models.ForeignKey(categories,on_delete=models.CASCADE,related_name='blogs')
	blog_views = models.IntegerField(default=0)

	def __str__(self):
		return self.Blog_title

	def get_absolute_url(self):
		return reverse("blog:blogdetail", kwargs={'pk':self.pk})

	def total_likes(self):
		return self.likes.count()

	@classmethod
	def categories_count(cls):
		categories_count = categories.objects.annotate(blog_count=Count('blogs')).values_list('Title','blog_count')
		return categories_count


	def save(self, *args, **kwargs):
		imageTemproary = Image.open(self.Blog_image)
		outputIoStream = BytesIO()
		imageTemproaryResized = imageTemproary.resize( (900,300) ) 
		imageTemproaryResized.save(outputIoStream , format='JPEG', quality=150)
		outputIoStream.seek(0)
		self.Blog_image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.Blog_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
		super(Blog, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-id']



