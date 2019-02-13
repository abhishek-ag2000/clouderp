from django.shortcuts import render, redirect
from django.views.generic import (View,ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ecommerce_integration.models import coupon, Product, Product_review, Services, API
from todogst.models import Todo
from ecommerce_cart.models import Order
from django.db.models.functions import Coalesce
from django.db.models import Value, Sum, Count, F, ExpressionWrapper, Subquery, OuterRef, FloatField
from ecommerce_integration.forms import Product_review_form
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from userprofile.models import Profile, Product_activation
# Create your views here.


@login_required
def Products_listview(request):
	products_list = Product.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(products_list, 9)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
	current_order_products = []
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_products = [product.product for product in user_order_items]


	context = {
		'products_list'			: products_list,
		'users'					: users,
		'current_order_products': current_order_products,
		'Products'			 	: Product_activation.objects.filter(User=request.user, product__id=1, activate=True),
		'Todos'				 	: Todo.objects.filter(User=request.user, complete=False),
		'Todos_total'		 	: Todo.objects.filter(User=request.user, complete=False).aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']
	}

	return render(request, "products/product_list.html", context)

@login_required
def Subscribed_Products_listview(request):
	products_list = Product.objects.all()
	Todos = Todo.objects.filter(User=request.user, complete=False)
	Todos_total = Todos.aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']

	context = {
		'products': products_list,
		'Products'	: Product_activation.objects.filter(User=request.user,product__id = 1, activate=True),
		'Todos'				 	: Todos,
		'Todos_total'		 	: Todos_total,
	}

	return render(request, "products/subscribed_product.html", context)


@login_required
def Products_detailsview(request, pk):
	products_details = get_object_or_404(Product, pk=pk)
	reviews = Product_review.objects.filter(reviews=products_details.pk).order_by('-id')

	if request.method == "POST":
		Productreview_form = Product_review_form(request.POST or None)
		if Productreview_form.is_valid():
			name = request.POST.get('name')
			e_mail = request.POST.get('e_mail')
			text = request.POST.get('text')
			answer = Product_review.objects.create(reviews=products_details, User=request.user, name=name, e_mail=e_mail, text=text)
			answer.save()
			return HttpResponseRedirect(products_details.get_absolute_url())
	else:
		Productreview_form = Product_review_form()

	filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
	current_order_products = []
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_products = [product.product for product in user_order_items]

	Todos = Todo.objects.filter(User=request.user, complete=False)
	Todos_total = Todos.aggregate(the_sum=Coalesce(Count('id'), Value(0)))['the_sum']


	context = {

		'products_details'   	: products_details,
		'reviews'		   	 	: reviews,
		'Productreview_form' 	: Productreview_form,
		'Todos'				 	: Todos,
		'Todos_total'		 	: Todos_total,
		'current_order_products': current_order_products,
		'Products'				: Product_activation.objects.filter(User=request.user,product__id = 1, activate=True),


	}

	return render(request, 'products/product_details.html', context)


def review_delete(request,id):
	data = dict()
	review = get_object_or_404(Product_review,id=id)
	if request.method == "POST":
		review.delete()
		data['form_is_valid'] = True
		reviews = Product_review.objects.all().order_by('-id')
		data['comments'] = render_to_string('products/reviews.html',{'reviews':reviews})
	else:
		context = {'review':review}
		data['html_form'] = render_to_string('products/reviews_delete.html',context,request=request)

	return JsonResponse(data)


