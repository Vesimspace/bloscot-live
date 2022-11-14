from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView

from .models import Post


class BlogPageView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 1

class BlogOtherView(ListView):
    model = Post
    template_name = 'blog.html'
    paginate_by = 1

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'

