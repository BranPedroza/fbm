from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('admin/', admin.site.urls),
]
