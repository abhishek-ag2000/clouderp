from django.conf.urls import url
from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
	

	url(r'^$',views.profiledetailview.as_view(),name='profiledetail'),
    url(r'^userprofile/(?P<pk>\d+)/$',views.specific_profile,name='specific_profile'),
	url(r'^profileupdate/$',views.profileupdateview.as_view(),name='profileupdate'),

	path('activate/<product_activation_id>', views.activate_subscriptions, name='activate'),
	path('deactivate/<product_activation_id>', views.deactivate_subscriptions, name='deactivate'),

	path('activate/product/<product_activation_id>', views.activate_subscriptions_productlist, name='activate_product'),
	path('deactivate/product/<product_activation_id>', views.deactivate_subscriptions_productlist, name='deactivate_product'),
]