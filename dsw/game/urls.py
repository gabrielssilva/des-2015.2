from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list_game/$', views.List.as_view(), name='list_game'),
    url(r'^get_game_form/$', views.new_game_form, name='get_game_form'),
]