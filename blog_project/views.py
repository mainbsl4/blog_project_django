# from django.shortcuts import render
# from posts.models import Post

# def home(request):
#     data = Post.objects.all()
    
#     return render(request, 'home.html', {'data': data})



from django.shortcuts import render
from posts.models import Post
from categories.models import Category
from django.db.models import Q

def home(request):
    query = request.GET.get('q')  # Get search query from the URL, if any
    data = Post.objects.all()

    if query:
        data = Post.objects.filter(
            Q(title__icontains=query) |  # Search by title
            Q(category__name__icontains=query)  # Search by category name
        ).distinct()  # Use distinct to avoid duplicates if a post matches both title and category

    return render(request, 'home.html', {'data': data})