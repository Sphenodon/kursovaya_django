from django.forms import ModelForm

from .models import News


class NewsFormCreate(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'id', ]


class NewsFormUpdate(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'id', ]
