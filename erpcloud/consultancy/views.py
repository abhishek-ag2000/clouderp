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

	def get_queryset(self):
		return consultancy.objects.all().order_by('-id')


@login_required
def consultancy_detail(request, pk):
	consultancy_details = get_object_or_404(consultancy, pk=pk)
	comments = Answer.objects.filter(Questions=consultancy_details).order_by('-id')

	if request.method == "POST":
		Answer_form = Answerform(request.POST or None)
		if Answer_form.is_valid():
			text = request.POST.get('text')
			answer = Answer.objects.create(Questions=consultancy_details, User=request.user, text=text)
			answer.save()
			return HttpResponseRedirect(consultancy_details.get_absolute_url())

	context = {
		'consultancy_details' : consultancy_details,
		'comments' : comments,	
	}

	return render(request, 'consultancy/consultancy_details.html', context)



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


