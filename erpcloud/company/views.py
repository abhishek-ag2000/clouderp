from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from company.models import company
from ecommerce_integration.models import coupon, Product, Product_review, Services, API
from userprofile.models import Profile, Product_activation
from company.forms import companyform
from django.shortcuts import redirect
from todogst.models import Todo
from accounting_double_entry.models import selectdatefield
from accounting_double_entry.forms import DateRangeForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase,Sales,Stock_Total,Stock_Total_sales
from django.db.models.functions import Coalesce
from django.db.models import Value, Sum, Count, F, ExpressionWrapper, Subquery, OuterRef, FloatField
from django.db.models.fields import DecimalField
from django.db.models.functions import Coalesce 
from django.core.exceptions import PermissionDenied

# Create your views here.

class ProductExistsRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if Product_activation.objects.filter(User= request.user, product__id = 1, activate=True):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class companyListView(ProductExistsRequiredMixin,LoginRequiredMixin,ListView):
	model = company
	paginate_by = 10

	def get_queryset(self):
		return company.objects.filter(User=self.request.user).order_by('id')

	def get_context_data(self, **kwargs):
		context = super(companyListView, self).get_context_data(**kwargs)
		context['selectdates'] = selectdatefield.objects.filter(User=self.request.user)
		context['Products'] = Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']


		# Capital Account
		qs = company.objects.filter(User= self.request.user)
		qs = qs.annotate(
			capital = Subquery(
				group1.objects.filter(User=self.request.user, Company=OuterRef('pk'), Master__group_Name__icontains='Capital A/c'
					).values(
						'Company'
					).annotate(
						closing = Sum('ledgergroups__Closing_balance')
					).values('closing'),
				output_field=FloatField()
				),
			capital_ledger = Subquery(
				ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'), group1_Name__group_Name__icontains='Capital A/c'
					).values(
						'Company'
					).annotate(
						closing_ledger = Sum('Closing_balance')
					).values('closing_ledger'),
				output_field=FloatField()
				)
			)
		qs1 = qs.aggregate(the_sum=Coalesce(Sum('capital'), Value(0)))['the_sum']
		qs2 = qs.aggregate(the_sum=Coalesce(Sum('capital_ledger'), Value(0)))['the_sum']

		total_cacb = qs1 + qs2

		# Current Assets

		ca = company.objects.filter(User= self.request.user)
		ca = ca.annotate(
			current = Subquery(
				group1.objects.filter(User=self.request.user, Company=OuterRef('pk'), Master__group_Name__icontains='Current Assets'
					).values(
						'Company'
					).annotate(
						closing = Sum('ledgergroups__Closing_balance')
					).values('closing'),
				output_field=FloatField()
				),
			current_ledger = Subquery(
				ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'), group1_Name__group_Name__icontains='Current Assets'
					).values(
						'Company'
					).annotate(
						closing_ledger = Sum('Closing_balance')
					).values('closing_ledger'),
				output_field=FloatField()
				)
			)
		ca1 = ca.aggregate(the_sum=Coalesce(Sum('current'), Value(0)))['the_sum']
		ca2 = ca.aggregate(the_sum=Coalesce(Sum('current_ledger'), Value(0)))['the_sum']

		total_current_asset = ca1 + ca2

		# Fixed Asset

		fa = company.objects.filter(User= self.request.user)
		fa = fa.annotate(
			fixed = Subquery(
				group1.objects.filter(User=self.request.user, Company= OuterRef('pk'), Master__group_Name__icontains='Fixed Assets'
					).values(
						'Company'
					).annotate(
						closing = Sum('ledgergroups__Closing_balance')
					).values('closing'),
				output_field=FloatField()
				),
			fixed_ledger = Subquery(
				ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'), group1_Name__group_Name__icontains='Fixed Assets'
					).values(
						'Company'
					).annotate(
						closing_ledger = Sum('Closing_balance')
					).values('closing_ledger'),
				output_field=FloatField()
				)
			)
		fa1 = fa.aggregate(the_sum=Coalesce(Sum('fixed'), Value(0)))['the_sum']
		fa2 = fa.aggregate(the_sum=Coalesce(Sum('fixed_ledger'), Value(0)))['the_sum']

		total_fixed_asset = fa1 + fa2

		Assets = total_current_asset + total_fixed_asset

		# # Profit & Loss A/c
		# pl = company.objects.filter(User= self.request.user)
		# pl = pl.annotate(
		# 	purchase_sum = Subquery(
		# 		ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'),group1_Name__group_Name__icontains='Purchase Accounts'
		# 			).values(
		# 					'Company'
		# 			).annotate(
		# 					closing_ledger_purchase = Sum('Closing_balance')
		# 			).values('closing_ledger_purchase'),
		# 		output_field=FloatField()
		# 		),
		# 	directexp_sum = Subquery(
		# 		ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'),group1_Name__group_Name__icontains='Direct Expenses'
		# 			).values(
		# 					'Company'
		# 			).annotate(
		# 					closing_ledger_directexp = Sum('Closing_balance')
		# 			).values('closing_ledger_directexp'),
		# 		output_field=FloatField()
		# 		),
		# 	directinc_sum = Subquery(
		# 		ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'),group1_Name__group_Name__icontains='Direct Incomes'
		# 			).values(
		# 					'Company'
		# 			).annotate(
		# 					closing_ledger_directinc = Sum('Closing_balance')
		# 			).values('closing_ledger_directinc'),
		# 		output_field=FloatField()
		# 		),
		# 	sales_sum = Subquery(
		# 		ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'),group1_Name__group_Name__icontains='Sales Account'
		# 			).values(
		# 					'Company'
		# 			).annotate(
		# 					closing_ledger_sales = Sum('Closing_balance')
		# 			).values('closing_ledger_sales'),
		# 		output_field=FloatField()
		# 		),
		# 	indirectexp_sum = Subquery(
		# 		ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'),group1_Name__group_Name__icontains='Indirect Expense'
		# 			).values(
		# 					'Company'
		# 			).annotate(
		# 					closing_ledger_indirectexp = Sum('Closing_balance')
		# 			).values('closing_ledger_indirectexp'),
		# 		output_field=FloatField()
		# 		),
		# 	indirectinc_sum = Subquery(
		# 		ledger1.objects.filter(User=self.request.user, Company=OuterRef('pk'),group1_Name__group_Name__icontains='Indirect Income'
		# 			).values(
		# 					'Company'
		# 			).annotate(
		# 					closing_ledger_indirectinc = Sum('Closing_balance')
		# 			).values('closing_ledger_indirectinc'),
		# 		output_field=FloatField()
		# 		),
		# 		)

		# ldc = pl.aggregate(the_sum=Coalesce(Sum('purchase_sum'), Value(0)))['the_sum']
		# lddt = pl.aggregate(the_sum=Coalesce(Sum('directexp_sum'), Value(0)))['the_sum']
		# lddi = pl.aggregate(the_sum=Coalesce(Sum('directinc_sum'), Value(0)))['the_sum']
		# ldsc = pl.aggregate(the_sum=Coalesce(Sum('sales_sum'), Value(0)))['the_sum']
		# ldse = pl.aggregate(the_sum=Coalesce(Sum('indirectexp_sum'), Value(0)))['the_sum']
		# ldsi = pl.aggregate(the_sum=Coalesce(Sum('indirectinc_sum'), Value(0)))['the_sum']

		# # Closing Stock

		

		# if  lddi < 0 and lddt < 0:
		# 	gp = abs(ldsc) + abs(qs2) + abs(lddt) - abs(ldc) - abs(lddi)
		# elif lddt < 0:
		# 	gp = abs(ldsc) + abs(qs2) + abs(lddi) + abs(lddt) - abs(ldc)
		# elif lddi < 0:
		# 	gp = abs(ldsc) + abs(qs2) - abs(lddi) - abs(ldc) - abs(lddt)
		# else:	
		# 	gp = abs(ldsc) + abs(qs2) + abs(lddi) - abs(ldc) - abs(lddt)



		# if gp >=0:
		# 	if ldsi < 0 and ldse < 0:
		# 		np = (gp) + abs(ldse) - abs(ldsi)
		# 	elif ldse < 0:
		# 		np = (gp) + abs(ldsi) + abs(ldse)
		# 	elif ldsi < 0:
		# 		np = (gp) - abs(ldsi) - abs(ldse)
		# 	else:
		# 		np = (gp) + abs(ldsi) - abs(ldse)
		# else:
		# 	if ldsi < 0 and ldse < 0:
		# 		np = abs(ldse) - abs(ldsi) - abs(gp) 
		# 	elif ldsi < 0:
		# 		np = abs(ldsi) + abs(ldse) + abs(gp)
		# 	elif ldse < 0:
		# 		np = abs(ldsi) + abs(ldse) - abs(gp)
		# 	else:
		# 		np = abs(ldsi) - abs(ldse) - abs(gp)


		context['capital'] = total_cacb
		context['Assets'] = Assets
		return context

