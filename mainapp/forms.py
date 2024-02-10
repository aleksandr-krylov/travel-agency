from django import forms
from .models import News
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):

    def use_required_attribute(self, *args):
        return False


class NewsPostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )


    class Meta:
        model = News
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Картинка'
        }