from django.urls import re_path

from news import views

urlpatterns = [
    re_path(r'^news/detail/(?P<news_id>\d+)/$', views.news_detail, name='detail'),
    re_path(r'^news/update/(?P<news_id>\d+)/$', views.news_update, name='update'),
    re_path(r'^news/delete/(?P<news_id>\d+)/$', views.news_delete, name='delete'),
    re_path(r'^thirdPartyNews/detail/(?P<news_id>\d+)/$', views.third_party_news_detail, name='tpn_detail'),
    re_path(r'^thirdPartyNews/update/(?P<news_id>\d+)/$', views.third_party_news_update, name='tpn_update'),
    re_path(r'^thirdPartyNews/delete/(?P<news_id>\d+)/$', views.third_party_news_delete, name='tpn_delete'),
    re_path(r'^create/$', views.news_create, name='create'),
    re_path(r'^thirdPartyNews/$', views.third_party_news),
    re_path(r'^myNews/$', views.my_news),
    re_path(r'^startGen/$', views.start_gen),
    re_path(r'^stopGen/$', views.stop_gen),
    re_path(r'^$', views.news_list),
]
