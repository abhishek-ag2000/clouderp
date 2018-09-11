from django.conf.urls import url
from accounting_double_entry import views

app_name = 'accounting_double_entry'

urlpatterns = [

####### Groups Urls ########################################

    url(r'^$',views.group1ListView.as_view(),name='grouplist'),
    url(r'^(?P<pk>\d+)/$',views.group1DetailView.as_view(),name='groupdetail'),
    url(r'^groupcreate/$',views.group1CreateView.as_view(),name='groupcreate'),
    url(r'^groupupdate/(?P<pk>\d+)/$',views.group1UpdateView.as_view(),name='groupupdate'),
    url(r'^groupdelete/(?P<pk>\d+)/$',views.group1DeleteView.as_view(),name='groupdelete'),

####### Ledger Urls ########################################

    url(r'^ledgerlist/$',views.ledger1ListView.as_view(),name='ledgerlist'),
    url(r'^ledgerlist/(?P<pk>\d+)/$',views.ledger1DetailView.as_view(),name='ledgerdetail'),
    url(r'^ledgercreate/$',views.ledger1CreateView.as_view(),name='ledgercreate'),
    url(r'^ledgerupdate/(?P<pk>\d+)/$',views.ledger1UpdateView.as_view(),name='ledgerupdate'),
    url(r'^ledgerdelete/(?P<pk>\d+)/$',views.ledger1DeleteView.as_view(),name='ledgerdelete'),


####### Journal Urls ########################################  

    url(r'^journallist/$',views.journalListView.as_view(),name='list'),
    url(r'^journallist/(?P<pk>\d+)/$',views.journalDetailView.as_view(),name='detail'),
    url(r'^journal/create/$',views.journalCreateView.as_view(),name='create'),
    url(r'^journal/update/(?P<pk>\d+)/$',views.journalUpdateView.as_view(),name='update'),
    url(r'^journal/delete/(?P<pk>\d+)/$',views.journalDeleteView.as_view(),name='delete'),




   
    
]