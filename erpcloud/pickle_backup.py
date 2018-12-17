import pickle

# import all our apps models

from accounting_double_entry.models import ledger1,group1,journal,selectdatefield
from stockkeeping.models import Stockdata,Purchase,Sales


# make all queries .objects.all()

daterange = selectdatefield.objects.all()
dfp = Purchase.objects.all()
dfs = Sales.objects.all()
dfsd = Stockdata.objects.all()
sd = selectdatefield.objects.all()

# save dump

from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)
#data = serializers.serialize("Json", SomeModel.objects.all())

with open("file.json", "wb") as out:
    serialize('json', selectdatefield.objects.all(), cls=LazyEncoder)


#python manage.py shell < pickle_backup.py


