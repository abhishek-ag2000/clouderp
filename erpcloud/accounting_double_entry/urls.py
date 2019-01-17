from django.conf.urls import url
from accounting_double_entry import views

app_name = 'accounting_double_entry'

urlpatterns = [

####### Groups Urls ########################################

    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/grouplist$',views.group1ListView.as_view(),name='grouplist'),    
    url(r'^company/(?P<pk1>\d+)/groupdetail/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.group1DetailView.as_view(),name='groupdetail'),
    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/groupcreate/$',views.group1CreateView.as_view(),name='groupcreate'),
    url(r'^company/(?P<pk1>\d+)/groupupdate/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.group1UpdateView.as_view(),name='groupupdate'),
    url(r'^company/(?P<pk>\d+)/groupdelete/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.group1DeleteView.as_view(),name='groupdelete'),




####### Ledger Monthly Url ########################################

    url(r'^company/(?P<pk>\d+)/ledgermonthly/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.ledger_monthly_detail_view,name='ledgerdetailmonthly'),

####### Ledger Urls ########################################


    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/ledgerlist/$',views.ledger1ListView.as_view(),name='ledgerlist'),
    url(r'^company/(?P<pk>\d+)/ledgerdetail/(?P<pk2>\d+)/date/(?P<pk3>\d+)/$',views.ledger1_detail_view,name='ledgerdetail'),
    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/ledgercreate/$',views.ledger1CreateView.as_view(),name='ledgercreate'),
    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/ledgerupdate/(?P<pk2>\d+)/$',views.ledger1UpdateView.as_view(),name='ledgerupdate'),
    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/ledgerdelete/(?P<pk2>\d+)/$',views.ledger1DeleteView.as_view(),name='ledgerdelete'),

####### Journal Register Urls ########################################  

     url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/journalregister/$',views.Journal_Register_view.as_view(),name='journalregister'),

####### Journal Urls ########################################  

    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/journallist/$',views.journalListView.as_view(),name='list'),
    url(r'^company/(?P<pk1>\d+)/date/(?P<pk3>\d+)/journallist/(?P<pk2>\d+)/$',views.journal_detail,name='detail'),
    url(r'^company/(?P<pk>\d+)/date/(?P<pk3>\d+)/journal/create/$',views.journalCreateView.as_view(),name='create'),
    url(r'^company/(?P<pk1>\d+)/date/(?P<pk3>\d+)/journal/update/(?P<pk2>\d+)/$',views.journalUpdateView.as_view(),name='update'),
    url(r'^company/(?P<pk1>\d+)/date/(?P<pk3>\d+)/journal/delete/(?P<pk2>\d+)/$',views.journalDeleteView.as_view(),name='delete'),


####### Daterange Urls ########################################  
  
    url(r'^daterangecreate/$',views.datecreateview.as_view(),name='datecreate'),
    url(r'^daterangeupdate/(?P<pk>\d+)/$',views.dateupdateview.as_view(),name='dateupdate'),



    url(r'^company/(?P<pk>\d+)/trialbalance/date/(?P<pk3>\d+)/$',views.trial_balance_condensed_view,name='trialbalcond'),

    url(r'^company/(?P<pk>\d+)/P&L/date/(?P<pk3>\d+)/$',views.profit_and_loss_condensed_view,name='P&Lcond'),

    url(r'^company/(?P<pk>\d+)/balancesheet/date/(?P<pk3>\d+)/$',views.balance_sheet_condensed_view,name='blsht'),
  
]