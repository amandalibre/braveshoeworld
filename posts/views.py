from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


def post_list(request):
    posts = Post.objects.all().order_by("date")
    return render(request, "posts/post_list.html", {"posts":posts})


def post_list_11(request):
    posts_11 = Post.objects.filter(size__exact='11').order_by("date")
    return render(request, "posts/post_list_11.html", {"posts_11":posts_11})


def post_list_12(request):
    posts_12 = Post.objects.filter(size__exact='12').order_by("date")
    return render(request, "posts/post_list_12.html", {"posts_12":posts_12})


def post_list_13(request):
    posts_13 = Post.objects.filter(size__exact='13').order_by("date")
    return render(request, "posts/post_list_13.html", {"posts_13":posts_13})


def post_list_plus(request):
    posts_plus = Post.objects.filter(size__exact='plus').order_by("date")
    return render(request, "posts/post_list_plus.html", {"posts_plus":posts_plus})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html', {'form': form})

