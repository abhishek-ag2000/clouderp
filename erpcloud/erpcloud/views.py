from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from blog.models import Blog
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

 
class HomePage(TemplateView):
	template_name = "clouderp/index.html"

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("company:list"))
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(HomePage, self).get_context_data(**kwargs) 
		qs = Blog.objects.all()
		context['blog_list'] = qs
		context['likes'] = Blog.objects.annotate(Count('likes')).values_list('Blog_title','likes')

		page = self.request.GET.get('page')

		paginator = Paginator(qs, 4)

		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		context['users'] = users

		return context



def custom_404(request):
	return render(request,'404.html')

def custom_500(request):
	return render(request,'505.html')