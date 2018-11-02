from accounting_double_entry.models import ledger1,group1,journal
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

c = group1.objects.count()
q=0
while q <= c:
	a = group1.objects.all().filter(balance_nature = "Credit")[q]	
	b = a.ledger1_set.all().values_list('name')
	print(str(a) + "---"+ str(b))
	q+=1

if(ledgername.groupname.balancenature == 'debit'): 
	if (openingbalance >=0):
		#opening balance in debit side
	else:
		#opening balance in credit side
	if (closingbalance >=0):
		#closing balance in credit side
	else:
		#closing balance in debit side
else:# credit
	if (openingbalance >=0):
		#opening balance in credit side
	else:
		#opening balance in debit side
	if (closingbalance >=0):
		#closing balance in debit side
	else:
		#closing balance in credit side

# totals
if(ledgername.groupname.balancenature == 'debit'): 
	if (openingbalance >=0):
		 
		if(closingbalance >=0):
			total1 = opening balance + debitside 
			total2 = closingbalance + creditside 
		else:
			total1 = opening balance + debitside + closing_balance
			total2 = creditside
	else:# opening blanace negative
		if(closingbalance >=0):
			total1 = debitside
			total2 = opening balance + creditside + closing_balance 
		else:
			total1 = opening balance + creditside 
			total2 = closing balance + debitside 
else:
	if (openingbalance >=0):
		 
		if(closingbalance >=0):
			total1 = opening balance + creditside 
			total2 = closingbalance + debitside 
		else:
			total1 = opening balance + creditside + closing_balance
			total2 = debitside
	else:# opening blanace negative
		if(closingbalance >=0):
			total1 = creditside
			total2 = opening balance + debitside + closing_balance 
		else:
			total1 = opening balance + debitside 
			total2 = closing balance + creditside

# python manage.py shell < myscript.py