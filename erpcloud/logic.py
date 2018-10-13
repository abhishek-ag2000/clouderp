




#class selectdatefield(models.Model):
# 	Start_Date = models.DateField(blank=True, null=True)
# 	End_Date = models.DateField(blank=True, null=True)
# 	User = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="Users",on_delete=models.CASCADE,null=True,blank=True)
# 	Company = models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True,related_name='CompanyDate')

# 	def __str__(self):
# 		return str(self.End_Date)

# 	def get_absolute_url(self):
# 		return reverse("company:list")

# 	def clean(self):
# 		if self.Start_Date > self.End_Date:
# 			raise ValidationError('Start Date Cannot Be Greater Than End Date')

# class calculations(models.Model):
# 	daterange = models.ForeignKey(selectdatefield,on_delete=models.CASCADE,null=True,blank=True,related_name='endDate')
# 	Journal = models.ForeignKey(journal,on_delete=models.CASCADE,null=True,blank=True,related_name='journals')
# 	Ledger = models.ForeignKey(ledger1,on_delete=models.CASCADE,null=True,blank=True,related_name='ledgers')
# 	ledger_opening_bal     = models.DecimalField(max_digits=10,decimal_places=2)
# 	ledger_closing_balance = models.DecimalField(max_digits=10,decimal_places=2)

# 	def __str__(self):
# 		return str(self.ledger_closing_balance)

# 	def opening_balance(self,self.ledger,start_date,end_date):
# 		if startdate == ledger.creationdate:
# 			return ledger.opening_balance
# 		elif startdate > ledger.creationdate:
# 			# checking transactions via balance nature
# 			if groups.ledger.balance_nature == 'dr':
# 				debit = instance.Debitledgers.aggregate(debit=Sum('Debit'))['debit'](daterange)
#     			credit = instance.Creditledgers.aggregate(credit=Sum('Credit'))['credit']
# 				opening_balance = ledger.opening_balance + debit - credit
# 			else:
# 				debit = instance.Debitledgers.aggregate(debit=Sum('Debit'))['debit'](daterange)
#     			credit = instance.Creditledgers.aggregate(credit=Sum('Credit'))['credit']
# 				opening_balance = ledger.opening_balance - debit + credit
# 			return opening_balance
# 		else:
# 			pass

# 	def closing_balance(self,self.ledger,start_date,end_date):
# 		open_bal = opening_balance(self,self.ledger,start_date)
# 		if groups.ledger.balance_nature == 'dr':
# 				debit = instance.Debitledgers.aggregate(debit=Sum('Debit'))['debit'](daterange)
#     			credit = instance.Creditledgers.aggregate(credit=Sum('Credit'))['credit']
# 				closing_balance = ledger.opening_balance + debit - credit
# 			else:
# 				debit = instance.Debitledgers.aggregate(debit=Sum('Debit'))['debit'](daterange)
#     			credit = instance.Creditledgers.aggregate(credit=Sum('Credit'))['credit']
# 				closing_balance = ledger.opening_balance - debit + credit
#     	return closing_balance