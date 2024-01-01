"""
URL configuration for djangoProject4 project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from ca2 import views
from ca2.views import contact_view

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('zones/', views.QuietZoneListView.as_view(), name='list_zones'),
    path('zones/<int:pk>/', views.QuietZoneDetailView.as_view(), name='detail_zone'),
    path('contact/', contact_view, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
