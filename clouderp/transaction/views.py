from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from transaction.models import ledger1,transaction,journal
from transaction.forms import transactionForm,transactionFormSet,journalForm,journalFormSet

# Create your views here.

class ledger1ListView(LoginRequiredMixin,ListView):
	model = ledger1

	def get_queryset(self):
		return ledger1.objects.all()

class ledger1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'ledger1_details'
	model = ledger1
	template_name = 'transaction/ledger1_details.html'

class ledger1CreateView(LoginRequiredMixin,CreateView):
	fields = "__all__"
	model = ledger1

class ledger1UpdateView(LoginRequiredMixin,UpdateView):
	fields = "__all__"
	model = ledger1

class ledger1DeleteView(LoginRequiredMixin,DeleteView):
	model = ledger1
	


class transactionCreateView(LoginRequiredMixin,CreateView):
	model = transaction
	fields = ['Creation_Date']

	def get_context_data(self, **kwargs):
		data = super(transactionCreateView,self).get_context_data(**kwargs)
		if self.request.POST:
			data['transactions'] = transactionFormSet(self.request.POST)
		else:
			data['transactions'] = transactionFormSet()
		return data

	def form_valid(self,form):
		context = self.get_context_data()
		transactions = context['transactions']
		with transaction.atomic():
			self.object = form.save()

			if transactions.is_valid():
				transactions.instance = self.object
				transactions.save()
		return super(transactionCreateView,self).form_valid(form)

class journalCreateView(LoginRequiredMixin,CreateView):
	model = journal
	fields = ['Creation_Date']

	def get_context_data(self, **kwargs):
		data = super(journalCreateView,self).get_context_data(**kwargs)
		if self.request.POST:
			data['journals'] = journalFormSet(self.request.POST)
		else:
			data['journals'] = journalFormSet()
		return data

	def form_valid(self,form):
		context = self.get_context_data()
		journals = context['journals']
		with transaction.atomic():
			self.object = form.save()

			if transactions.is_valid():
				journals.instance = self.object
				journals.save()
		return super(journalCreateView,self).form_valid(form)


