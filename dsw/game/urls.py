from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^create_game/$', views.create_game, name='create_game'),
    url(r'^list_game/$', views.List.as_view(), name='list_game'),
]