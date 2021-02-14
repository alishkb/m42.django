from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', views.PostView.as_view(), name='detail'),
    path('create/', views.CreatePost, name='create'),
]
