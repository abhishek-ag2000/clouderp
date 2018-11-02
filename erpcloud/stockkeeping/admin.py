from django.contrib import admin
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase,Stock_Total,Sales

# Register your models here.


class Stockgroupadmin(admin.ModelAdmin):
	model = Stockgroup
	list_display = ['User', 'Company','name','under','quantities']
	search_fields = ['name']

class Simpleunitsadmin(admin.ModelAdmin):
	model = Simpleunits
	list_display = ['User', 'Company','symbol','formal']
	search_fields = ['symbol','formal']

class Compoundunitsadmin(admin.ModelAdmin):
	model = Compoundunits
	list_display = ['User', 'Company','firstunit','conversion','secondunit']
	search_fields = ['firstunit','secondunit']

class Stockdataadmin(admin.ModelAdmin):
	model = Stockdata
	list_display = ['User', 'Company','stock_name','gst_rate','hsn']
	search_fields = ['stock_name','hsn']

class Stock_Totaladmin(admin.ModelAdmin):
	model = Stock_Total
	list_display = ['purchases','stockitem','Quantity','rate','Total']
	search_fields = ['stockitem']

class Stock_Totalinline(admin.TabularInline):
	model = Stock_Total

class Purchaseadmin(admin.ModelAdmin):
	model = Purchase
	list_display = ['User', 'Company','ref_no','Party_ac','purchase','Total_Amount']
	search_fields = ['stock_name','hsn']
	inlines = [Stock_Totalinline]

class Salesadmin(admin.ModelAdmin):
	model = Sales
	list_display = ['User', 'Company','ref_no','Party_ac','sales','Total_Amount']
	search_fields = ['stock_name','hsn']
	inlines = [Stock_Totalinline]


admin.site.register(Stockgroup, Stockgroupadmin)
admin.site.register(Simpleunits, Simpleunitsadmin)
admin.site.register(Compoundunits, Compoundunitsadmin)
admin.site.register(Stockdata, Stockdataadmin)
admin.site.register(Purchase, Purchaseadmin)
admin.site.register(Sales, Salesadmin)
admin.site.register(Stock_Total, Stock_Totaladmin)