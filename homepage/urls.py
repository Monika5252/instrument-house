
from django.urls import path
from imd.homepage import views

urlpatterns = [
    path('Homepage/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    ]