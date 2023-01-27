"""Project32 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from App.views import *
from django.urls import re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',Home.as_view(),name='Home'),
    path('School_List/',School_List.as_view(),name='School_List'),
    
    path('School_Create/',School_Create.as_view(),name='School_Create'),
    re_path('^update/(?P<pk>\d+)/',School_Update.as_view(),name='update'),                            
    
    re_path('^delete/(?P<pk>\d+)/',School_Delete.as_view(),name='delete'),

    re_path('(?P<pk>\d+)/',School_Detail.as_view(),name='detail'),

]
