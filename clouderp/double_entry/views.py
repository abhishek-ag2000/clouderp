from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from double_entry.models import group1

# Create your views here.

class group1ListView(LoginRequiredMixin,ListView):
	model = group1

	def get_queryset(self):
		return group1.objects.all()

class group1DetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'group1_details'
	model = group1
	template_name = 'double_entry/group1_details.html'

class group1CreateView(LoginRequiredMixin,CreateView):
	fields = "__all__"
	model = group1

class group1UpdateView(LoginRequiredMixin,UpdateView):
	fields = "__all__"
	model = group1

class group1DeleteView(LoginRequiredMixin,DeleteView):
	model = group1
	success_url = reverse_lazy("double_entry:grouplist")


 