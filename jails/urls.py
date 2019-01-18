from django.urls import path

from . import views

app_name = 'jails'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<str:jail_name>/', views.detail, name='detail'),
    path('fetch_releases', views.fetch_releases, name='fetch_releases'),
    path('fetch_jails', views.fetch_jails, name='fetch_jails'),
    path('start', views.start, name='start'),
    path('stop', views.stop, name='stop'),
    path('delete', views.delete, name='delete'),
    path('create', views.create, name='create'),
]
