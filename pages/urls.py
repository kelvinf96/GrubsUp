from django.urls import path
from pages import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('home/', views.HomePageView.as_view(), name='homepage'),
]
