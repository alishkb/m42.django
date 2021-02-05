from django.http import HttpResponse
from django.views import generic
from post.models import Post, Comment

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'post/home.html'
    context_object_name = 'all_posts'
    model = Post
    # template_name = 'post.comment_set.all'
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostView(generic.DetailView):
    template_name = 'post/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        # post = context['post']
        comments = Comment.objects.filter(post=self.object)
        context['comments'] = comments
        return context
    