from django.contrib import admin
from transaction.models import ledger1,transaction,journal
# Register your models here.

admin.site.register(ledger1)
admin.site.register(transaction)
admin.site.register(journal)