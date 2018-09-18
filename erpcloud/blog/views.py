from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import Blog,categories
from blog.forms import Blogform,BlogSearchForm
from django.db.models import Q
# Create your views here.



class bloglistview(LoginRequiredMixin,ListView):
	model = Blog
	
	
	def get_queryset(self):
		return Blog.objects.filter(User=self.request.user).order_by('id')

	def get_context_data(self, **kwargs):
		context = super(bloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		return context


class allbloglistview(LoginRequiredMixin,ListView):
	model = Blog
		
	def get_queryset(self):
		return Blog.objects.all().order_by('id')

	def get_context_data(self, **kwargs):
		context = super(allbloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		return context




class blogdetailsview(LoginRequiredMixin,DetailView):
	context_object_name = 'blog_details'
	model = Blog
	template_name = 'blog/blog_details.html'

class blogcreateview(LoginRequiredMixin,CreateView):
	form_class = Blogform
	template_name = 'blog/blog_form.html'

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(blogcreateview, self).form_valid(form)

class blogupdateview(LoginRequiredMixin,UpdateView):
	model = Blog
	form_class = Blogform
	template_name = 'blog/blog_form.html'


class blogdeleteview(LoginRequiredMixin,DeleteView):
	model = Blog
	success_url = reverse_lazy("blog:bloglist")


class categoryListView(LoginRequiredMixin,ListView):
	model = categories
	template_name = 'blog/blog_list.html'

	def get_queryset(self):
		return Blog.objects.order_by('-id')


class categoryDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'category_details'
	model = categories
	template_name = 'blog/category_detail.html'

	def get_context_data(self, **kwargs):
		context = super(categoryDetailView, self).get_context_data(**kwargs) 
		context['blog_list'] = Blog.objects.all()
		return context

def search(request):
	template = 'blog/blog_list.html'

	query = request.GET.get('q')

	if query:
		result = Blog.objects.filter(Q(Blog_title__icontains=query) | Q(Description__icontains=query) | Q(Category__Title__icontains=query))
	else:
		result = Blog.objects.filter(User=self.request.user).order_by('id')

	context = {
		'blog_list':result,
		'categories_list':categories.objects.all(),
	}

	return render(request, template, context)