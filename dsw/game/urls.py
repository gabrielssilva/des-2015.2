from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^advertisement/$', views.create_game, name='advertisement'),
    url(r'^list_game/$', views.List.as_view(), name='list_game'),
]