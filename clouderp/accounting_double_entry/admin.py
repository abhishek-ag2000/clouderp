from django.contrib import admin
from accounting_double_entry.models import group1,ledger1,journal
from accounting_double_entry.forms import journalForm
# Register your models here.


class journaltransactionsdebit(admin.TabularInline):
	model = journal
	form = journalForm
	fk_name = 'By'
	exclude = ['Credit']

class journaltransactionscredit(admin.TabularInline):
	model = journal
	form = journalForm
	fk_name = 'To'
	exclude = ['Debit']
	



class ledgerAdmin(admin.ModelAdmin):
	model = ledger1
	inlines = [
           journaltransactionsdebit,
           journaltransactionscredit,
           ]

admin.site.register(ledger1, ledgerAdmin)
admin.site.register(group1)
admin.site.register(journal)







