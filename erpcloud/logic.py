




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



# {% if purchase_details.State == company_details.State %}
#                       <tr>
#                         <th>CGST ({{purchase_details.stockitem.gst_rate}}%)</th>
#                         <td>{{purchase_details.Total_Amount|mul:purchase_details.stockitem.gst_rate|div:2 }}</td>
#                       </tr>
#                       <tr>
#                         <th>SGST ({{purchase_details.stockitem.gst_rate}}%)</th>
#                         <td>{{purchase_details.Total_Amount|mul:purchase_details.stockitem.gst_rate|div:2 }}</td>
#                       </tr>
#                       <tr>
#                     <th>Total:</th>
#                       <td>{{purchase_details.Total_Amount|mul:1|add:purchase_details.stockitem.gst_rate|div:100}}</td>
#                     </tr>
#                 {% else %}
#                       <tr>
#                         <th>IGST ({{purchase_details.stockitem.gst_rate}}%)</th>
#                         <td>{{purchase_details.Total_Amount|mul:purchase_details.stockitem.gst_rate}}</td>
#                       </tr>
#                       <tr>
#                       <th>Total:</th>
#                         <td>{{purchase_details.Total_Amount|mul:1|add:purchase_details.stockitem.gst_rate|div:100}}</td>
#                       </tr>
#                 {% endif %}


# @login_required
# def ledger1_detail_view(request, pk, pk2, pk3):
# 	company_details = get_object_or_404(company, pk=pk)
# 	purchase_details = get_object_or_404(purchase, pk=pk2)
# 	sale_details = get_object_or_404(sale, pk=pk2)
# 	selectdatefield_details = get_object_or_404(selectdatefield, pk=pk3)
# 	# existing opening stock = all purchase of all stock items till starting date 
# 	qspur  = purchase.objects.filter(User=request.user, Company=company_details.pk, Date__gte=purchase_details.purchase.Creation_Date, Date__lte=selectdatefield_details.Start_Date)
# 	qsstock = qspur.objects.filter(User=request.user, Company=company_details.pk)

# 	qssale  = sale.objects.filter(User=request.user, Company=company_details.pk, Date__gte=sale_details.sales.Creation_Date, Date__lte=selectdatefield_details.Start_Date)
# 	qsstock = qssale.objects.filter(User=request.user, Company=company_details.pk)

# 	total_purchase = qspur.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']
# 	total_sale = qssale.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']

# 	opening_stock = total_purchase - total_sale

#   clsing stock

# 	qspur  = purchase.objects.filter(User=request.user, Company=company_details.pk, Date__gte=selectdatefield_details.Start_Date, Date__lte=selectdatefield_details.End_Date)
# 	qsstock = qspur.objects.filter(User=request.user, Company=company_details.pk)

# 	qssale  = sale.objects.filter(User=request.user, Company=company_details.pk, Date__gte=selectdatefield_details.Start_Date, Date__lte=selectdatefield_details.Start_Date)
# 	qsstock = qssale.objects.filter(User=request.user, Company=company_details.pk)

# 	total_purchase = qspur.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']
# 	total_sale = qssale.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']

# 	closing_stock = opening_stock + total_purchase - total_sale

# 	context = {

# 		'company_details' : company_details,
# 		'ledger1_details' : ledger1_details,
# 		'selectdatefield_details' : selectdatefield_details,
# 		'total_debit'     : total_debitcb,
# 		'total_credit'    : total_creditcb,
# 		'journal_debit'   : qscb,
# 		'journal_credit'  : qscb2,
# 		'closing_balance' : closing_balance,
# 		'opening_balance' : opening_balance,		
# 		'company_list'    : company.objects.all(),
# 		'selectdate' 	  : selectdatefield.objects.filter(User=request.user),
				
# 	}	

# 	return render(request, 'accounting_double_entry/ledger1_details.html', context)