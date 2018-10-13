"""erpcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.conf import settings



urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^base/$", views.base.as_view(), name="base"),
    path('admin/', admin.site.urls),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r"^accounting_double_entry/", include("accounting_double_entry.urls", namespace="accounting_double_entry")),
    url(r"^company/", include("company.urls", namespace="company")),
    url(r"^todo/", include("todogst.urls", namespace="todogst")),
    url(r"^profile/", include("userprofile.urls", namespace="userprofile")),
    url(r"^blog/", include("blog.urls", namespace="blog")),
    url(r'^select2/', include('django_select2.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r"^consultancy/", include("consultancy.urls", namespace="consultancy")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


handler404 = 'erpcloud.views.custom_404'
handler500 = 'erpcloud.views.custom_500'



