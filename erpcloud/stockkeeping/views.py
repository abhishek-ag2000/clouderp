from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from company.models import company
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase,Sales,Stock_Total,Stock_Total_sales
from stockkeeping.forms import Stockgroup_form,Simpleunits_form,Compoundunits_form,Stockdata_form,Purchase_form,Sales_form,Purchase_formSet,Sales_formSet
from userprofile.models import Profile
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models.functions import Coalesce
from django.db.models import Value, Sum, F, ExpressionWrapper
from django.db.models.fields import DecimalField
# Create your views here.


##################################### Simple Unit Views #####################################

class Simpleunits_listview(LoginRequiredMixin,ListView):
	model = Simpleunits
	template_name = 'stockkeeping/simpleunits/simpleunits_list.html'
	paginate_by = 15


	def get_queryset(self):
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(Simpleunits_listview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Simpleunits_detailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'simpleunits_details'
	model = Simpleunits
	template_name = 'stockkeeping/simpleunits/simpleunits_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		simpleunit = get_object_or_404(Simpleunits, pk=pk2)
		return simpleunit


	def get_context_data(self, **kwargs):
		context = super(Simpleunits_detailsview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Simpleunits_createview(LoginRequiredMixin,CreateView):
	form_class  = Simpleunits_form
	template_name = "stockkeeping/simpleunits/simpleunits_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:simplelist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(Simpleunits_createview, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(Simpleunits_createview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Simpleunits_updateview(LoginRequiredMixin,UpdateView):
	model = Simpleunits
	form_class  = Simpleunits_form
	template_name = "stockkeeping/simpleunits/simpleunits_form.html"


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		simpleunits_details  = get_object_or_404(Simpleunits, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:simpledetail', kwargs={'pk1':company_details.pk, 'pk2':group1_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		simpleunit = get_object_or_404(Simpleunits, pk=pk2)
		return simpleunit

	def get_context_data(self, **kwargs):
		context = super(Simpleunits_updateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class Simpleunits_deleteview(LoginRequiredMixin,DeleteView):
	model = Simpleunits
	template_name = "stockkeeping/simpleunits/simpleunits_confirm_delete.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:simplelist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk)
		simpleunit = get_object_or_404(Simpleunits, pk=pk2)
		return simpleunit

	def get_context_data(self, **kwargs):
		context = super(Simpleunits_deleteview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


##################################### Compound Unit Views #####################################



class Compoundunit_listview(LoginRequiredMixin,ListView):
	model = Compoundunits
	template_name = 'stockkeeping/compoundunits/compoundunits_list.html'
	paginate_by = 15


	def get_queryset(self):
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(Compoundunit_listview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class Compoundunits_detailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'compoundunits_details'
	model = Compoundunits
	template_name = 'stockkeeping/compoundunits/compoundunits_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		compoundunit = get_object_or_404(Compoundunits, pk=pk2)
		return compoundunit


	def get_context_data(self, **kwargs):
		context = super(Compoundunits_detailsview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Compoundunits_createview(LoginRequiredMixin,CreateView):
	form_class  = Compoundunits_form
	template_name = "stockkeeping/compoundunits/compoundunits_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:compoundlist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(Compoundunits_createview, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(Compoundunits_createview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Compoundunits_createview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Compoundunits_updateview(LoginRequiredMixin,UpdateView):
	model = Compoundunits
	form_class  = Compoundunits_form
	template_name = "stockkeeping/compoundunits/compoundunits_form.html"


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		compoundunits_details  = get_object_or_404(Compoundunits, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:compounddetail', kwargs={'pk1':company_details.pk, 'pk2':compoundunits_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		compoundunit = get_object_or_404(Compoundunits, pk=pk2)
		return compoundunit

	def get_form_kwargs(self):
		data = super(Compoundunits_updateview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Compoundunits_updateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Compoundunits_deleteview(LoginRequiredMixin,DeleteView):
	model = Compoundunits
	template_name = "stockkeeping/compoundunits/compoundunits_confirm_delete.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:compoundlist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		compoundunit = get_object_or_404(Compoundunits, pk=pk2)
		return compoundunit

	def get_context_data(self, **kwargs):
		context = super(Compoundunits_deleteview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

		
##################################### Stockgroup Views #####################################

class Stockgroup_listview(LoginRequiredMixin,ListView):
	model = Stockgroup
	template_name = 'stockkeeping/stockgroup/stockgroup_list.html'
	paginate_by = 15


	def get_queryset(self):
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(Stockgroup_listview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockgroup_detailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'stockgrp_details'
	model = Stockgroup
	template_name = 'stockkeeping/stockgroup/stockgroup_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		stockgroup = get_object_or_404(Stockgroup, pk=pk2)
		return Stockgroup


	def get_context_data(self, **kwargs):
		context = super(Stockgroup_detailsview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		stockgrp_details = get_object_or_404(Stockgroup, pk=self.kwargs['pk2'])
		context['stockgrp_details'] = stockgrp_details
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockgroup_createview(LoginRequiredMixin,CreateView):
	form_class  = Stockgroup_form
	template_name = "stockkeeping/stockgroup/stockgroup_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockgrouplist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(Stockgroup_createview, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(Stockgroup_createview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Stockgroup_createview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockgroup_updateview(LoginRequiredMixin,UpdateView):
	model = Stockgroup
	form_class  = Stockgroup_form
	template_name = "stockkeeping/stockgroup/stockgroup_form.html"


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		stockgroup_details  = get_object_or_404(Stockgroup, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockgroupdetail', kwargs={'pk1':company_details.pk, 'pk2':stockgroup_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		stockgroup = get_object_or_404(Stockgroup, pk=pk2)
		return stockgroup

	def get_form_kwargs(self):
		data = super(Stockgroup_updateview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk1'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Stockgroup_updateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockgroup_deleteview(LoginRequiredMixin,DeleteView):
	model = Stockgroup
	template_name = "stockkeeping/stockgroup/stockgroup_confirm_delete.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockgrouplist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		stockgroup = get_object_or_404(Stockgroup, pk=pk2)
		return stockgroup

	def get_context_data(self, **kwargs):
		context = super(Stockgroup_deleteview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


##################################### Stockitems Views #####################################

class closing_list_view(LoginRequiredMixin,ListView):
	model = Stockdata
	paginate_by = 15

	def get_template_names(self):
		if True:  
			return ['stockkeeping/closing_stock.html']
		else:
			return ['stockkeeping/stockitem/stockdata_list.html']


	def get_queryset(self):
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk']).order_by('-id')

	def get_context_data(self, **kwargs):
		context = super(closing_list_view, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		qsstart = Stockdata.objects.filter(User=self.request.user, Company=company_details.pk, Date__lte=selectdatefield_details.Start_Date)
		qs = Stockdata.objects.filter(User=self.request.user, Company=company_details.pk, Date__lte=selectdatefield_details.End_Date)
		total = qs.annotate(the_sum=Coalesce(Sum('salestock__Quantity'),0)).values('the_sum')
		total2 = qs.annotate(the_sum2=Coalesce(Sum('purchasestock__Quantity_p'),0)).values('the_sum2')
		qs = qs.annotate(
    		sales_sum = Coalesce(Sum('salestock__Quantity'),0),
    		purchase_sum = Coalesce(Sum('purchasestock__Quantity_p'),0),
    		purchase_tot = Coalesce(Sum('purchasestock__Total_p'),0)
		)
		qs1 = qs.annotate(
    		difference = ExpressionWrapper(F('purchase_sum') - F('sales_sum'), output_field=DecimalField()),
    		total = ExpressionWrapper((F('purchase_tot') / F('purchase_sum')) * (F('purchase_sum') - F('sales_sum')), output_field=DecimalField())
		) 
		context['Totalquantitysales'] = total
		context['Totalquantitypurchase'] = total2
		context['Totalquantity'] = qs1.values()
		return context

class Stockdata_listview(LoginRequiredMixin,ListView):
	model = Stockdata
	template_name = 'stockkeeping/stockitem/stockdata_list.html'
	paginate_by = 15


	def get_queryset(self):
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(Stockdata_listview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class Stockdata_detailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'stockdata_details'
	model = Stockdata
	template_name = 'stockkeeping/stockitem/stockdata_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		stockdata = get_object_or_404(Stockdata, pk=pk2)
		return stockdata


	def get_context_data(self, **kwargs):
		context = super(Stockdata_detailsview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockdata_createview(LoginRequiredMixin,CreateView):
	form_class  = Stockdata_form
	template_name = "stockkeeping/stockitem/stockdata_form.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockdatalist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		return super(Stockdata_createview, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(Stockdata_createview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Stockdata_createview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockdata_updateview(LoginRequiredMixin,UpdateView):
	model = Stockdata
	form_class  = Stockdata_form
	template_name = "stockkeeping/stockitem/stockdata_form.html"


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		stockdata_details  = get_object_or_404(Stockdata, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockdatadetail', kwargs={'pk1':company_details.pk, 'pk2':stockdata_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		stockdata = get_object_or_404(Stockdata, pk=pk2)
		return stockdata

	def get_form_kwargs(self):
		data = super(Stockdata_updateview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk1'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Stockdata_updateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Stockdata_deleteview(LoginRequiredMixin,DeleteView):
	model = Stockdata
	template_name = "stockkeeping/stockitem/stockdataunits_confirm_delete.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockdatalist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		compoundunit = get_object_or_404(Stockdata, pk=pk2)
		return compoundunit

	def get_context_data(self, **kwargs):
		context = super(Stockdata_deleteview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

##################################### Purchase Views #####################################

class Purchase_listview(LoginRequiredMixin,ListView):
	model = Purchase
	template_name = 'stockkeeping/purchase/purchase_list.html'
	paginate_by = 15


	def get_queryset(self):
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'], date__gte=selectdatefield_details.Start_Date, date__lte=selectdatefield_details.End_Date)

	def get_context_data(self, **kwargs):
		context = super(Purchase_listview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class Purchase_detailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'purchase_details'
	model = Purchase
	template_name = 'stockkeeping/purchase/purchase_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		purchase = get_object_or_404(Purchase, pk=pk2)
		return purchase


	def get_context_data(self, **kwargs):
		context = super(Purchase_detailsview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		purchase_details = get_object_or_404(Purchase, pk=self.kwargs['pk2'])
		qsob  = Stock_Total.objects.filter(purchases=purchase_details.pk)
		context['stocklist'] = qsob
		
		return context

class Purchase_createview(LoginRequiredMixin,CreateView):
	form_class  = Purchase_form
	template_name = 'stockkeeping/purchase/purchase_form.html'

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:purchaselist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_context_data(self, **kwargs):
		context = super(Purchase_createview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		if self.request.POST:
			context['stocks'] = Purchase_formSet(self.request.POST)
		else:
			context['stocks'] = Purchase_formSet()
		return context

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		context = self.get_context_data()
		stocks = context['stocks']
		with transaction.atomic():
			self.object = form.save()
			if stocks.is_valid():
				stocks.instance = self.object
				stocks.save()
		return super(Purchase_createview, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(Purchase_createview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data



class Purchase_updateview(LoginRequiredMixin,UpdateView):
	model = Purchase
	form_class  = Purchase_form
	template_name = 'stockkeeping/purchase/purchase_form.html'


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		purchase_details  = get_object_or_404(Purchase, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:purchasedetail', kwargs={'pk1':company_details.pk, 'pk2':purchase_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		purchase = get_object_or_404(Purchase, pk=pk2)
		return purchase

	def get_form_kwargs(self):
		data = super(Purchase_updateview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data

	def get_context_data(self, **kwargs):
		context = super(Purchase_updateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

class Purchase_deleteview(LoginRequiredMixin,DeleteView):
	model = Purchase
	template_name = "stockkeeping/purchase/purchase_confirm_delete.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:purchaselist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		purchase = get_object_or_404(Purchase, pk=pk2)
		return purchase

	def get_context_data(self, **kwargs):
		context = super(Purchase_deleteview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context

##################################### Sales Views #####################################

class Sales_listview(LoginRequiredMixin,ListView):
	model = Sales
	template_name = 'stockkeeping/sales/sales_list.html'
	paginate_by = 15


	def get_queryset(self):
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return self.model.objects.filter(User=self.request.user, Company=self.kwargs['pk'], date__gte=selectdatefield_details.Start_Date, date__lte=selectdatefield_details.End_Date)

	def get_context_data(self, **kwargs):
		context = super(Sales_listview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class Sales_detailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'sales_details'
	model = Sales
	template_name = 'stockkeeping/sales/sales_details.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		sales = get_object_or_404(Sales, pk=pk2)
		return sales


	def get_context_data(self, **kwargs):
		context = super(Sales_detailsview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		sales_details = get_object_or_404(Sales, pk=self.kwargs['pk2'])
		qsjb  = Stock_Total_sales.objects.filter(sales=sales_details.pk)
		context['stocklist'] = qsjb
		return context

class Sales_createview(LoginRequiredMixin,CreateView):
	form_class  = Sales_form
	template_name = 'stockkeeping/sales/sales_form.html'

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:saleslist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_context_data(self, **kwargs):
		context = super(Sales_createview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		if self.request.POST:
			context['stocksales'] = Sales_formSet(self.request.POST)
		else:
			context['stocksales'] = Sales_formSet()
		return context

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		context = self.get_context_data()
		stocksales = context['stocksales']
		with transaction.atomic():
			self.object = form.save()
			if stocksales.is_valid():
				stocksales.instance = self.object
				stocksales.save()
		return super(Sales_createview, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(Sales_createview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk'])
			)
		return data



class Sales_updateview(LoginRequiredMixin,UpdateView):
	model = Sales
	form_class  = Sales_form
	template_name = 'stockkeeping/sales/sales_form.html'


	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		sales_details  = get_object_or_404(Sales, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:salesdetail', kwargs={'pk1':company_details.pk, 'pk2':sales_details.pk,'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		sales = get_object_or_404(Sales, pk=pk2)
		return sales

	def get_context_data(self, **kwargs):
		context = super(Sales_updateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		if self.request.POST:
			context['stocksales'] = Sales_formSet(self.request.POST)
		else:
			context['stocksales'] = Sales_formSet()
		return context

	def form_valid(self, form):
		form.instance.User = self.request.user
		c = company.objects.get(pk=self.kwargs['pk'])
		form.instance.Company = c
		context = self.get_context_data()
		stocksales = context['stocksales']
		with transaction.atomic():
			self.object = form.save()
			if stocksales.is_valid():
				stocksales.instance = self.object
				stocksales.save()
		return super(Sales_createview, self).form_valid(form)

	def get_form_kwargs(self):
		data = super(Sales_updateview, self).get_form_kwargs()
		data.update(
			User=self.request.user,
			Company=company.objects.get(pk=self.kwargs['pk1'])
			)
		return data



class Sales_deleteview(LoginRequiredMixin,DeleteView):
	model = Sales
	template_name = "stockkeeping/sales/sales_confirm_delete.html"

	def get_success_url(self,**kwargs):
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:saleslist', kwargs={'pk':company_details.pk, 'pk3':selectdatefield_details.pk})

	def get_object(self):
		pk1 = self.kwargs['pk']
		pk2 = self.kwargs['pk2']
		get_object_or_404(company, pk=pk1)
		sales = get_object_or_404(Sales, pk=pk2)
		return sales

	def get_context_data(self, **kwargs):
		context = super(Sales_deleteview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context		

##################################### Profit & Loss A/c #####################################

@login_required
def profit_and_loss_view(request,pk,pk3):
	company_details = get_object_or_404(company, pk=pk)
	selectdatefield_details = get_object_or_404(selectdatefield, pk=pk3)

	# closing stock
	qs = Stockdata.objects.filter(User=request.user, Company=company_details.pk, Date__lte=selectdatefield_details.End_Date)
	total = qs.annotate(the_sum=Coalesce(Sum('salestock__Quantity'),0)).values('the_sum')
	total2 = qs.annotate(the_sum2=Coalesce(Sum('purchasestock__Quantity_p'),0)).values('the_sum2')
	qs = qs.annotate(
    	sales_sum = Coalesce(Sum('salestock__Quantity'),0),
    	purchase_sum = Coalesce(Sum('purchasestock__Quantity_p'),0),
    	purchase_tot = Coalesce(Sum('purchasestock__Total_p'),0)
	)
	qs1 = qs.annotate(
    	difference = ExpressionWrapper(F('purchase_sum') - F('sales_sum'), output_field=DecimalField()),
    	total = ExpressionWrapper((F('purchase_tot') / F('purchase_sum')) * (F('purchase_sum') - F('sales_sum')), output_field=DecimalField())
		) 

	qs2 = qs1.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']

	# opening stock
	qo = Stockdata.objects.filter(User=request.user, Company=company_details.pk, Date__lte=selectdatefield_details.Start_Date)
	totalo = qo.annotate(the_sum=Coalesce(Sum('salestock__Quantity'),0)).values('the_sum')
	totalo2 = qo.annotate(the_sum2=Coalesce(Sum('purchasestock__Quantity_p'),0)).values('the_sum2')
	qo = qo.annotate(
    	sales_sum = Coalesce(Sum('salestock__Quantity'),0),
    	purchase_sum = Coalesce(Sum('purchasestock__Quantity_p'),0),
    	purchase_tot = Coalesce(Sum('purchasestock__Total_p'),0)
	)
	qo1 = qo.annotate(
    	difference = ExpressionWrapper(F('purchase_sum') - F('sales_sum'), output_field=DecimalField()),
    	total = ExpressionWrapper((F('purchase_tot') / F('purchase_sum')) * (F('purchase_sum') - F('sales_sum')), output_field=DecimalField())
		) 

	qo2 = qo1.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']

	ld = ledger1.objects.filter(User=request.user, Company=company_details.pk, group1_Name__group_Name__icontains='Purchase Accounts', Creation_Date__gte=selectdatefield_details.Start_Date, Creation_Date__lte=selectdatefield_details.End_Date)
	ldc = ld.aggregate(the_sum=Coalesce(Sum('Closing_balance'), Value(0)))['the_sum']

	ldd = ledger1.objects.filter(User=request.user, Company=company_details.pk, group1_Name__group_Name__icontains='Direct Expenses', Creation_Date__gte=selectdatefield_details.Start_Date, Creation_Date__lte=selectdatefield_details.End_Date)
	lddt = ldd.aggregate(the_sum=Coalesce(Sum('Closing_balance'), Value(0)))['the_sum']

	ldi = ledger1.objects.filter(User=request.user, Company=company_details.pk, group1_Name__group_Name__icontains='Direct Incomes', Creation_Date__gte=selectdatefield_details.Start_Date, Creation_Date__lte=selectdatefield_details.End_Date)
	lddi = ldi.aggregate(the_sum=Coalesce(Sum('Closing_balance'), Value(0)))['the_sum']

	lds = ledger1.objects.filter(User=request.user, Company=company_details.pk, group1_Name__group_Name__icontains='Sales Account', Creation_Date__gte=selectdatefield_details.Start_Date, Creation_Date__lte=selectdatefield_details.End_Date)
	ldsc = lds.aggregate(the_sum=Coalesce(Sum('Closing_balance'), Value(0)))['the_sum']

	lde = ledger1.objects.filter(User=request.user, Company=company_details.pk, group1_Name__group_Name__icontains='Indirect Expenses', Creation_Date__gte=selectdatefield_details.Start_Date, Creation_Date__lte=selectdatefield_details.End_Date)
	ldse = lde.aggregate(the_sum=Coalesce(Sum('Closing_balance'), Value(0)))['the_sum']

	ldi = ledger1.objects.filter(User=request.user, Company=company_details.pk, group1_Name__group_Name__icontains='Indirect Incomes', Creation_Date__gte=selectdatefield_details.Start_Date, Creation_Date__lte=selectdatefield_details.End_Date)
	ldsi = ldi.aggregate(the_sum=Coalesce(Sum('Closing_balance'), Value(0)))['the_sum']

	# qo1 means opening stock exists

	if qo1:
		gp = (abs(ldsc) + abs(qs2) + abs(lddt)) - (abs(qo2) + abs(ldc) + abs(lddi))
	else:
		gp = abs(ldsc) + abs(qs2) - abs(ldc)

	if gp >=0:
		if qo1 :
			tradingp  =  abs(qo2) + abs(ldc) + abs(lddt) + abs(gp)
			tradingp2 = abs(qs2) + abs(ldsi) + abs(ldsc) 
		else:
			tradingp =  abs(ldc) + abs(lddt) + abs(gp)
			tradingp2 = abs(qs2) + abs(ldsi) + abs(ldsc)

	else: # gp <0
		if qo1 :
			tradingp =  abs(qo2) + abs(ldc) + abs(lddt) 
			tradingp2 = abs(qs2) + abs(ldsi) + abs(ldsc) + abs(gp) 
		else:
			tradingp =  abs(ldc) + abs(lddt)
			tradingp2 = abs(qs2) + abs(ldsi) + abs(ldsc) + abs(gp)

	tgp = abs(qs2) + abs(ldsi) + abs(ldsc)

	np = abs(gp) + abs(ldsi) - abs(ldse)

	tp = abs(ldse) + abs(np)

	tc = abs(ldsi) + abs(gp)

	context = {

		'company_details' : company_details,
		'selectdatefield_details' : selectdatefield_details,
		'closing_stock' : qs2,
		'each_closing_stock' : qs1.values(),
		'opening_stock': qo2,
		'each_opening_stock' : qo1.values(),
		'purchase_ledger' : ld,
		'total_purchase_ledger' : ldc,
		'sales_ledger' : lds,
		'total_sales_ledger' : ldsc,
		'indirectexp_ledger' : lde,
		'total_indirectexp_ledger' : ldse,
		'indirectinc_ledger' : ldi,
		'total_indirectinc_ledger' : ldsi,
		'total_direct_expenses': lddt,
		'direct_expenses': ldd,
		'total_direct_incomes': lddi,
		'direct_incomes': ldi,
		'gross_profit' : gp,
		'nett_profit' : np,
		'tradingprofit': tradingp,
		'tradingprofit2': tgp,
		'totalpl' : tp,
		'totalplright' : tc
	}

	return render(request, 'stockkeeping/P&L.html', context)

##################################### Trial Balance #####################################

@login_required
def trial_balance_view(request,pk,pk3):
	company_details = get_object_or_404(company, pk=pk)
	selectdatefield_details = get_object_or_404(selectdatefield, pk=pk3)

	# opening stock
	qo = Stockdata.objects.filter(User=request.user, Company=company_details.pk, Date__lte=selectdatefield_details.Start_Date)
	totalo = qo.annotate(the_sum=Coalesce(Sum('salestock__Quantity'),0)).values('the_sum')
	totalo2 = qo.annotate(the_sum2=Coalesce(Sum('purchasestock__Quantity_p'),0)).values('the_sum2')
	qo = qo.annotate(
    	sales_sum = Coalesce(Sum('salestock__Quantity'),0),
    	purchase_sum = Coalesce(Sum('purchasestock__Quantity_p'),0),
    	purchase_tot = Coalesce(Sum('purchasestock__Total_p'),0)
	)
	qo1 = qo.annotate(
    	difference = ExpressionWrapper(F('purchase_sum') - F('sales_sum'), output_field=DecimalField()),
    	total = ExpressionWrapper((F('purchase_tot') / F('purchase_sum')) * (F('purchase_sum') - F('sales_sum')), output_field=DecimalField())
		) 

	qo2 = qo1.aggregate(the_sum=Coalesce(Sum('total'), Value(0)))['the_sum']

	groups = group1.objects.filter(User=request.user, Company=company_details.pk, ledgergroups__Creation_Date__gte=selectdatefield_details.Start_Date, ledgergroups__Creation_Date__lte=selectdatefield_details.End_Date)
	groups_cb = groups.annotate(
				closing = Coalesce(Sum('ledgergroups__Closing_balance'), 0),
				opening = Coalesce(Sum('ledgergroups__Balance_opening'), 0),
			)

	# groups with debit balance nature
	groupsdebit = group1.objects.filter(User=request.user, Company=company_details.pk, balance_nature__icontains='Debit', ledgergroups__Creation_Date__gte=selectdatefield_details.Start_Date, ledgergroups__Creation_Date__lte=selectdatefield_details.End_Date)
	groups_cbc = groupsdebit.annotate(
				closing = Coalesce(Sum('ledgergroups__Closing_balance'), 0)).filter(closing__gt = 0)

	groupcbl = groupsdebit.annotate(
			closing = Coalesce(Sum('ledgergroups__Closing_balance'), 0)).filter(closing__lt = 0)

	group_ob = groupsdebit.annotate(
			opening = Coalesce(Sum('ledgergroups__Balance_opening'), 0)).filter(opening__gt = 0)

	group_obl = groupsdebit.annotate(
			opening = Coalesce(Sum('ledgergroups__Balance_opening'), 0)).filter(opening__lt = 0)

	posdebcb = groups_cbc.aggregate(the_sum=Coalesce(Sum('closing'), Value(0)))['the_sum']
	negdbcl = groupcbl.aggregate(the_sum=Coalesce(Sum('closing'), Value(0)))['the_sum']
	posdebob = group_ob.aggregate(the_sum=Coalesce(Sum('opening'), Value(0)))['the_sum']
	negdebob = group_obl.aggregate(the_sum=Coalesce(Sum('opening'), Value(0)))['the_sum']


	# groups with credit balance nature
	groupscredit = group1.objects.filter(User=request.user, Company=company_details.pk, balance_nature__icontains='Credit', ledgergroups__Creation_Date__gte=selectdatefield_details.Start_Date, ledgergroups__Creation_Date__lte=selectdatefield_details.End_Date)

	groups_ccb = groupscredit.annotate(
				closing = Coalesce(Sum('ledgergroups__Closing_balance'), 0)).filter(closing__gt = 0)

	groupcbcl = groupscredit.annotate(
			closing = Coalesce(Sum('ledgergroups__Closing_balance'), 0)).filter(closing__lt = 0)

	group_cob = groupscredit.annotate(
			opening = Coalesce(Sum('ledgergroups__Balance_opening'), 0)).filter(opening__gt = 0)

	group_ocbl = groupscredit.annotate(
			opening = Coalesce(Sum('ledgergroups__Balance_opening'), 0)).filter(opening__lt = 0)


	poscrcl = groups_ccb.aggregate(the_sum=Coalesce(Sum('closing'), Value(0)))['the_sum']
	necrcl = groupcbcl.aggregate(the_sum=Coalesce(Sum('closing'), Value(0)))['the_sum']
	pocrob = group_cob.aggregate(the_sum=Coalesce(Sum('opening'), Value(0)))['the_sum']
	necrob = group_ocbl.aggregate(the_sum=Coalesce(Sum('opening'), Value(0)))['the_sum']


	total_debit_closing = posdebcb + abs(necrcl) + qo2
	total_credit_closing = poscrcl + abs(negdbcl)

	total_debit_opening = posdebob + abs(necrob)
	total_credit_opening = pocrob + abs(negdebob)





	context = {
		'company_details' : company_details,
		'selectdatefield_details' : selectdatefield_details,
		'opening_stock' : qo2,
		'groups' : groups,
		'groups_closing' : groups_cb,

		'total_debit_closing' : total_debit_closing,
		'total_debit_opening' : total_debit_opening,

		'total_credit_closing' : total_credit_closing,
		'total_credit_opening' : total_credit_opening,
	}

	return render(request, 'stockkeeping/Trial_Balance/trial_bal.html', context)



