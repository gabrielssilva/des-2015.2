from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.advertisement, name='advertisement'),
    url(r'^list_advertisiments/$', views.List.as_view(), name='list_advertisiments'),
]