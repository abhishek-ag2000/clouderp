from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from company.models import company
from company.forms import companyform
# Create your views here.


class companyListView(LoginRequiredMixin,ListView):
	model = company

	def get_queryset(self):
		return company.objects.filter(User=self.request.user)

class companyDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'company_details'
	model = company
	template_name = 'company/Dashboard.html'


class companyCreateView(LoginRequiredMixin,CreateView):
	form_class  = companyform
	template_name = "company/company_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(companyCreateView, self).form_valid(form)


class companyUpdateView(LoginRequiredMixin,UpdateView):
	model = company
	form_class  = companyform
	template_name = "company/company_form.html"

class companyDeleteView(LoginRequiredMixin,DeleteView):
	model = company
	success_url = reverse_lazy("company:list")