from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import register
from django.views import generic
from .models import Post, Comment, Like_Post, Dislike_Post, Like_Comment, Dislike_Comment, Category, Tag
from .forms import AddPostForm, EditPostForm, AddCommentForm, EditCommentForm, SearchForm
from accounts.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .forms import AddCommentForm
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
# from django.contrib.postgres.search import SearchVector
# from django.db.models import Q
# Create your views here.


def HomeView(request, cat_id=None, tag_id=None, user_id=None):
    posts = Post.objects.filter(approving=True)
    categories = Category.objects.filter(is_fcat=True)
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            # if 'sub' in request.GET:
            sub = form.cleaned_data['sub']
            print(sub)
            print(cd)
            if sub == 'all':
                posts = posts.annotate(similarity=Greatest(
                    TrigramSimilarity('title', cd),
                    TrigramSimilarity('text', cd),
                    TrigramSimilarity('user__last_name', cd),
                    TrigramSimilarity('user__first_name', cd),
                    TrigramSimilarity('tag__name', cd),
                )).filter(similarity__gt=0.1).order_by('-similarity')
            elif sub == 'user':
                posts = posts.annotate(similarity=Greatest(
                    TrigramSimilarity('user__last_name', cd),
                    TrigramSimilarity('user__first_name', cd),
                )).filter(similarity__gt=0.1).order_by('-similarity')
            else:
                posts = posts.annotate(similarity=TrigramSimilarity(form.cleaned_data['sub'],cd),).filter(similarity__gt=0.1).order_by('-similarity')
            

            # posts = posts.annotate(search=SearchVector('title', 'text', 'user__last_name', 'user__first_name', 'tag__name')).filter(search=cd)

            # if 'sub' in request.GET:
            #     print([i for i in form.cleaned_data['sub']])
            # # else:
            # posts = posts.filter(Q(title__icontains=cd) | Q(text__icontains=cd) | Q(user__last_name__icontains=cd) | Q(user__first_name__icontains=cd) | Q(tag__name__icontains=cd))
    if cat_id:
        category = get_object_or_404(Category, id=cat_id)
        posts = posts.filter(category=category)
    elif tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        posts = posts.filter(tag=tag)
    if user_id:
        user = get_object_or_404(User, id=user_id)
        posts = posts.filter(user=user)
    return render(request, 'posts/home.html', {'posts':posts, 'categories': categories, 'form':form})


# class HomeView(generic.ListView):
#     template_name = 'posts/home.html'
#     context_object_name = 'posts'
#     model = Post
#     # template_name = 'post.comment_set.all'
#     def get_queryset(self):
#         return Post.objects.order_by('-pub_date')


def PostView(request, post_id):
    post = get_object_or_404(Post, id=post_id)    
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_com = form.save(commit=False)
            new_com.post = post
            new_com.user = request.user
            new_com.save()
            form = AddCommentForm()
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
    else:
        form = AddCommentForm()

    like_dislike = True
    c_like_dislike = {}
    if request.user.is_authenticated:
        if post.like_dislike(request.user) == 'can_dislike':
            like_dislike = 'dislike'
        elif post.like_dislike(request.user) == 'can_like':
            like_dislike = 'like'
        for comment in comments:
            clike = True
            if comment.like_dislike(request.user) == 'can_dislike':
                clike = 'dislike'
            elif comment.like_dislike(request.user) == 'can_like':
                clike = 'like'
            c_like_dislike[comment] = clike

    @register.filter
    def get_item(dict, key):
        return dict.get(key)
    
    return render(request, 'posts/detail.html', {'post':post, 'comments':comments, 'form':form, 'like_dislike': like_dislike, 'clike': c_like_dislike})

# class PostView(generic.DetailView):
#     template_name = 'post/detail.html'
#     model = Post
#     def get_context_data(self, **kwargs):
#         context = super(PostView, self).get_context_data(**kwargs)
#         request = self.request
#         # post = context['post']
#         comments = Comment.objects.filter(post=self.object)
#         if request.method == 'POST':
#             form = AddCommentForm(request.POST)
#             if form.is_valid():
#                 new_com = form.save(commit=False)
#                 new_com.post = request.object
#                 new_com.user = request.user
#                 new_com.save()
#                 messages.success(request, 'کامنت با موفقیت ثبت شد', 'success')
#         else:
#             form = AddCommentForm()
#         context['form'] = form
#         context['comments'] = comments
#         return context

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
                return redirect('posts:home')
            # pass
        else:
            form = AddPostForm()
        return render(request, 'posts/create.html', {'form':form})
    else:
        return redirect('posts:home')

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
                return redirect('posts:detail', post.id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'posts/edit.html', {'form':form})
    else:
        return redirect('posts:home')

@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Dislike_Post.objects.filter(user=request.user, post=post).delete()
    like = Like_Post(user=request.user, post=post)
    like.save()
    return redirect('posts:detail', post_id)

@login_required
def post_dislike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like_Post.objects.filter(user=request.user, post=post).delete()
    dislike = Dislike_Post(user=request.user, post=post)
    dislike.save()
    return redirect('posts:detail', post_id)

def EditComment(request, user_id, comment_id):
    if user_id == request.user.id:
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.method == 'POST':
            form = EditCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, 'ویرایش نظر با موفقیت انجام شد', 'success')
                return redirect('posts:detail', comment.post.id)
        else:
            form = EditCommentForm(instance=comment)
        return render(request, 'posts/edit.html', {'form':form})
    else:
        return redirect('posts:home')

@login_required
def comment_like(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    Dislike_Comment.objects.filter(user=request.user, comment=comment).delete()
    like = Like_Comment(user=request.user, comment=comment)
    like.save()
    return redirect('posts:detail', post_id)

@login_required
def comment_dislike(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    Like_Comment.objects.filter(user=request.user, comment=comment).delete()
    dislike = Dislike_Comment(user=request.user, comment=comment)
    dislike.save()
    return redirect('posts:detail', post_id)
