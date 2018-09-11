from accounting_double_entry.models import ledger1,group1,journal
from datetime import datetime,date

# ledger name loop stored in a list with opening balance and its date 
# list1 =[[name,,bal_nature,creation_date,opening balance],
#  		  [name,bal_nature,creation_date,opening balance],
#  		[name,bal_nature,creation_date,opening balance]]

lspre = ledger1.objects.all()
jpre = journal.objects.all()



def list_ledger(listleg):

	listledger = [['','','','']	for x in range(lspre.count())]

	f=0
	for q in lspre:
		k=0
		while k<4:
			if (k==0):
				listledger[f][k] =q.Creation_Date
			elif(k==1):
				listledger[f][k] =q.name
			elif(k==2):
				gn = q.group1_Name
				gn_bn = gn.balance_nature
				listledger[f][k] = gn_bn
			else:
				listledger[f][k] =q.Opening_Balance
			k=k+1
		f=f+1

	return listledger

## #JOURNAL
# List3 =[[DATE,TO,BY,DEBIT,CREDIT],
# 		[DATE,TO,BY,DEBIT,CREDIT]]

def list_journal(listjour):

	listjournal= [['','','','',''] for x in range(jpre.count())]

	c=0 
	for i in jpre:
		d=0
		while d<5:
			if (d==0):
				listjournal[c][d] =i.Date
			elif(d==1):
				listjournal[c][d] =i.To
			elif(d==2):
				listjournal[c][d] =i.By
			elif(d==3):
				listjournal[c][d] =i.Debit
			else:
				listjournal[c][d] =i.Credit
			d=d+1
		c=c+1
	return listjournal

# journal List i =[[DATE,TO,BY,DEBIT,CREDIT],]
#  ledgerlist1 w =[[name,,bal_nature,creation_date,opening balance],]



ls = list_ledger(lspre)



j = list_journal(jpre)

print(ls,'\n',j)

# total of to side
for w in listledger:
	#print(w[2],w[3])
	# eg hdfc a/c 'to' side total will be all to sides where hdfc is 'by' or debited
		# journal loop
	sum1 =0
	for i in listjournal:

		if(str(i[2]) == w[1]):
			sum1 +=i[3]
		
	print('\n',w[1],'-',sum1)
	# if(w[2] == 'Debit'):# check bal nature
	# 	o_b = w[3]
	# 	sum1 = sum1 + o_b 








# total of by side












# closing balance final
# list2 = [[name,date,closing_balance],
# 			[name,date,closing_balance]]