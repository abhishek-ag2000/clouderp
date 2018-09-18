from django.conf.urls import url
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
	

	url(r'^$',views.profiledetailview.as_view(),name='profiledetail'),
	url(r'^profileupdate/$',views.profileupdateview.as_view(),name='profileupdate'),
]