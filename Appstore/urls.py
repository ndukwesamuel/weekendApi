"""Appstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from Home.views import (data_page, simple_one ,CreateData,
 DataListView, DataOne, UpdateData)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_page ,  name="home"),
    path('simple/', simple_one.as_view(),  name="simple_one"),
    path('data/', DataListView.as_view(),  name="DataListView"),
    path('create/', CreateData.as_view(),  name="CreateData"),

    path('data/<str:pk>/', DataOne.as_view(),  name="DataOne"),
    path('update/<str:pk>/', UpdateData.as_view(),  name="UpdateData"),





]
