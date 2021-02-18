from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.models import User
from .models import User
from post.models import Post
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                if next:
                    return redirect(next)
                return redirect('post:home')
            else:
                messages.error(request, 'wrong username or password', 'warning')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['last_name'], cd['phone'], cd['password'])
            # user.save()
            login(request, user)
            messages.success(request, f'You logged in successfully {cd["username"]}', 'success')
            return redirect('post:home')
    else:
        form = UserRegistrationForm()
    return render(request,'accounts/register.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('post:home')

@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'accounts/dashboard.html', {'user': user, 'posts': posts})
# Create your views here.
