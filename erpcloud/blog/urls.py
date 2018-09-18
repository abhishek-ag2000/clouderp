from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
	url(r'^$',views.bloglistview.as_view(),name='bloglist'),
	url(r'^(?P<pk>\d+)/$',views.blogdetailsview.as_view(),name='blogdetail'),
	url(r'^blogcreate/$',views.blogcreateview.as_view(),name='blogcreate'),
	url(r'^blogupdate/(?P<pk>\d+)/$',views.blogupdateview.as_view(),name='blogupdate'),
	url(r'^blogdelete/(?P<pk>\d+)/$',views.blogdeleteview.as_view(),name='blogdelete'),
	url(r'^bloglist/$',views.allbloglistview.as_view(),name='allbloglist'),


	url(r'^categorylist/$',views.categoryListView.as_view(),name='categoryList'),
	url(r'^categorylist/(?P<pk>\d+)/$',views.categoryDetailView.as_view(),name='categoryDetail'),

	url(r'^result/$', views.search, name='search'),
]