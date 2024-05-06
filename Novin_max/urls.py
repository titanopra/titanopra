"""
URL configuration for Novin_max project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.contrib import admin
from django.urls import path
from azbankgateways.urls import az_bank_gateways_urls
from novin_part.views import go_to_gateway_view,callback_gateway_view

urlpatterns = [
    path('', include('home.urls')),
    path('', include('novin_media.urls')),
    path('', include('novin_fix.urls')),
    path('', include('blog.urls')),
    path('', include('novin_academy.urls')),
    path('', include('acount.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    path("bankgateways/", az_bank_gateways_urls()),
    path('', include('novin_part.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
