from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^list/$', views.List.as_view(), name='list'),
    url(r'^login/$', views.login, name='login'),

]