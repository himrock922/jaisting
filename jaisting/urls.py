from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('django_admins/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^jails/', include('jails.urls')),
    url(r'^networks/', include('networks.urls')),
]
