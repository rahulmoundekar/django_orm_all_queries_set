"""django_orm_all_queries_set URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from orm_all_queries_cookbook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexView),
    path('countries', views.viewCountries),
    path('states', views.viewStatesByCountry),
    path('cities', views.viewCitiesByState),

    path('doAnd', views.doAnd),
    path('doOr', views.doOr),
    path('doSelectSomeFields', views.doSelectSomeFields),
    path('doFindLargest', views.doFindSecondLargest),
    path('doAsc', views.doAsc),
    path('doDesc', views.doDesc),
    path('doLike', views.doLike),
    path('doBetween', views.doBetween),

    path('getCount', views.getCount),
    path('getCountBy', views.getCountBy),
    path('getAve', views.getAvg),
    path('getMin', views.getMin),
    path('getMax', views.getMax),
]
