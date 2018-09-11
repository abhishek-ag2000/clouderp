from django.contrib import admin
from accounting_double_entry.models import group1,ledger1,journal

# Register your models here.

class group1admin(admin.ModelAdmin):
	model = group1
	list_display = ['group_Name', 'Master','balance_nature']
	search_fields = ['group_Name']
	readonly_fields = ('User',)



class journaladmin(admin.ModelAdmin):
	model = journal
	list_display = ['By', 'To','Debit','Credit']
	search_fields = ['By','To']
	readonly_fields = ('User',)



class journaltransactionsdebit(admin.TabularInline):
	model = journal
	fk_name = 'By'
	exclude = ['Credit', 'Total_Debit', 'Total_Credit']
	

class journaltransactionscredit(admin.TabularInline):
	model = journal
	fk_name = 'To'
	exclude = ['Debit', 'Total_Credit', 'Total_Debit']
	



class ledgerAdmin(admin.ModelAdmin):
	model = ledger1
	ledger1_display = ['Creation_Date', 'name','Opening_Balance']
	search_fields = ['name']
	readonly_fields = ('User',)
	inlines = [
           journaltransactionsdebit,
           journaltransactionscredit,
           ]

	

admin.site.register(ledger1,ledgerAdmin)
admin.site.register(group1,group1admin)
admin.site.register(journal,journaladmin)







