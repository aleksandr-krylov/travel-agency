from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView
from .models import Post, Comment
from .forms import CommentForm


def blog(request):
    posts = Post.objects.all()
    top3posts = posts[:3]
    top5comments = Comment.objects.all()[:5]
    comments = []
    for post in posts:
        n_comments = len(Comment.objects.filter(post=post.id))
        comments.append(n_comments)

    posts_comments = zip(posts, comments)

    context = {
        'posts': posts,
        'top3posts': top3posts,
        'top5comments': top5comments,
        'posts_comments': posts_comments
    }

    return render(request, 'blog/blog-main.html', context)


def blogpost(request, pk):
    # retrieve the requested post from posts table
    post = Post.objects.get(id=pk)
    # pull up all the comments of the requested blog-post by filtering
    comments = Comment.objects.filter(post=pk)
    # Handle the form for adding a comment
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # Fill in following fields since the form doesn't have such fields
            comment_form = form.save(commit=False)
            comment_form.author = request.user
            comment_form.date_commented = timezone.now()
            comment_form.post = Post.objects.get(id=pk)
            # Save changes
            comment_form.save()
            return redirect('blog-post', pk=post.id)
        else:
            for message in form.error_messages:
                messages.error(request, f'{message}: {form.error_messages[message]}')
    else:
        form = CommentForm() # blank form

    top3posts = Post.objects.all()[:3]
    top5comments = Comment.objects.all()[:5]
    n_comments = len(comments)

    context = {
        'top3posts': top3posts,
        'top5comments': top5comments,
        'post': post,
        'comments': comments,
        'n_comments': n_comments,
        'form': form
    }

    return render(request,
                  'blog/blog-post.html',
                  context)

