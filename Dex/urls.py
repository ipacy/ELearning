"""Dex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.documentation import include_docs_urls
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

admin.site.site_header = "E Learning System"
admin.site.site_title = "E Learning System"
admin.site.index_title = "Welcome to E Learning Portal"

urlpatterns = [
                  path('kichuadmin/', admin.site.urls),
                  path('docs/', include_docs_urls(title='E Learning API')),
                  path('', include('home.api.urls')),
                  path('', include('course.api.urls')),
                  path('', include('enrollment.api.urls')),
                  path('restauth/', include('rest_auth.urls')),
                  path('', TemplateView.as_view(template_name="submarine.html")),
                  path('', include('progress.urls')),
                  path('silk/', include('silk.urls', namespace='silk'))

              ] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)