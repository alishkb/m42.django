from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from post.models import Post, Comment
from .forms import AddPostForm, EditPostForm, AddCommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .forms import AddCommentForm
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
        if self.request.method == 'POST':
            form = AddCommentForm(self.request.POST)
            if form.is_valid():
                new_com = form.save(commit=False)
                new_com.post = self.object
                new_com.user = self.request.user
                new_com.save()
                messages.success(request, 'کامنت با موفقیت ثبت شد', 'success')
        else:
            form = AddCommentForm()
            context['form'] = form
        context['comments'] = comments
        return context

@login_required    
def CreatePost(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.save()
                messages.success(request, 'پست شما با موفقیت ذخیره شد', 'success')
                return redirect('post:home')
            # pass
        else:
            form = AddPostForm()
        return render(request, 'post/create.html', {'form':form})
    else:
        return redirect('post:home')

@login_required
def DeletePost(request, user_id, post_id):
    if user_id == request.user.id:
        Post.objects.filter(pk=post_id).delete()
        messages.success(request, 'پست با موفقیت حذف شد', 'success')
        return redirect('accounts:dashboard', user_id)
    else:
        messages.error(request, 'شما اجازه درخواست مورد نظر را ندارید', 'error')
        return redirect('posts:home')

@login_required
def EditPost(request, user_id, post_id):
    if user_id == request.user.id:
        post = get_object_or_404(Post, pk=post_id)
        if request.method =='POST':
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                # re = form.save(commit=False)
                # re.text += (f'edited on {datetime.datetime.now()}')
                # re.save()
                messages.success(request, 'ویرایش پست با موفقیت انجام شد', 'success')
                return redirect('post:detail', post.id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'post/edit.html', {'form':form})
    else:
        return redirect('post:home')

