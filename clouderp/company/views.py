from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from company.models import company,companyowner
# Create your views here.


class companyListView(LoginRequiredMixin,ListView):
	model = company

	def get_queryset(self):
		return company.objects.all()

class companyDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'company_details'
	model = company
	template_name = 'company/Dashboard.html'


class companyCreateView(LoginRequiredMixin,CreateView):
	fields = "__all__"
	model = company

class companyUpdateView(LoginRequiredMixin,UpdateView):
	fields = "__all__"
	model = company

class companyDeleteView(LoginRequiredMixin,DeleteView):
	model = company
	success_url = reverse_lazy("company:list")