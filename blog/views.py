from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    Posts = Post.objects.filtter(published_date__lte = timezone.now() ).order_by('published_date')
    return render(request, 'blog/post_list.html', {})       