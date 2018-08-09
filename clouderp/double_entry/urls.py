from django.conf.urls import url
from double_entry import views

app_name = 'double_entry'

urlpatterns = [
    url(r'^$',views.group1ListView.as_view(),name='grouplist'),
    url(r'^(?P<pk>\d+)/$',views.group1DetailView.as_view(),name='groupdetail'),
    url(r'^groupcreate/$',views.group1CreateView.as_view(),name='groupcreate'),
    url(r'^groupupdate/(?P<pk>\d+)/$',views.group1UpdateView.as_view(),name='groupupdate'),
    url(r'^groupdelete/(?P<pk>\d+)/$',views.group1DeleteView.as_view(),name='groupdelete'),
]