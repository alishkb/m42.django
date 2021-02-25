from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('category/<int:cat_id>', views.HomeView, name='cat_filter'),
    path('post_detail/<int:post_id>/', views.PostView, name='detail'),
    path('post_create/<int:user_id>', views.CreatePost, name='create'),
    path('post_delete/<int:user_id>/<int:post_id>/', views.DeletePost, name='delete'),
    path('post_edit/<int:user_id>/<int:post_id>/', views.EditPost, name='edit'),
    path('like/<int:post_id>/', views.post_like, name='post_like'),
    path('dislike/<int:post_id>/', views.post_dislike, name='post_dislike'),
    path('clike/<int:post_id>/<int:comment_id>/', views.comment_like, name='comment_like'),
    path('cdislike/<int:post_id>/<int:comment_id>/', views.comment_dislike, name='comment_dislike'),  
]
