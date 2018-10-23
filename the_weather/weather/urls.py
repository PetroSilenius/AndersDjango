from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup),
    path('actionUrl', views.temp)
]