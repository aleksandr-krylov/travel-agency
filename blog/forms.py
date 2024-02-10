from django import forms
from .models import Post, Comment
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):

    def use_required_attribute(self, *args):
        return False


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )


    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'image']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'content': 'Содержание',
            'image': 'Картинка'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ['text']
        labels = {'text': 'Комментарий'}
