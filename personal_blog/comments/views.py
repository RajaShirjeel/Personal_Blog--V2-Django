from django.shortcuts import render, redirect

from comments.models import Comment
from posts.models import Post

# Create your views here.
def create_comment(request, slug):
    if request.method == 'POST':
        text = request.POST.get('comment')
        post = Post.objects.filter(slug=slug).first()
        
        Comment.objects.create(
            user = request.user,
            text = text,
            post = post
        )

    return redirect('posts:view_post', slug=slug)