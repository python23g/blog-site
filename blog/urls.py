from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogsView.as_view(), name='blogs_detail'),
]
