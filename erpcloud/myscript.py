from accounting_double_entry.models import ledger1,group1,journal,selectdatefield
from stockkeeping.models import Stockdata,Purchase,Sales
# from datetime import datetime,date

# # ledger name loop stored in a list with opening balance and its date 
# # list1 =[[name,bal_nature,creation_date,opening balance],
# #  		  [name,bal_nature,creation_date,opening balance],
# #  		[name,bal_nature,creation_date,opening balance]]

# def list_ledger(listleg):
# 	listledger = [['','','','']	for x in range(listleg.count())]
# 	f=0
# 	for q in listleg:
# 		k=0
# 		while k<4:
# 			if (k==0):
# 				listledger[f][k] = q.Creation_Date
# 			elif(k==1):
# 				listledger[f][k] = q.name
# 			elif(k==2):
# 				gn = q.group1_Name
# 				gn_bn = gn.balance_nature
# 				listledger[f][k] = gn_bn
# 			else:
# 				listledger[f][k] = q.Opening_Balance
# 			k=k+1
# 		f=f+1
# 	return listledger

# ## #JOURNAL
# # List3 =[[DATE,TO,BY,DEBIT,CREDIT],
# # 		[DATE,TO,BY,DEBIT,CREDIT]]

# def list_journal(listjour):
# 	listjournal= [['','','','',''] for x in range(listjour.count())]
# 	c=0 
# 	for i in listjour:
# 		d=0
# 		while d<5:
# 			if (d==0):
# 				listjournal[c][d] =i.Date
# 			elif(d==1):
# 				listjournal[c][d] =i.To
# 			elif(d==2):
# 				listjournal[c][d] =i.By
# 			elif(d==3):
# 				listjournal[c][d] =i.Debit
# 			else:
# 				listjournal[c][d] =i.Credit
# 			d=d+1
# 		c=c+1
# 	return listjournal

# # eg hdfc a/c 'to' side total will be all to sides where hdfc is 'by' or debited
# def toside(ledgerlist,journallist,lname):
# 	for w in ledgerlist:
# 		sum2 =0
# 		for i in journallist:
# 			if(str(i[2]) == w[1]):
# 				sum2 +=i[3]
# 		if(str(w[1])==str(lname)):
# 			return(sum2)

# # eg hdfc a/c 'by' side total will be all by sides where hdfc is 'to' or credited
# def byside(ledgerlist,journallist,lname):
# 	for w in ledgerlist:
# 		sum1 =0
# 		for i in journallist:
# 			if(str(i[1]) == w[1]):
# 				sum1 +=i[4]
# 		if(str(w[1])==str(lname)):
# 			return(sum1)


# def closing_balance(ledgerlist,journallist,ledgername,balnat):
# 		lnam = str(ledgername)
# 		gnature = str(balnat)
# 		sumto = 0
# 		sumby=0
# 		if(gnature == 'Debit'):
# 			sumto+=ledgername.Opening_Balance
# 		else:
# 			sumby+=ledgername.Opening_Balance
# 		sumto+=toside(ledgerlist,journallist,ledgername)
# 		sumby+=byside(ledgerlist,journallist,ledgername)
# 		clbal= sumto-sumby
# 		print(ledgername,"=",clbal)

# #return [name , date , balance]

# def total_balance(ledgerlist,journallist,ledgername,balnat):
# 		lnam = str(ledgername)
# 		gnature = str(balnat)
# 		sumto = 0
# 		sumby=0
# 		if(gnature == 'Debit'):
# 			sumto+=ledgername.Opening_Balance
# 		else:
# 			sumby+=ledgername.Opening_Balance
# 		sumto+=toside(ledgerlist,journallist,ledgername)
# 		sumby+=byside(ledgerlist,journallist,ledgername)
# 		print(ledgername,"=",sumto)


# def ledgernames(ledgerlist):
# 	for i in ledgerlist:
# 		return i.name

# def ledger_balnature(ledgerlist):
# 	for u in ledgerlist:
# 		return u.group1_Name.balance_nature

# # journal List i =[[DATE,TO,BY,DEBIT,CREDIT],]
# #  ledgerlist1 w =[[name,,bal_nature,creation_date,opening balance],]

# lspre = ledger1.objects.all()
# ls = list_ledger(lspre)

# jpre = journal.objects.all()
# j = list_journal(jpre)

# #print(lspre[1].group1_Name.balance_nature)
# #print(sum +lspre[0].Opening_Balance)
# # x = toside(ls,j,'Hdfc A/c')
# # print(type(str(lspre[0])))

# # HDFC A/c
# closing_balance(ls,j,ledgernames(ls),ledger_balnature(ls))
# total_balance(ls,j,ledgernames(ls),ledger_balnature(ls))

