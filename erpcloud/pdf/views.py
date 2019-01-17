from django.shortcuts import render
from pdf.utils import render_to_pdf
from django.http import HttpResponse
from django.views.generic import (View,ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from stockkeeping.models import Stockgroup,Simpleunits,Compoundunits,Stockdata,Purchase,Sales,Stock_Total,Stock_Total_sales
from company.models import company
from accounting_double_entry.models import group1,ledger1,journal,selectdatefield
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Generate_Purchase_PDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('purchase_details_pdf.html')

		purchase_details = get_object_or_404(Purchase, pk=self.kwargs['pk2'])
		stocklist = Stock_Total.objects.filter(purchases=purchase_details.pk)

		context = {

			"company_details"          : get_object_or_404(company, pk=self.kwargs['pk1']),
			"selectdatefield_details"  : get_object_or_404(selectdatefield, pk=self.kwargs['pk3']),
			"purchase_details"         : purchase_details,
			"stocklist" 			   : stocklist,
		}
		html = template.render(context)
		pdf = render_to_pdf('purchase_details_pdf.html', context)
		if pdf:
			return HttpResponse(pdf, content_type='application/pdf')
		return HttpResponse("PDF Not Found")



class Generate_Sales_PDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('sales_details_pdf.html')

		sales_details = get_object_or_404(Sales, pk=self.kwargs['pk2'])
		stocklist  = Stock_Total_sales.objects.filter(sales=sales_details.pk)

		context = {

			"company_details"          : get_object_or_404(company, pk=self.kwargs['pk1']),
			"selectdatefield_details"  : get_object_or_404(selectdatefield, pk=self.kwargs['pk3']),
			"sales_details"            : sales_details,
			"stocklist" 			   : stocklist,
		}
		html = template.render(context)
		pdf = render_to_pdf('sales_details_pdf.html', context)
		if pdf:
			return HttpResponse(pdf, content_type='application/pdf')
		return HttpResponse("PDF Not Found")


class Sales_detailsview_print(LoginRequiredMixin,DetailView):
	context_object_name = 'sales_details'
	model = Sales
	template_name = 'sale_details_print.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		sales = get_object_or_404(Sales, pk=pk2)
		return sales


	def get_context_data(self, **kwargs):
		context = super(Sales_detailsview_print, self).get_context_data(**kwargs) 
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		sales_details = get_object_or_404(Sales, pk=self.kwargs['pk2'])
		qsjb  = Stock_Total_sales.objects.filter(sales=sales_details.pk)
		context['stocklist'] = qsjb
		return context


class Purchase_detailsview_print(LoginRequiredMixin,DetailView):
	context_object_name = 'purchase_details'
	model = Purchase
	template_name = 'purchase_details_print.html'

	def get_object(self):
		pk1 = self.kwargs['pk1']
		pk2 = self.kwargs['pk2']
		pk3 = self.kwargs['pk3']
		get_object_or_404(selectdatefield, pk=pk3)
		get_object_or_404(company, pk=pk1)
		purchase = get_object_or_404(Purchase, pk=pk2)
		return purchase


	def get_context_data(self, **kwargs):
		context = super(Purchase_detailsview_print, self).get_context_data(**kwargs) 
		company_details = get_object_or_404(company, pk=self.kwargs['pk1'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		purchase_details = get_object_or_404(Purchase, pk=self.kwargs['pk2'])
		qsob  = Stock_Total.objects.filter(purchases=purchase_details.pk)
		context['stocklist'] = qsob
		
		return context