from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Color(models.Model):
    value = models.CharField(max_length=20, verbose_name=_('Color value'), unique=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    value = models.CharField(max_length=40, verbose_name=_('Tag value'), unique=True)
    color = models.ForeignKey(to='blog.Color', on_delete=models.SET(''), related_name='tags')
    updated_at = models.DateTimeField(verbose_name=_('Last saved at'), auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)

    def __str__(self):
        return self.value


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('Post title'), unique=True)
    value = models.TextField(verbose_name=_('Post value'))
    tags = models.ManyToManyField(to='blog.Tag', related_name='posts', verbose_name=_('Post tags'), blank=True)
    image_url = models.URLField(verbose_name=_('Post thumbnail url'), blank=True)
    updated_at = models.DateTimeField(verbose_name=_('Last saved at'), auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)

    def slug(self):
        return slugify(f'{self.title} {self.id}')

    def __str__(self):
        return self.title


class Comment(models.Model):
    value = models.TextField(verbose_name=_('Comment value'))
    user = models.ForeignKey(to='user.User', related_name='comments', verbose_name=_('User'), on_delete=models.CASCADE)
    post = models.ForeignKey(to='blog.Post', related_name='comments', verbose_name=_('Post'), on_delete=models.CASCADE)
    updated_at = models.DateTimeField(verbose_name=_('Last saved at'), auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)

    def __str__(self):
        return f'[{self.user}]: {self.value}'
