from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from blogs.forms import BlogPostForm
from .models import BlogPost
from .my_checks import check_current_user

def index(request):
    """Home page"""
    blog_posts = BlogPost.objects.order_by('-date_added')
    content = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', content)

@login_required
def new_post(request):
    """Add a new blog"""
    if request.method != 'POST':
        #No data submitted, create a blank form.
        form = BlogPostForm()
    else:
        #POST data submitted, process data
        form = BlogPostForm(request.POST)
        if form.is_valid():
            #Add owner for each post
            new_post = form.save(commit=False)
            new_post.owner = request.user
            
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit a existing blog."""
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method != 'POST':
        #Initial request, pre-fill with current blog.
        form = BlogPostForm(instance=post)
    else:
        #POST data submitted, process data
        form = BlogPostForm(data=request.POST, instance=post)
        if form.is_valid():
            check_current_user(request, post)
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form, 'post':post}
    return render(request, 'blogs/edit_post.html', context)