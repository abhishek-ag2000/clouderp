from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounting_double_entry.models import group1,ledger1,journal
from accounting_double_entry.forms import journalForm,group1Form,Ledgerform
from django.db.models import Sum
from company.models import company
from django.db.models import Q



# Create your views here.
###################### Views For Group Display ############################################

class group1ListView(LoginRequiredMixin,ListView):
	model = group1

	def get_queryset(self):
		return group1.objects.filter(User=self.request.user)

class group1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'group1_details'
	model = group1
	template_name = 'accounting_double_entry/group1_details.html'


class group1CreateView(LoginRequiredMixin,CreateView):
	form_class  = group1Form
	template_name = "accounting_double_entry/group1_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(group1CreateView, self).form_valid(form)

class group1UpdateView(LoginRequiredMixin,UpdateView):
	model = group1
	form_class  = group1Form
	template_name = "accounting_double_entry/group1_form.html"

class group1DeleteView(LoginRequiredMixin,DeleteView):
	model = group1
	success_url = reverse_lazy("accounting_double_entry:grouplist")

################## Views For Ledger Display ###################################


class ledger1ListView(LoginRequiredMixin,ListView):
	model = ledger1

	def get_queryset(self):
		return ledger1.objects.filter(User=self.request.user)

class ledger1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'ledger1_details'
	model = ledger1
	template_name = 'accounting_double_entry/ledger1_details.html'

	def get_context_data(self, **kwargs):
		context = super(ledger1DetailView, self).get_context_data(**kwargs) 
		context['journal_list'] = journal.objects.all()
		context['company_list'] = company.objects.all()
		return context

class ledger1CreateView(LoginRequiredMixin,CreateView):
	form_class = Ledgerform
	template_name = "accounting_double_entry/ledger1_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(ledger1CreateView, self).form_valid(form)

class ledger1UpdateView(LoginRequiredMixin,UpdateView):
	model = ledger1
	form_class = Ledgerform
	template_name = "accounting_double_entry/ledger1_form.html"

class ledger1DeleteView(LoginRequiredMixin,DeleteView):
	model = ledger1
	success_url = reverse_lazy("accounting_double_entry:ledgerlist")
	

################## Views For journal Display ###################################


class journalListView(LoginRequiredMixin,ListView):
	model = journal

	def get_queryset(self):
		return journal.objects.filter(User=self.request.user)

class journalDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'journal_details'
	model = journal
	template_name = 'accounting_double_entry/journal_details.html'

class journalCreateView(LoginRequiredMixin,CreateView):
	model = journal
	form_class  = journalForm

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(journalCreateView, self).form_valid(form)

class journalUpdateView(LoginRequiredMixin,UpdateView):
	model = journal
	form_class  = journalForm

class journalDeleteView(LoginRequiredMixin,DeleteView):
	model = journal
	success_url = reverse_lazy("accounting_double_entry:list")
