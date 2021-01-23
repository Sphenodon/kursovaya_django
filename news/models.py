from django.db import models
from django.urls import reverse


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    news_author_id = models.BigIntegerField(default=1, verbose_name='id автора')
    news_author = models.CharField(max_length=30, verbose_name='Автор', default='unknown')
    img_link = models.CharField(max_length=300, verbose_name='Ссылка на картинку',
                                default='/resources/static/img/news-1.jpg')

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('news:detail', kwargs={'news_id': self.id})

    def get_update_url(self):
        return reverse('news:update', kwargs={'news_id': self.id})

    def get_delete_url(self):
        return reverse('news:delete', kwargs={'news_id': self.id})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'news'


class NewsFromAssociate(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    news_link = models.CharField(max_length=200, verbose_name='Сайт', default='unknown')
    news_author = models.CharField(max_length=30, verbose_name='Автор', default='unknown')
    img_link = models.CharField(max_length=300, verbose_name='Ссылка на картинку',
                                default='/resources/static/img/news-1.jpg')

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('news:tpn_detail', kwargs={'news_id': self.id})

    def get_update_url(self):
        return reverse('news:tpn_update', kwargs={'news_id': self.id})

    def get_delete_url(self):
        return reverse('news:tpn_delete', kwargs={'news_id': self.id})

    class Meta:
        verbose_name = 'Новость партёра'
        verbose_name_plural = 'Новости партнёров'
        db_table = 'news_from_associate'


class CommentsForNews(models.Model):
    id = models.AutoField(primary_key=True)
    news_id = models.IntegerField(default=0, verbose_name='id новости')
    comment_text = models.TextField(verbose_name='Комментарий')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True,
                                     verbose_name='Дата публикации')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    comment_author = models.CharField(max_length=30, verbose_name='Автор комментария', default='unknown')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий для новостей'
        verbose_name_plural = 'Комментарии для новостей'
        db_table = 'news_comments'


class CommentsForTpNews(models.Model):
    id = models.AutoField(primary_key=True)
    news_id = models.IntegerField(default=0, verbose_name='id новости')
    comment_text = models.TextField(verbose_name='Комментарий')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True,
                                     verbose_name='Дата публикации')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    comment_author = models.CharField(max_length=30, verbose_name='Автор комментария', default='unknown')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий для партнерских новостей'
        verbose_name_plural = 'Комментарии для партнерских новостей'
        db_table = 'news_tp_comments'
