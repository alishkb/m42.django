from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
]
