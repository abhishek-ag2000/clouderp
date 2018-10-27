from django.contrib import admin
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase

# Register your models here.

admin.site.register(Stockgroup)
admin.site.register(Simpleunits)
admin.site.register(Compoundunits)
admin.site.register(Stockdata)
admin.site.register(Purchase)