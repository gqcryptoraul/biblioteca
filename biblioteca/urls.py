"""
    biblioteca URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('app.autor.urls')),
    re_path('', include('app.libro.urls')),
    re_path('', include('app.lector.urls')),
]
