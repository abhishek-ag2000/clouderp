from django.conf.urls import url,include
from company import views
from django.urls import path

app_name = 'company'

urlpatterns = [
######################### Company Urls ################################################
    url(r'^$',views.companyListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.companyDetailView.as_view(),name='Dashboard'),
    url(r'^create/$',views.companyCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.companyUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.companyDeleteView.as_view(),name='delete'),

	
    url(r'^selectdate/$',views.selectdaterangecreate.as_view(),name='select'),
    url(r'^selectdateupdate/(?P<pk>\d+)/$',views.selectdaterange.as_view(),name='dateupdate'),
	
]