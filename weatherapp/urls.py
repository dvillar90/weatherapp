"""weatherapp URL Configuration

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
from weather import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather', views.index, name="index"),  #the path for our index view
    path('login', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('', include ('django.contrib.auth.urls')),
    path('map',views.map,name="map"),
    path('home', views.home, name="home"),
    path('weather', views.index_2, name="index"),
    path('delete_city/<int:city_id>/', views.delete_city, name='delete_city'),
    path('', views.intro, name="intro"),
    path('login', views.view_login, name="login")
   ]

