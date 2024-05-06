from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,Blog_tags,Blog_details
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog-modern.html', {'blogs':blogs})

def bdetail(request,pk):
    blog = Blog.objects.get(id=pk)
    blog_details = Blog_details.objects.filter(id=pk)
    blog_tags = Blog_tags.objects.all()
    return render(request, 'blog/blog-single.html',{'pk':blog,'blog_details':blog_details,'tags':blog_tags})