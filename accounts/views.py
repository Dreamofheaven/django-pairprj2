from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from .models import User

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

#회원조회
@login_required
def detail(request, pk):
    User_detail = User.objects.get(pk=pk)
    context = {
        'User_detail':User_detail,
    }
    return render(request,'accounts/detail.html',context)

#정보수정
# def edit(request, user):
@login_required
def edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else: 
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
        # 'user': user,
    }
    return render(request,'accounts/update.html', context)

#회원탈퇴
@login_required
def delete(request):
    user = request.user
    user.delete()
    logout(request)
    return redirect(request,'posts:index')