from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post_detail/<int:pk>/', views.PostView.as_view(), name='detail'),
    path('post_create/<int:user_id>', views.CreatePost, name='create'),
    path('post_delete/<int:user_id>/<int:post_id>/', views.DeletePost, name='delete'),
    path('post_edit/<int:user_id>/<int:post_id>/', views.EditPost, name='edit')
]
