from django.shortcuts import render, redirect
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import Profile, Product_activation
from userprofile.forms import profileform
from django.shortcuts import get_object_or_404
from company.models import company
from django.shortcuts import get_object_or_404
from todogst.models import Todo
from django.db.models.functions import Coalesce 
from django.db.models import Count, Value
from ecommerce_integration.models import coupon, Product, Product_review, Services, API
from django.contrib.auth.decorators import login_required



# Create your views here.

class profiledetailview(LoginRequiredMixin,DetailView):
	context_object_name = 'profile_details'
	model = Profile
	template_name = 'userprofile/profile.html'

	def get_object(self):
		return self.request.user.profile

	def get_context_data(self, **kwargs):
		context = super(profiledetailview, self).get_context_data(**kwargs)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Products'] = Product_activation.objects.filter(User=self.request.user,id=1, activate=True)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum'] 
		return context

class profileupdateview(LoginRequiredMixin,UpdateView):
	model = Profile
	form_class = profileform
	template_name = 'userprofile/profile_form.html'

	def get_object(self):
		return self.request.user.profile


	def get_context_data(self, **kwargs):
		context = super(profileupdateview, self).get_context_data(**kwargs) 
		context['profile_details'] = Profile.objects.all()
		context['Products'] = Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True)
		context['Todos'] = Todo.objects.filter(User=self.request.user, complete=False)
		context['Todos_total'] = context['Todos'].aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum'] 
		return context

def specific_profile(request, pk):
	profile_details = get_object_or_404(Profile, pk=pk)

	context = {
		'profile_details' : profile_details,
		'Products'		  : Product_activation.objects.filter(User=self.request.user,product__id = 1, activate=True),
		'Todos'			  : Todo.objects.filter(User=request.user, complete=False),
		'Todos_total' 	  : Todo.objects.filter(User=request.user, complete=False).aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum'] 
	}
	return render(request, 'userprofile/specific_profile.html', context)


@login_required
def activate_subscriptions(request, product_activation_id):
    product = Product_activation.objects.get(pk=product_activation_id)
    product.activate = True
    product.deactivate = False
    product.save()

    return redirect('ecommerce_integration:subscribedproductlist')

@login_required
def activate_subscriptions_productlist(request, product_activation_id):
    product = Product_activation.objects.get(pk=product_activation_id)
    product.activate = True
    product.deactivate = False
    product.save()

    return redirect('ecommerce_integration:productlist')


@login_required
def deactivate_subscriptions(request, product_activation_id):
    product = Product_activation.objects.get(pk=product_activation_id)
    product.deactivate = True
    product.activate = False
    product.save()

    return redirect('ecommerce_integration:subscribedproductlist')


@login_required
def deactivate_subscriptions_productlist(request, product_activation_id):
    product = Product_activation.objects.get(pk=product_activation_id)
    product.deactivate = True
    product.activate = False
    product.save()

    return redirect('ecommerce_integration:productlist')