from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AdvertisementView.as_view(), name='advertisement'),
    url(r'^list_advertisiments/$', views.List.as_view(), name='list_advertisiments'),
]