from django.contrib import admin
from blog.models import Color, Tag, Post, Comment


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_filter = ('value',)
    search_fields = ('value',)
    list_display = ('value',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('value', 'color')
    search_fields = ('value', 'color')
    list_display = ('value', 'color')
    fieldsets = (
        (None,
         {'fields': ('value', 'color')}
         ),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('tags', 'user')
    search_fields = ('title', 'value', 'user')
    list_display = ('title', 'value', 'user')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('user', 'post')
    search_fields = ('value', 'user', 'post')
    list_display = ('value', 'user', 'post')
