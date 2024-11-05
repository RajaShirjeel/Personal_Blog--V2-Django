from django.shortcuts import render, redirect

from .forms import CreatePost
from .models import Post

# Create your views here.
def home_page(request):

    posts = Post.objects.all()
    first_post = posts.first()
    posts = posts[1:]
    return render(request, 'posts/home.html', {'posts': posts, 'first_post': first_post})


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
    date = post.created_on.strftime('%b %-d, %Y')
    return render(request, 'posts/post.html', {'post':post, 'date':date})