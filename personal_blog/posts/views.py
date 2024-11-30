from django.shortcuts import render, redirect
from functools import wraps

from .forms import CreatePost
from .models import Post
from comments.models import Comment

# Create your views here.

# admin only decorator
def authors_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        profile = request.user
        if profile.id == 1:
            return function(request, *args, **kwargs)
        else:
            return render(request, 'posts/admin.html')
        
  return wrap

def home_page(request):

    posts = Post.objects.all()
    first_post = posts.first()
    posts = posts[1:]
    return render(request, 'posts/home.html', {'posts': posts, 'first_post': first_post})

@authors_only
def create_form(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            return redirect('posts:home')
        
    else:
        form = CreatePost()

    return render(request, 'posts/new_post.html', {'form': form})


def view_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post_date = post.created_on.strftime('%b %-d, %Y')
    comments = Comment.objects.filter(post = post).all()
    return render(request, 'posts/post.html', {'post':post, 'date':post_date, 'comments': comments})


def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect('posts:home')