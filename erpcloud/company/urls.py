from django.conf.urls import url
from company import views

app_name = 'company'

urlpatterns = [
    url(r'^$',views.companyListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.companyDetailView.as_view(),name='Dashboard'),
    url(r'^create/$',views.companyCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.companyUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.companyDeleteView.as_view(),name='delete')
]