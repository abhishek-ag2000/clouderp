from django.conf.urls import url
from django.urls import path
from ecommerce_integration import views

app_name = 'ecommerce_integration'

urlpatterns = [

	url(r'^$',views.Products_listview,name='productlist'),
	url(r'^productsubscribed/$',views.Subscribed_Products_listview,name='subscribedproductlist'),
	url(r'^product/(?P<pk>\d+)/$',views.Products_detailsview,name='productdetail'),



	url(r'^reviews/(?P<id>\d+)/delete$', views.review_delete, name='reviewdelete'),

]
