from django.urls import path

from . import views

app_name = 'firewalls'
urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_all_lists', views.fetch_all_lists, name='fetch_all_lists'),
]