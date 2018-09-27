from django.shortcuts import render
from consultancy.models import consultancy,Answer
from consultancy.forms import consultancyform,Answerform
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.


class consultancyListView(ListView):
	model = consultancy
	paginate_by = 6

	def get_queryset(self):
		return consultancy.objects.all().order_by('-id')





class myconsultancyListView(LoginRequiredMixin,ListView):
	model = consultancy
	paginate_by = 6

	def get_queryset(self):
		return consultancy.objects.filter(User=self.request.user).order_by('-id')

	def get_template_names(self):
		if True:  
			return ['consultancy/myconsultancy.html']
		else:
			return ['consultancy/consultancy_list.html']




@login_required
def consultancy_detail(request, pk):
	consultancy_details = get_object_or_404(consultancy, pk=pk)
	comments = Answer.objects.filter(Questions=consultancy_details).order_by('-id')

	is_liked = False
	if consultancy_details.like.filter(pk=request.user.id).exists():
		is_liked = True

	if request.method == "POST":
		Answer_form = Answerform(request.POST or None)
		if Answer_form.is_valid():
			text = request.POST.get('text')
			answer = Answer.objects.create(Questions=consultancy_details, User=request.user, text=text)
			answer.save()
			return HttpResponseRedirect(consultancy_details.get_absolute_url())
	else:
		Answer_form = Answerform()

	context = {
		'consultancy_details' : consultancy_details,
		'comments' : comments,	
		'is_liked' : is_liked,
		'total_like' : consultancy_details.total_like(),
		'Answer_form' : Answer_form,
	}

	return render(request, 'consultancy/consultancy_details.html', context)


@login_required
def liked_post(request):
	consultancy_details = get_object_or_404(consultancy, pk=request.POST.get('consultancy_details_id'))
	is_liked = False
	if consultancy_details.like.filter(pk=request.user.id).exists():
		consultancy_details.like.remove(request.user)
		is_liked = False
	else:
		consultancy_details.like.add(request.user)
		is_liked = True

	return HttpResponseRedirect(consultancy_details.get_absolute_url())




class consultancycreate(LoginRequiredMixin,CreateView):
	form_class = consultancyform
	template_name = "consultancy/consultancy_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(consultancycreate, self).form_valid(form)

class consultancyupdate(LoginRequiredMixin,UpdateView):
	model = consultancy
	form_class  = consultancyform
	template_name = "consultancy/consultancy_form.html"


class consultancydelete(LoginRequiredMixin,DeleteView):
	model = consultancy
	success_url = reverse_lazy("consultancy:consultancylist")


