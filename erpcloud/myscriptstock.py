from accounting_double_entry.models import ledger1,group1,journal,selectdatefield
from stockkeeping.models import Stockdata,Purchase,Sales
from django.forms.models import model_to_dict

from django.utils.dateformat import format
from django.utils.dates import MONTHS
from datetime import datetime, date
from django.db.models.functions import TruncMonth, Coalesce
from django.db.models import Sum
import calendar

from django.db.models import Case, When, Value, CharField


daterange = selectdatefield.objects.all()
dfp = Purchase.objects.all()
dfs = Sales.objects.all()
dfsd = Stockdata.objects.all()
sd = selectdatefield.objects.all()

#python manage.py shell < myscriptstock.py

# from datetime import datetime, timedelta
# from collections import OrderedDict

# dates = ["2014-10-10", "2016-01-07"]

# start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]

# x =OrderedDict(((start + timedelta(_)).strftime(r"%b-%y"), None) for _ in 
# range((end - start).days)).keys()

# for i in x:
# 	print(datetime(i))
# 	function(qs,stockcreationdate,i)

# #for _ in range((end - start).days):
# 	#OrderedDict((start+ timedelta(_)).strftime(r"%b-%y"), None).keys()
# 	#print(start+timedelta(_).datetime.datetime.strftime(r"%b-%y"), None)
# 	#print(type(timedelta(_)))

# #print(type(start))

# def function(qs,strtdate,enddate):
# 	qs = Stockdata.objects.filter(User=self.request.user, Company=company_details.pk, Date__gte=selectdatefield_details.Start_Date, Date__lte=enddate)
# 		total = qs.annotate(the_sum=Coalesce(Sum('salestock__Quantity'),0)).values('the_sum')
# 		total2 = qs.annotate(the_sum2=Coalesce(Sum('purchasestock__Quantity_p'),0)).values('the_sum2')
# 		qs = qs.annotate(
#     		sales_sum = Coalesce(Sum('salestock__Quantity'),0),
#     		purchase_sum = Coalesce(Sum('purchasestock__Quantity_p'),0),
#     		purchase_tot = Coalesce(Sum('purchasestock__Total_p'),0)
# 		)
# 		qs1 = qs.annotate(
#     		difference = ExpressionWrapper(F('purchase_sum') - F('sales_sum'), output_field=DecimalField()),
#     		total = ExpressionWrapper((F('purchase_tot') / F('purchase_sum')) * (F('purchase_sum') - F('sales_sum')), output_field=DecimalField())
# 		) 

# 		return total,total2,qs


# i = strtdate
# while i < end_date:
# 	qs = Stockdata.objects.filter(User=self.request.user, Company=company_details.pk, Date__lte=i)
# 	function()
# 		return pass
# 	i = i + timedelta(1 mon)

# fs = Sales.objects.annotate(month = TruncMonth('date')).values('month').annotate(sales_sum = Sum('Total_Amount'))

# print(fs.values('month','sales_sum'))


# import calender

# [calendar.month_name[month] for month in fs]


conditions = []
for i in range(1, 13):
	month_name = calendar.month_name[i]		
	conditions.append(When(date__month=i, then=Value(month_name)))
	print(month_name)

x = Purchase.objects.annotate(month_name=Case(*conditions, default=Value(""), output_field=CharField())).order_by("month_name").values_list("month_name", flat=True).distinct().annotate(sales_sum=Sum('Total_Purchase')).values_list("month_name","sales_sum")

# y = x.values('month_name','sales_sum')
# print(y)


for month_name,sales_sum in x:
	print(month_name,sales_sum)
	


y = x.aggregate(the_sum=Coalesce(Sum('sales_sum'), Value(0)))['the_sum']
print(y)

# month_name = calendar.month_name[-1]
# print(type(month_name))

# if (month_name == y["month_name"]):
# 	print(month_name)
# else:
# 	print('none')

