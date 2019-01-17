from django.conf.urls import url
from pdf import views

app_name = 'pdf'

urlpatterns = [

	url(r'^company/(?P<pk1>\d+)/purchasedetailpdf/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.Generate_Purchase_PDF.as_view(),name='purchasedetailpdf'),
	url(r'^company/(?P<pk1>\d+)/saledetailpdf/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.Generate_Sales_PDF.as_view(),name='salesdetailpdf'),

	url(r'^company/(?P<pk1>\d+)/salesdetail/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.Sales_detailsview_print.as_view(),name='salesdetailprint'),
	url(r'^company/(?P<pk1>\d+)/purchasedetail/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.Purchase_detailsview_print.as_view(),name='purchasedetailprint'),


]