from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from accounting_double_entry.forms import journalForm,group1Form,Ledgerform,DateRangeForm
from userprofile.models import Profile
from django.db.models import Sum
from company.models import company
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import F
import datetime
from django.db.models import Value
from django.db.models.functions import Coalesce

# Create your views here.
###################### Views For Group Display ############################################

class group1ListView(LoginRequiredMixin,ListView):
	model = group1
	paginate_by = 15

	def get_queryset(self):
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(group1ListView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class group1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'group1_details'
	model = group1
	template_name = 'accounting_double_entry/group1_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		group = get_object_or_404(group1, pk=pk2)
		return group


	def get_context_data(self, **kwargs):
		context = super(group1DetailView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class group1CreateView(LoginRequiredMixin,CreateView):
	form_class  = group1Form
	template_name = "accounting_double_entry/group1_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:grouplist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})


	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(group1CreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(group1CreateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class group1UpdateView(LoginRequiredMixin,UpdateView):
	model = group1
	form_class  = group1Form
	template_name = "accounting_double_entry/group1_form.html"


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		group1_details  = get_object_or_404(group1, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:groupdetail', kwargs={'pk1':company_details.pk, 'pk2':group1_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		group = get_object_or_404(group1, pk=pk2)
		return group


	def get_context_data(self, **kwargs):
		context = super(group1UpdateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class group1DeleteView(LoginRequiredMixin,DeleteView):
	model = group1

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:grouplist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})
	

	def get_object(self):
		pk = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk)
		group = get_object_or_404(group1, pk=pk2)
		return group

	def get_context_data(self, **kwargs):
		context = super(group1DeleteView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

################## Views For Ledger Display ###################################


class ledger1ListView(LoginRequiredMixin,ListView):
	model = ledger1
	paginate_by = 15

	def get_queryset(self):
		return ledger1.objects.filter(User=self.request.user, Company=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(ledger1ListView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

@login_required
def ledger1_detail_view(request, pk, pk2, pk3):
	company_details = get_object_or_404(company, pk=pk)
	ledger1_details = get_object_or_404(ledger1, pk=pk2)
	selectdatefield_details = get_object_or_404(selectdatefield, pk=pk3)

	# opening balance
	qsob  = journal.objects.filter(User=request.user, Company=company_details.pk, By=ledger1_details.pk, Date__gte=ledger1_details.Creation_Date, Date__lte=selectdatefield_details.Start_Date)
	qsob2 = journal.objects.filter(User=request.user, Company=company_details.pk, To=ledger1_details.pk, Date__gte=ledger1_details.Creation_Date, Date__lte=selectdatefield_details.Start_Date)

	total_debitob = qsob.aggregate(the_sum=Coalesce(Sum('Debit'), Value(0)))['the_sum']
	total_creditob = qsob2.aggregate(the_sum=Coalesce(Sum('Credit'), Value(0)))['the_sum']

	# opening balance
	qscb  = journal.objects.filter(User=request.user, Company=company_details.pk, By=ledger1_details.pk, Date__gte=selectdatefield_details.Start_Date, Date__lte=selectdatefield_details.End_Date)
	qscb2 = journal.objects.filter(User=request.user, Company=company_details.pk, To=ledger1_details.pk, Date__gte=selectdatefield_details.Start_Date, Date__lte=selectdatefield_details.End_Date)	

	total_debitcb = qscb.aggregate(the_sum=Coalesce(Sum('Debit'), Value(0)))['the_sum']
	total_creditcb = qscb2.aggregate(the_sum=Coalesce(Sum('Credit'), Value(0)))['the_sum']
	
	if(ledger1_details.Creation_Date!=selectdatefield_details.Start_Date):
		if(ledger1_details.group1_Name.balance_nature == 'Debit'):
			opening_balance = ledger1_details.Opening_Balance + total_debitob - total_creditob
		else:
			opening_balance = ledger1_details.Opening_Balance + total_creditob - total_debitob 
	else:
		opening_balance = ledger1_details.Opening_Balance

	if(ledger1_details.group1_Name.balance_nature == 'Debit'):
		closing_balance = opening_balance + total_debitcb - total_creditcb
	else:
		closing_balance = opening_balance + total_creditcb - total_debitcb 


	context = {

		'company_details' : company_details,
		'ledger1_details' : ledger1_details,
		'selectdatefield_details' : selectdatefield_details,
		'total_debit'     : total_debitcb,
		'total_credit'    : total_creditcb,
		'journal_debit'   : qscb,
		'journal_credit'  : qscb2,
		'closing_balance' : closing_balance,
		'opening_balance' : opening_balance,		
		'company_list'    : company.objects.all(),
		'selectdate' 	  : selectdatefield.objects.filter(User=request.user),
				
	}	

	return render(request, 'accounting_double_entry/ledger1_details.html', context)


class ledger1CreateView(LoginRequiredMixin,CreateView):
	form_class = Ledgerform
	template_name = "accounting_double_entry/ledger1_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:ledgerlist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(ledger1CreateView, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(ledger1CreateView, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(ledger1CreateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class ledger1UpdateView(LoginRequiredMixin,UpdateView):
	model = ledger1
	form_class = Ledgerform
	template_name = "accounting_double_entry/ledger1_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		ledger1_details = get_object_or_404(ledger1, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:ledgerdetail', kwargs={'pk':company_details.pk, 'pk2':ledger1_details.pk, 'pk3' : selectdatefield_details.pk})

	def get_object(self):
		pk = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk)
		ledger = get_object_or_404(ledger1, pk=pk2)
		return ledger

	def get_form_kwargs(self):
		data = super(ledger1UpdateView, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data


	def get_context_data(self, **kwargs):
		context = super(ledger1UpdateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class ledger1DeleteView(LoginRequiredMixin,DeleteView):
	model = ledger1

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:ledgerlist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})
	

	def get_object(self):
		pk1 = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		ledger = get_object_or_404(ledger1, pk=pk2)
		return ledger


	def get_context_data(self, **kwargs):
		context = super(ledger1DeleteView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		context['selectdates'] = selectdatefield.objects.filter(User=self.request.user)
		return context
	

################## Views For journal Display ###################################


class journalListView(LoginRequiredMixin,ListView):
	model = journal
	paginate_by = 15

	def get_queryset(self):
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return journal.objects.filter(User=self.request.user, Company=self.kwargs['pk'], Date__gte=selectdatefield_details.Start_Date, Date__lte=selectdatefield_details.End_Date)


	def get_context_data(self, **kwargs):
		context = super(journalListView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		context['narrate'] = 'being journal.By debited by journal.To for journal.Credit.'
		return context

def journal_detail(request, pk1, pk2, pk3):
	company_details = get_object_or_404(company, pk=pk1)
	journal_details = get_object_or_404(journal, pk=pk2)
	selectdatefield_details = get_object_or_404(selectdatefield, pk=pk3)


	context = {
		'journal_details'          : journal_details,
		'company_details'          : company_details,
		'selectdatefield_details'  : selectdatefield_details,
	}
	return render(request, 'accounting_double_entry/journal_details.html', context)



class journalCreateView(LoginRequiredMixin,CreateView):
	model = journal
	form_class  = journalForm

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:list', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(journalCreateView, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(journalCreateView, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data


	def get_context_data(self, **kwargs):
		context = super(journalCreateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class journalUpdateView(LoginRequiredMixin,UpdateView):
	model = journal
	form_class  = journalForm

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		journal_details = get_object_or_404(journal, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:detail', kwargs={'pk1':company_details.pk, 'pk2':journal_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		Journal = get_object_or_404(journal, pk=pk2)
		return Journal

	def get_form_kwargs(self):
		data = super(journalUpdateView, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk1'])
			)
		return data


	def get_context_data(self, **kwargs):
		context = super(journalUpdateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class journalDeleteView(LoginRequiredMixin,DeleteView):
	model = journal

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('accounting_double_entry:list', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		Journal = get_object_or_404(journal, pk=pk2)
		return Journal


	def get_context_data(self, **kwargs):
		context = super(journalDeleteView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

################## Views For Daterange Display ###################################

class datecreateview(LoginRequiredMixin,CreateView):
	form_class = DateRangeForm
	template_name = "company/selectdate.html"

	def get_success_url(self,**kwargs):
		return reverse('company:list')

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(datecreateview, self).form_valid(form)

class dateupdateview(LoginRequiredMixin,UpdateView):
	model = selectdatefield
	form_class = DateRangeForm
	template_name = "company/selectdate.html"

	def get_success_url(self,**kwargs):
		return reverse('company:list')

































# def search_by_date(request,pk,pk1):
# 	template = 'accounting_double_entry/ledger1_details.html'

# 	query_start = request.GET.get('s')

# 	query_end = request.GET.get('q')

# 	if query_start and query_end:
# 		# selectdaterange.objects.get_or_create(Start_Date=query_start,End_Date=query_end)
# 		result = journal.objects.filter(User=request.user, Date__gte=query_start, Date__lte=query_end)

# 	else:
# 		result = journal.objects.filter(User=request.user)

# 	company_details = get_object_or_404(company, pk=pk)
# 	ledger1_details = get_object_or_404(ledger1, pk=pk1)

# 	context = {
# 		'journal_list'    : result,
# 		'ledger1_details' : ledger1_details,
# 		'company_details' : company_details,
# 	}

# 	return render(request, template, context)