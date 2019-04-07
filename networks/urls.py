from django.urls import path

from . import views

app_name = 'networks'
urlpatterns = [
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('get_jails', views.get_jails, name='get_jails'),
]
