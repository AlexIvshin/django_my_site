from django.urls import path
from .views import *
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', head_page, name='head_page_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),

    path('scripts/', scripts_list, name='scripts_list_url'),
    path('script/<str:slug>/', ScriptDetail.as_view(), name='script_detail_url'),

    path('mans/', mans_list, name='mans_list_url'),
    path('man/<str:slug>/', ManDetail.as_view(), name='man_detail_url'),

    path('link/', links_list, name='links_list_url'),

    path('commands/', commands_list, name='commands_list_url'),
    path('command/<str:slug>/', CommandDetail.as_view(), name='command_detail_url'),

    path('search/', search_list, name='search_list_url'),

    path('archive/', archivefiles_list, name='archivefiles_list_url'),
]
