from django.conf.urls import url
from transaction import views

app_name = 'transaction'

urlpatterns = [
    url(r'^$',views.ledger1ListView.as_view(),name='ledgerlist'),
    url(r'^(?P<pk>\d+)/$',views.ledger1DetailView.as_view(),name='ledgerdetail'),
    url(r'^ledgercreate/$',views.ledger1CreateView.as_view(),name='ledgercreate'),
    url(r'^ledgerupdate/(?P<pk>\d+)/$',views.ledger1UpdateView.as_view(),name='ledgerupdate'),
    url(r'^ledgerdelete/(?P<pk>\d+)/$',views.ledger1DeleteView.as_view(),name='ledgerdelete'),

   
    url(r'^transactioncreate/$',views.transactionCreateView.as_view(),name='transactioncreate'),
  

]