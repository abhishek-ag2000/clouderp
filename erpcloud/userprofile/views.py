from django.shortcuts import render
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import Profile
from userprofile.forms import profileform

# Create your views here.

class profiledetailview(LoginRequiredMixin,DetailView):
	context_object_name = 'profile_details'
	model = Profile
	template_name = 'userprofile/profile.html'

	def get_object(self):
		return self.request.user.profile

class profileupdateview(LoginRequiredMixin,UpdateView):
	model = Profile
	form_class = profileform
	template_name = 'userprofile/profile_form.html'

	def get_object(self):
		return self.request.user.profile


	def get_context_data(self, **kwargs):
		context = super(profileupdateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		return context