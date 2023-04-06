from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def init(request):
    return redirect('posts:index')

@login_required
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
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
            post = form.save()
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
    print(subject)
    posts = Post.objects.filter(category=subject)
    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/view_category.html', context)
