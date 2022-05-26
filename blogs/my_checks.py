from django.http import Http404

def check_current_user(request, blog_post):
    """Make sure If post ownered by current user."""
    if request.user != blog_post.owner:
        raise Http404
