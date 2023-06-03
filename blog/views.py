from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


class BlogListview(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 2
    
class BlogDetailView(DetailView):
    model = Blog
    
def about(request):
    return render(request, 'blog/about.html')