from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView,TemplateView
from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from blog.models import Blog
from django.db.models import Count
from company.models import company
from django.shortcuts import get_object_or_404
from accounting_double_entry.models import selectdatefield
from consultancy.models import consultancy,Answer
from django.db.models import Count, Value
from django.db.models.functions import Coalesce 
from userprofile.models import Profile
from ecommerce_integration.models import coupon, Product, Services, API
from todogst.models import Todo
from userprofile.models import Profile, Product_activation



 
class HomePage(ListView):
	template_name = "clouderp/index.html"

	def get_queryset(self):
		return Blog.objects.all().annotate(num_submissions=Count('likes')).order_by('-num_submissions')[:4]

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("ecommerce_integration:productlist"))
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(HomePage, self).get_context_data(**kwargs) 
		context['total_consultancies'] = consultancy.objects.aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']
		context['Bussiness_users'] = Profile.objects.filter(user_type__icontains='Bussiness User').aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']
		context['Professional_users'] = Profile.objects.filter(user_type__icontains='Professional').aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']
		context['Products'] = Product.objects.all()
		context['Products_count'] = Product.objects.aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']

		return context

class base(TemplateView):
	template_name = "clouderp/base.html"

	def get_context_data(self, **kwargs):
		context = super(base, self).get_context_data(**kwargs) 
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		context['Todos'] = Todo.objects.filter(User=request.user, complete=False)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']
		context['Products'] = Product_activation.objects.filter(User=self.request.user,id=1, activate=True)
		return context



def custom_404(request):
	return render(request,'404.html')

def custom_500(request):
	return render(request,'505.html')