from django.conf.urls import url
from consultancy import views

app_name = 'consultancy'

urlpatterns = [
	url(r'^$',views.consultancyListView.as_view(),name='consultancylist'),
	url(r'^(?P<pk>\d+)/$',views.consultancy_detail,name='consultancydetail'),
	url(r'^consultancycreate/$',views.consultancycreate.as_view(),name='consultancycreate'),
	url(r'^consultancyupdate/(?P<pk>\d+)/$',views.consultancyupdate.as_view(),name='consultancyupdate'),
	url(r'^consultancydelete/(?P<pk>\d+)/$',views.consultancydelete.as_view(),name='consultancydelete'),

	url(r'^consultancylike/$', views.liked_post, name="like_question"),

	url(r'^myquestions/$',views.myconsultancyListView.as_view(),name='myquestions'),


]
