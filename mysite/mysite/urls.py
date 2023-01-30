"""mysite URL Configuration

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
from django.urls import path, include 
from pages.views import home_view , contact_view
from playground.views import service_detail_view , service_create_view , dynamic_lookup_view, stock_search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home') ,
    path('create/', service_create_view),
    path('contact/', contact_view),
    path('service/' , service_detail_view ),
    path('service/stocksearch/', stock_search_view )
  
]
