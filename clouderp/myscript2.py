# https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell

#python manage.py shell < myscript.py

from accounting_double_entry.models import ledger1,group1,journal
from datetime import datetime,date

ls = ledger1.objects.all()

ls1 = ls[0]

cdate= ls1.Creation_Date

# gn = ls1.group1_Name
# gn_bn = gn.balance_nature

diffdate = date.today()-cdate

j = journal.objects.all()

#print(ls,'\n',ls1,'\n',cdate,'\n',gn,
#     '\n',gn_bn,'\n',diffdate,'\n',j)


# ledger name loop stored in a list with opening balance and its date 
# LEDGER DATA
# list1 =[[name,,bal_nature,creation_date,opening balance],
#  		  [name,bal_nature,creation_date,opening balance],
#  		[name,bal_nature,creation_date,opening balance]]

# list2 = [ [[name],[date,closing_balance],[date,closing_balance],[date,closing_balance]] ,
# 		  [[name],[date,closing_balance],[date,closing_balance],[date,closing_balance]] ,
# 		  [[name],[date,closing_balance],[date,closing_balance],[date,closing_balance]] ]

	
# #JOURNAL
# List3 =[[DATE,TO,BY,DEBIT,CREDIT],
# 		[DATE,TO,BY,DEBIT,CREDIT]]

# blank list creation

list33= [['','','','',''] for x in range(j.count())]

c=0 # j.count
for i in j:
	d=0
	while d<5:
		if (d==0):
			list33[c][d] =i.Date
		elif(d==1):
			list33[c][d] =i.To
		elif(d==2):
			list33[c][d] =i.By
		elif(d==3):
			list33[c][d] =i.Debit
		else:
			list33[c][d] =i.Credit
		d=d+1
	c=c+1

print(list33)


list44 = [['','','','']	for x in range(ls.count())]

f=0
for q in ls:
	k=0
	while k<4:
		if (k==0):
			list44[f][k] =q.Creation_Date
		elif(k==1):
			list44[f][k] =q.name
		elif(k==2):
			gn = q.group1_Name
			gn_bn = gn.balance_nature
			list44[f][k] = gn_bn
		else:
			list44[f][k] =q.Opening_Balance
		k=k+1
	f=f+1

print(list44)



#i = j.select_related('Hdfc A/c')
#print(i)
#for i in j:
	# print('\n',
	# 	i.Date,'\n',

	# 	i.By,'\n',
	# 	i.Debit,'\n',

	# 	i.To,'\n',
	# 	i.Credit,'\n',)

#for n in ls:
#	print(n.journal_set.all())


# def closing_balance(bal_nature,by_total,to_total,date_strt,date_end):
# 	pass
# 	def by_total():
# 		pass

# ld = journal.objects.all()
# ld1 = ld[0].To
# lf = ld1.group1_Name
# lk = lf.balance_nature

# print(ld,'\n',ld1,'\n',lf,'\n',lk)


