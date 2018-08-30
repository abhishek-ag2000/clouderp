from django.contrib import admin
from accounting_double_entry.models import group1,ledger1,journal

# Register your models here.


class journaltransactionsdebit(admin.TabularInline):
	model = journal
	fk_name = 'By'
	exclude = ['Debit', 'Total_Debit', 'Total_Credit']
	

class journaltransactionscredit(admin.TabularInline):
	model = journal
	fk_name = 'To'
	exclude = ['Credit', 'Total_Credit', 'Total_Debit']
	



class ledgerAdmin(admin.ModelAdmin):
	model = ledger1
	inlines = [
           journaltransactionsdebit,
           journaltransactionscredit,
           ]

admin.site.register(ledger1, ledgerAdmin)
admin.site.register(group1)
admin.site.register(journal)







