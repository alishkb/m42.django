from django.http import HttpResponse
from django.views import generic
from post.models import Post

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'post/home.html'
    context_object_name = 'all_posts'
    model = Post
    # template_name = 'post.comment_set.all'
    # def get_queryset(self):
    #     return Post.objects.order_by('-pub_date')

class PostView(generic.DetailView):
    model = Post
    template_name = 'post/post.html'


