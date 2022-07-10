from django.urls import path
from . import views

urlpatterns = [
    # path('getCreds/', views.getCreds),
    path('', views.landing),
    path('getCreds/', views.getCreds),
]
