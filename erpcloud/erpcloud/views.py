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

 
class HomePage(ListView):
	template_name = "clouderp/index.html"
	paginate_by = 4

	def get_queryset(self):
		return Blog.objects.all().order_by('-id')

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("company:list"))
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(HomePage, self).get_context_data(**kwargs) 
		context['likes'] = Blog.objects.annotate(Count('likes')).values_list('Blog_title','likes')
		return context

class base(TemplateView):
	template_name = "clouderp/base.html"

	def get_context_data(self, **kwargs):
		context = super(base, self).get_context_data(**kwargs) 
		company_details = get_object_or_404(company, pk=self.kwargs['pk'])
		context['company_details'] = company_details
		selectdatefield_details = get_object_or_404(selectdatefield, pk=self.kwargs['pk3'])
		context['selectdatefield_details'] = selectdatefield_details
		return context



def custom_404(request):
	return render(request,'404.html')

def custom_500(request):
	return render(request,'505.html')