from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from blog.forms import PostModelForm
from blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'


class PostListlView(ListView):
    model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostCreateView(CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blog/post-add.html'
    success_url = '/posts/'

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.object.slug})
