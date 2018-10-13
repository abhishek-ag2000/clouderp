from django.conf.urls import url

from .views import (
        SelectDateRange
        )

urlpatterns = [
    url(r'^$', SelectDateRange.as_view(), name='daterange'),
]
