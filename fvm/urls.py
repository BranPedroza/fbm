from django.urls import path, include



urlpatterns = [
    path('dashboard/',include('dashboard.urls')),
    path('usuarios/',include('usuarios.urls')),
]
