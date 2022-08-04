from django.contrib import admin
from blog.models import Color, Tag, Post, Comment


@admin.register(Color)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('value',)
    search_fields = ('value',)
    list_display = ('value',)


@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('value', 'color')
    search_fields = ('value', 'color')
    list_display = ('value', 'color')
    fieldsets = (
        (None,
         {'fields': ('value', 'color')}
         ),
    )


@admin.register(Post)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('tags',)
    search_fields = ('title', 'value')
    list_display = ('title', 'value')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('user', 'post')
    search_fields = ('value', 'user', 'post')
    list_display = ('value', 'user', 'post')
