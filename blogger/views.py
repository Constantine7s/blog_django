from django.shortcuts import render
from .models import Post, Category, Author

def home(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest':latest,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def post(request, slug)
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    
    return render(request, 'post.html', context)

def about (request):
    return render(request, 'about.html')