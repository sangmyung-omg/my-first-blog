from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')    # publish를 한 것만 뜸
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    # render : MVT 중 template을 불러오는 메소드

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/base.html', {'post': post})