#ba = ledger1.objects.filter(group1_Name__balance_nature='Debit').values_list('name','balance_nature')

	# c = group1.objects.count()
	# q=0
	# while q <= c:
	# 	a = group1.objects.all().filter(balance_nature = "Credit")[q]	
	# 	b = a.ledger1_set.all().values_list('name')
	# 	print(str(a) + "---"+ str(b))
	# 	q+=1

	# if(ledgername.groupname.balancenature == 'debit'): 
	# 	if (openingbalance >=0):
	# 		#opening balance in debit side
	# 	else:
	# 		#opening balance in credit side
	# 	if (closingbalance >=0):
	# 		#closing balance in credit side
	# 	else:
	# 		#closing balance in debit side
	# else:# credit
	# 	if (openingbalance >=0):
	# 		#opening balance in credit side
	# 	else:
	# 		#opening balance in debit side
	# 	if (closingbalance >=0):
	# 		#closing balance in debit side
	# 	else:
	# 		#closing balance in credit side

	# # totals
	# if(ledgername.groupname.balancenature == 'debit'): 
	# 	if (openingbalance >=0):
			 
	# 		if(closingbalance >=0):
	# 			total1 = opening balance + debitside 
	# 			total2 = closingbalance + creditside 
	# 		else:
	# 			total1 = opening balance + debitside + closing_balance
	# 			total2 = creditside
	# 	else:# opening blanace negative
	# 		if(closingbalance >=0):
	# 			total1 = debitside
	# 			total2 = opening balance + creditside + closing_balance 
	# 		else:
	# 			total1 = opening balance + creditside 
	# 			total2 = closing balance + debitside 
	# else:
	# 	if (openingbalance >=0):
			 
	# 		if(closingbalance >=0):
	# 			total1 = opening balance + creditside 
	# 			total2 = closingbalance + debitside 
	# 		else:
	# 			total1 = opening balance + creditside + closing_balance
	# 			total2 = debitside
	# 	else:# opening blanace negative
	# 		if(closingbalance >=0):
	# 			total1 = creditside
	# 			total2 = opening balance + debitside + closing_balance 
	# 		else:
	# 			total1 = opening balance + debitside 
	# 			total2 = closing balance + creditside

# python manage.py shell < myscript.py

# dt1_range = datetime.strptime(dt1,'%Y-%m-%d')
# dt2_range = datetime.strptime(dt2,'%Y-%m-%d')

#for j in pd.date_range(start=dt1, end=dt2, freq='D'):
#		print(pd.to_date(j))

#print(dt1 , dt2)
from datetime import datetime, date
import pandas as pd

daterange = selectdatefield.objects.all()
#print(daterange[1].Start_Date)
#print(daterange[1].End_Date)
i=0
while i < len(daterange):
	dt1 =str(daterange[i].Start_Date)
	dt2 =str(daterange[i].End_Date)
	print('User :',i)
	df = pd.date_range(start=dt1, end=dt2, freq='D')
	#print(df)
	for j in df:
		pass
		#print(j)
	i+=1

dfp = pd.DataFrame(list(Purchase.objects.all()))
dfs = pd.DataFrame(list(Sales.objects.all()))
dfsd = pd.DataFrame(list(Stockdata.objects.all()))
sd = pd.DataFrame(list(selectdatefield.objects.all()))

print(len(dfp))
i=0
while i < len(dfp):
	print('Purchases')
	print(dfp[0][i].User,' ',dfp[0][i].Company,' ',dfp[0][i].date,' ',dfp[0][i].Party_ac,' ',dfp[0][i].purchase,' ',dfp[0][i].Total_Purchase)
	i+=1

i=0
while i < len(dfs):
	print('Sales')
	print(dfs[0][i].User,' ',dfs[0][i].Company,' ',dfs[0][i].date,' ',dfs[0][i].Party_ac,' ',dfs[0][i].sales,' ',dfs[0][i].Total_Amount)
	i+=1

i=0
while i < len(dfsd):
	print('stockdata')
	print(dfsd[0][i].User,' ',dfsd[0][i].Company,' ',dfsd[0][i].Date,' ',dfsd[0][i].stock_name,' ',dfsd[0][i].qty_sale,' ',dfsd[0][i].qty_purchas)
	i+=1

i=0
while i < len(sd):
	print('datefield')
	print(sd[0][i].User,' ',sd[0][i].Start_Date,' ',sd[0][i].End_Date)
	i+=1


dfp = pd.DataFrame(list(Purchase.objects.all()))
dfs = pd.DataFrame(list(Sales.objects.all()))
dfsd = pd.DataFrame(list(Stockdata.objects.all()))
sd = pd.DataFrame(list(selectdatefield.objects.all()))

# calculation of stock from starting date of company to start date of date range
# -> opening stock, rate , value of each item

# calculation of stock within the date range

i=0
while i < len(sd):
	dt1 =sd[0][i].Start_Date
	dt2 =sd[0][i].End_Date
	print('User :',i)
	i=0
	x={}
	while i < len(dfsd):
		x[dfsd[0][i].stock_name]=[0,0,0] # appending in qty, rate, value
		# or opening balance from above 
		i=0
		while i < len(dfp):
			if loop.date == purchase.date:
				if (x[dfsd[0][i].stock_name][1] != 0):
					x[dfsd[0][i].stock_name][1] = (x[dfsd[0][i].stock_name][1] + (purchase value /(purchase qty*purchase rate)))/2
				else:
					x[dfsd[0][i].stock_name][1] =purchase value /(purchase qty*purchase rate)

				x[dfsd[0][i].stock_name][2] = x[dfsd[0][i].stock_name][2] + purchase 
			i+=1
		i=0
		while i < len(dfs):	
			value = value - (sales.qty * x[dfsd[0][i].stock_name][1]) # error if no purchases or stock balance till date
			i+=1
		i+=1
	i+=1

