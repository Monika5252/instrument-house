from django.urls import path

if __name__ == '__main__':
    from imd.homepage import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
]