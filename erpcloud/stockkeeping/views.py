from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from company.models import company
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase,Sales,Stock_Total,Stock_Total_sales
from stockkeeping.forms import Stockgroup_form,Simpleunits_form,Compoundunits_form,Stockdata_form,Purchase_form,Sales_form,Purchase_formSet,Sales_formSet
from userprofile.models import Profile
from django.shortcuts import get_object_or_404
from django.db import transaction
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
		compoundunits_details  = get_object_or_404(Compoundunits, pk=self.kwargs['pk2'])
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		return reverse('stockkeeping:stockdatadetail', kwargs={'pk1':company_details.pk, 'pk2':compoundunits_details.pk,'pk3':selectdatefield_details.pk})

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
			Company=company.objects.get(pk=self.kwargs['pk'])
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
		context = super(Compoundunits_deleteview, self).get_context_data(**kwargs) 
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

