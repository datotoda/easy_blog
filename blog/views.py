from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin, DeleteView

from blog.forms import PostModelForm, CommentModelForm
from blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


class PostDetailView(DetailView, FormMixin):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
    form_class = CommentModelForm
    success_url = 'posts/'

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('user:login'))

        form = self.get_form()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.post_id = self.get_object().id
            obj.user_id = self.request.user.id
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.get_object().slug})


class PostListlView(ListView):
    model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'
    paginate_by = 10


class MyPostListlView(PostListlView):
    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).all()


class PostCreateView(CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blog/post-add.html'
    success_url = '/posts/'
    object = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.object.slug})


class PostOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id != self.get_object().user.id:
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)


class PostEditView(PostOwnerMixin, UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blog/post-update.html'

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.object.slug})


class PostDeleteView(PostOwnerMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post-list')
    template_name = 'blog/post-delete.html'
