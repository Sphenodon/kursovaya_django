from django.contrib import admin

from .models import News, CommentsForNews, CommentsForTpNews, NewsFromAssociate


class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated', 'news_author']
    list_display_links = ['title']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']
    list_editable = []

    class Meta:
        model = News


class TpNewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated', 'news_author']
    list_display_links = ['title']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']
    list_editable = []

    class Meta:
        model = NewsFromAssociate


class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['news_id', 'comment_text', 'comment_author']
    list_display_links = ['comment_text']
    search_fields = ['comment_text']
    list_filter = ['timestamp']
    list_editable = []

    class Meta:
        model = CommentsForNews


class TpCommentsModelAdmin(admin.ModelAdmin):
    list_display = ['news_id', 'comment_text', 'comment_author']
    list_display_links = ['comment_text']
    search_fields = ['comment_text']
    list_filter = ['timestamp']
    list_editable = []

    class Meta:
        model = CommentsForTpNews


admin.site.register(News, NewsModelAdmin)
admin.site.register(NewsFromAssociate, TpNewsModelAdmin)
admin.site.register(CommentsForNews, CommentsModelAdmin)
admin.site.register(CommentsForTpNews, TpCommentsModelAdmin)