class companyDetailView(ProductExistsRequiredMixin,LoginRequiredMixin,DetailView):
	context_object_name = 'company_details'
	model = company
	template_name = 'company/Dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(companyDetailView, self).get_context_data(**kwargs)
		context['todo_list'] = Todo.objects.filter(User=self.request.user)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		context['Products'] = Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True)
		return context


class companyCreateView(ProductExistsRequiredMixin,LoginRequiredMixin,CreateView):
	form_class  = companyform
	template_name = "company/company_form.html"

	def get_success_url(self,**kwargs):
		return reverse('company:list')

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(companyCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(companyCreateView, self).get_context_data(**kwargs)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Products'] = Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum'] 
		return context


class companyUpdateView(ProductExistsRequiredMixin,LoginRequiredMixin,UpdateView):
	model = company
	form_class  = companyform
	template_name = "company/company_form.html"

	def get_success_url(self,**kwargs):
		return reverse('company:list')

	def get_context_data(self, **kwargs):
		context = super(companyUpdateView, self).get_context_data(**kwargs)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Products'] = Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum'] 
		return context

class companyDeleteView(ProductExistsRequiredMixin,LoginRequiredMixin,DeleteView):
	model = company
	success_url = reverse_lazy("company:list")

	def get_success_url(self,**kwargs):
		return reverse('company:list')

	def get_context_data(self, **kwargs):
		context = super(companyDeleteView, self).get_context_data(**kwargs)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum'] 
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['Products'] = Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True)
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
