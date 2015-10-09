from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^register/$', views.Auth.register, name='register'),
    url(r'^list/$', views.List.as_view(), name='list'),
    url(r'^login/$', views.Auth.login, name='login'),
    url(r'^logout/$', views.Auth.logout, name='logout'),
    url(r'^$', views.homeLogged, name='logged_index'),
]