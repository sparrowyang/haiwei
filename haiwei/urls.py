"""haiwei URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import detail, api
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index),
                  path('api/v1/loadall', api.main_data),

                  path('detail/', detail.open),
                  path('uploads/', views.r_upload),
                  path('uploads/new/', views.upload),
                  path('uploads/login/', views.r_login),
                  path('all/', views.all_data),
                  path('setting/', views.setting),
                  path('setting/save/', views.save_settting),

                  path('search/location/', views.location_data),
                  path('search/taste/', views.taste_data),
                  path('search/id/', views.id_data),
                  path('search/fname/', views.fname_data),
                  path('search/random/', views.random_data),
                  path('location/', views.location_data)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
