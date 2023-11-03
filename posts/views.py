from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def init(request):
    return redirect('posts:index')

@login_required
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'get_user_model': get_user_model,
    }
    return render(request,'posts/index.html',context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')


@login_required
def read(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/read.html', context)


@login_required
def create(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:read',post.pk)
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request,'posts/new.html',context)


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:read', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/edit.html', context)


@login_required
def view_category(request, subject):
    category_dict = {
        'develop': '개발',
        'design':'디자인',
        'plan':'기획',
    }
    print(category_dict[subject])
    posts = Post.objects.filter(category=category_dict[subject])
    print(posts)
    context = {
        'posts': posts,
        'subject':subject,
    }
    return render(request, 'posts/view_category.html', context)


@login_required
def post_comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post_comment_form = PostCommentForm(request.POST)
    if post_comment_form.is_valid():
        comment = post_comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:read', post.pk)
    context = {
        'post': post,
        'post_comment_form': post_comment_form,
    }
    return render(request, 'posts/read.html', context)
