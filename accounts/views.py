from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import User
from posts.models import Post
from .forms import UserLoginForm, UserRegistrationForm, PhoneLoginForm, VerifyPhoneForm, UserDashboardForm
from django.contrib.auth.decorators import login_required
from random import randint
from kavenegar import *



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
                messages.success(request, 'شما با موفقیت وارد شدید', 'success')
                if next:
                    return redirect(next)
                return redirect('posts:home')
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
            if cd['password'] == cd['re_password']:
                normal_user = Group.objects.get(name = 'کاربران ساده')
                user = User.objects.create_user(cd['username'], cd['last_name'], cd['phone'], cd['password'])
                user.groups.add(normal_user)
                # user.save()
                login(request, user)
                messages.success(request, f'اطلاعات شما با موفقیت ثبت شد {cd["username"]}', 'success')
                return redirect('posts:home')
            else:
                messages.error(request, 'رمز وارد شده با تکرار رمز یکسان نمیباشد', 'error')
    else:
        form = UserRegistrationForm()
    return render(request,'accounts/register.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید', 'success')
    return redirect('posts:home')

@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    if request.method == 'POST':
        form = UserDashboardForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات کاربر با موفقیت به روزرسانی شد', 'success')
    else:
        form = UserDashboardForm(instance=user)
    return render(request, 'accounts/dashboard.html', {'user': user, 'posts': posts, 'form':form})

def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            # global phone, ch
            # set ch in session
            phone = f"0{form.cleaned_data['phone']}"
            ch = randint(1000, 9999)
            request.session['ch'] = ch
            request.session['phone'] = phone
            api = KavenegarAPI('37513432732F4B58674A7A4D504D7375474F47526634327934564351502F673337384E7A4A39584D5333383D')
            params = { 'sender': '', 'receptor':phone, 'message':ch }
            response = api.sms_send(params)
            return redirect('accounts:verify')
    else:
        form = PhoneLoginForm()
    return render(request, 'accounts/phone_login.html', {'form':form})

def verify(request):
    if request.method == 'POST':
        form = VerifyPhoneForm(request.POST)
        if form.is_valid():
            ch = request.session['ch']
            if ch == form.cleaned_data['code']:
                phone = request.session['phone']
                user = get_object_or_404(User, phone=phone)
                login(request, user)
                messages.success(request, 'شما با موفقیت وارد شدید', 'success')
                return redirect('posts:home')
            else:
                messages.error(request, 'کد وارد شده معتبر نمیباشد', 'warning')                
    else:
        form = VerifyPhoneForm()
    return render(request, 'accounts/verify.html', {'form':form})
# Create your views here.
