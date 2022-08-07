from django import forms

from blog.models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'value', 'image_url', 'tags')

        widgets = {
            'title': forms.TextInput(),
            'value': forms.Textarea(),
            'image_url': forms.TextInput(),
            'tags': forms.SelectMultiple(),
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('value',)

        widgets = {
            'value': forms.Textarea(),
        }
