from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView

from blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
