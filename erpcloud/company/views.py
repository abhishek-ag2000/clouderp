from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from company.models import company
from company.forms import companyform
from django.shortcuts import redirect
from todogst.models import Todo
from accounting_double_entry.models import selectdatefield
from accounting_double_entry.forms import DateRangeForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from django.db.models.functions import Coalesce
from django.db.models import Value, Sum, F, ExpressionWrapper
from django.db.models.fields import DecimalField
# Create your views here.


class companyListView(LoginRequiredMixin,ListView):
	model = company
	paginate_by = 10

	def get_queryset(self):
		return company.objects.filter(User=self.request.user).order_by('id')

	def get_context_data(self, **kwargs):
		context = super(companyListView, self).get_context_data(**kwargs)
		context['selectdates'] = selectdatefield.objects.filter(User=self.request.user)
		return context

class companyDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'company_details'
	model = company
	template_name = 'company/Dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(companyDetailView, self).get_context_data(**kwargs)
		context['todo_list'] = Todo.objects.filter(User=self.request.user).order_by('-id')
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context


class companyCreateView(LoginRequiredMixin,CreateView):
	form_class  = companyform
	template_name = "company/company_form.html"

	def get_success_url(self,**kwargs):
		return reverse('company:list')

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(companyCreateView, self).form_valid(form)


class companyUpdateView(LoginRequiredMixin,UpdateView):
	model = company
	form_class  = companyform
	template_name = "company/company_form.html"

	def get_success_url(self,**kwargs):
		return reverse('company:list')

class companyDeleteView(LoginRequiredMixin,DeleteView):
	model = company
	success_url = reverse_lazy("company:list")

	def get_success_url(self,**kwargs):
		return reverse('company:list')

	def get_context_data(self, **kwargs):
		context = super(companyDeleteView, self).get_context_data(**kwargs) 
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context





# class Todolist(LoginRequiredMixin,ListView):
# 	model = Todo
# 	paginate_by = 10

# 	def get_queryset(self):
# 		return Todo.objects.filter(User=self.request.user)

# 	def post(self, request, *args, **kwargs):
# 		return TodoUpdate.as_view()(request)

# class TodoCreate(LoginRequiredMixin,CreateView):
# 	form_class = Todoform
# 	template_name = 'company/todo_form.html'

# 	def form_valid(self, form):
# 		form.instance.User = self.request.user
# 		return super(TodoCreate, self).form_valid(form)


# class TodoUpdate(LoginRequiredMixin,UpdateView):
# 	model = Todo
# 	form_class = Todoform
# 	template_name = 'company/todo_form.html'


# class TodoDelete(LoginRequiredMixin,UpdateView):
# 	model = Todo
# 	success_url = reverse_lazy("company:Todolist")

# 	def get(self, *args, **kwargs):
# 		return self.delete(*args, **kwargs)

# class Tododelete(LoginRequiredMixin,DeleteView):
# 	model = Todo
# 	success_url = reverse_lazy("company:Dashboard")
# 	template_name = 'company/todo_confirm_delete.html'

# 	def get(self, *args, **kwargs):
# 		return self.delete(*args, **kwargs)


# def deleteCompleted(request):
# 	Todo.objects.filter(complete__exact=True).delete()

# 	return redirect('company:Dashboard')
