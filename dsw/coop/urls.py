from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^list/$', views.List.as_view(), name='list'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^$', views.homeLogged, name='logged_index'),
    
]