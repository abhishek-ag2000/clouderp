from django.contrib import admin
from Double_entryy.models import (group,ledger,
								contact,transaction,
								line_Item,account)




admin.site.register(group)
admin.site.register(ledger)
admin.site.register(contact)
admin.site.register(transaction)
admin.site.register(line_Item)
admin.site.register(account)

