from django.shortcuts import render, redirect
from django.views import generic
from post.models import Post, Comment
from .forms import AddPostForm
from django.contrib import messages

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'post/home.html'
    context_object_name = 'all_posts'
    model = Post
    # template_name = 'post.comment_set.all'
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostView(generic.DetailView):
    template_name = 'post/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        # post = context['post']
        comments = Comment.objects.filter(post=self.object)
        context['comments'] = comments
        return context
    
def CreatePost(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.save()
                messages.success(request, 'پست شما با موفقیت ذخیره شد!', 'success')
                return render('post:home')
            # pass
        else:
            form = AddPostForm()
    return render(request, 'post/create.html', {'form':form})
