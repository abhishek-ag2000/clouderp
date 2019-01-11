from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import Blog,categories
from blog.forms import Blogform,BlogSearchForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.contrib.auth.decorators import login_required


# Create your views here.

class viewbloglistview(LoginRequiredMixin,ListView):
	model = Blog
	paginate_by = 6

	def get_template_names(self):
		if True:  
			return ['blog/view_blogs.html']
		else:
			return ['blog/blog_list.html']

	def get_queryset(self):
		return Blog.objects.all().order_by('-blog_views')[:20]

	def get_context_data(self, **kwargs):
		context = super(viewbloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		context['categories_count'] = Blog.categories_count()
		return context

class likebloglistview(LoginRequiredMixin,ListView):
	model = Blog
	paginate_by = 6

	def get_template_names(self):
		if True:  
			return ['blog/blog_by_likes.html']
		else:
			return ['blog/blog_list.html']

	def get_queryset(self):
		return Blog.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:20]

	def get_context_data(self, **kwargs):
		context = super(likebloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		context['categories_count'] = Blog.categories_count()
		return context



class latestbloglistview(LoginRequiredMixin,ListView):
	model = Blog
	paginate_by = 6

	def get_template_names(self):
		if True:  
			return ['blog/latest_blog.html']
		else:
			return ['blog/blog_list.html']

	def get_queryset(self):
		return Blog.objects.all().order_by('-id')

	def get_context_data(self, **kwargs):
		context = super(latestbloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		context['categories_count'] = Blog.categories_count()
		return context



class bloglistview(LoginRequiredMixin,ListView):
	model = Blog
	paginate_by = 4
	
	
	def get_queryset(self):
		return Blog.objects.filter(User=self.request.user).order_by('id')

	def get_context_data(self, **kwargs):
		context = super(bloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		context['categories_count'] = Blog.categories_count()
		return context


class allbloglistview(ListView):
	model = Blog
	paginate_by = 6


	def get_template_names(self):
		if True:  
			return ['blog/all_blogs.html']
		else:
			return ['blog/blog_list.html']
		
	def get_queryset(self):
		return Blog.objects.all().order_by('id')

	def get_context_data(self, **kwargs):
		context = super(allbloglistview, self).get_context_data(**kwargs) 
		context['categories_list'] = categories.objects.all()
		context['categories_count'] = Blog.categories_count()
		return context




def post_detail(request, pk):
	blog_details = get_object_or_404(Blog, pk=pk)

	blog_details.blog_views=blog_details.blog_views + 1
	blog_details.save()	

	is_liked = False
	if blog_details.likes.filter(pk=request.user.id).exists():
		is_liked = True
	context = {
		'blog_details' : blog_details,
		'is_liked' : is_liked,
		'total_likes' : blog_details.total_likes(),
		'categories_list' : categories.objects.all(),
		'categories_count' : blog_details.categories_count(),
		
	}

	return render(request, 'blog/blog_details.html', context)
	

@login_required
def like_post(request):
	blog_details = get_object_or_404(Blog, pk=request.POST.get('blog_details_id'))
	is_liked = False
	if blog_details.likes.filter(pk=request.user.id).exists():
		blog_details.likes.remove(request.user)
		is_liked = False
	else:
		blog_details.likes.add(request.user)
		is_liked = True

	return HttpResponseRedirect(blog_details.get_absolute_url())



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
	paginate_by = 6

	def get_queryset(self):
		return Blog.objects.order_by('-id')


class categoryDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'category_details'
	model = categories
	template_name = 'blog/category_detail.html'
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super(categoryDetailView, self).get_context_data(**kwargs)
		context['blog_list'] = Blog.objects.all()
		context['categories_list'] = categories.objects.all()
		context['categories_count'] = Blog.categories_count()
		return context

def search(request):
	template = 'blog/blog_list.html'

	query = request.GET.get('q')

	if query:
		result = Blog.objects.filter(Q(Blog_title__icontains=query) | Q(Description__icontains=query) | Q(Category__Title__icontains=query))
	else:
		result = Blog.objects.all().order_by('id')

	context = {
		'blogs':result,
		'categories_l':categories.objects.all(),
	}

	return render(request, template, context)



