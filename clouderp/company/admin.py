from django.contrib import admin
from . import models
# Register your models here.


class companyownerInline(admin.TabularInline):
	model = models.companyowner


class companyAdmin(admin.ModelAdmin):

	search_fields = ['Name']

	list_display = ['Name', 'Company_Email', 'Mobile_No', 'Financial_Year_From']

admin.site.register(models.company,companyAdmin)
admin.site.register(models.companyowner)
