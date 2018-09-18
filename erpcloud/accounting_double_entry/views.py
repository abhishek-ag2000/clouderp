from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounting_double_entry.models import group1,ledger1,journal
from accounting_double_entry.forms import journalForm,group1Form,Ledgerform
from userprofile.models import Profile
from django.db.models import Sum
from company.models import company
from django.db.models import Q



# Create your views here.
###################### Views For Group Display ############################################

class group1ListView(LoginRequiredMixin,ListView):
	model = group1

	def get_queryset(self):
		return group1.objects.filter(User=self.request.user)

	def get_context_data(self, **kwargs):
		context = super(group1ListView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class group1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'group1_details'
	model = group1
	template_name = 'accounting_double_entry/group1_details.html'

	def get_context_data(self, **kwargs):
		context = super(group1DetailView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context


class group1CreateView(LoginRequiredMixin,CreateView):
	form_class  = group1Form
	template_name = "accounting_double_entry/group1_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(group1CreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(group1CreateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class group1UpdateView(LoginRequiredMixin,UpdateView):
	model = group1
	form_class  = group1Form
	template_name = "accounting_double_entry/group1_form.html"


	def get_context_data(self, **kwargs):
		context = super(group1UpdateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class group1DeleteView(LoginRequiredMixin,DeleteView):
	model = group1
	success_url = reverse_lazy("accounting_double_entry:grouplist")

	def get_context_data(self, **kwargs):
		context = super(group1DeleteView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

################## Views For Ledger Display ###################################


class ledger1ListView(LoginRequiredMixin,ListView):
	model = ledger1

	def get_queryset(self):
		return ledger1.objects.filter(User=self.request.user)

	def get_context_data(self, **kwargs):
		context = super(ledger1ListView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class ledger1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'ledger1_details'
	model = ledger1
	template_name = 'accounting_double_entry/ledger1_details.html'

	def get_context_data(self, **kwargs):
		context = super(ledger1DetailView, self).get_context_data(**kwargs) 
		context['journal_list'] = journal.objects.all()
		context['company_list'] = company.objects.all()
		context['profile_list'] = Profile.objects.all()
		return context

class ledger1CreateView(LoginRequiredMixin,CreateView):
	form_class = Ledgerform
	template_name = "accounting_double_entry/ledger1_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(ledger1CreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ledger1CreateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class ledger1UpdateView(LoginRequiredMixin,UpdateView):
	model = ledger1
	form_class = Ledgerform
	template_name = "accounting_double_entry/ledger1_form.html"


	def get_context_data(self, **kwargs):
		context = super(ledger1UpdateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class ledger1DeleteView(LoginRequiredMixin,DeleteView):
	model = ledger1
	success_url = reverse_lazy("accounting_double_entry:ledgerlist")


	def get_context_data(self, **kwargs):
		context = super(ledger1DeleteView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context
	

################## Views For journal Display ###################################


class journalListView(LoginRequiredMixin,ListView):
	model = journal

	def get_queryset(self):
		return journal.objects.filter(User=self.request.user)


	def get_context_data(self, **kwargs):
		context = super(journalListView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class journalDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'journal_details'
	model = journal
	template_name = 'accounting_double_entry/journal_details.html'


	def get_context_data(self, **kwargs):
		context = super(journalDetailView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class journalCreateView(LoginRequiredMixin,CreateView):
	model = journal
	form_class  = journalForm

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(journalCreateView, self).form_valid(form)


	def get_context_data(self, **kwargs):
		context = super(journalCreateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class journalUpdateView(LoginRequiredMixin,UpdateView):
	model = journal
	form_class  = journalForm


	def get_context_data(self, **kwargs):
		context = super(journalUpdateView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context

class journalDeleteView(LoginRequiredMixin,DeleteView):
	model = journal
	success_url = reverse_lazy("accounting_double_entry:list")


	def get_context_data(self, **kwargs):
		context = super(journalDeleteView, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context
