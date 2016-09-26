from django.conf.urls import url

from polls import views
from polls import user_views

urlpatterns = [
    # ex : /polls/
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': mysite.settings.STATIC_URL}),
    # 管理页面
    # url(r'^$', views.login),
    url(r'login/$', user_views.login, name='login'),
    url(r'logout/$', user_views.logout, name='logout'),
    url(r'modify_password_view/$', user_views.modify_password_view, name='modify_password_view'),
    url(r'modify_password/$', user_views.modify_password, name='modify_password'),
    url(r'admin/$', views.admin, name='admin'),
    url(r'userList/$', user_views.user_list, name='userList'),
    url(r'user/userAdd/$', user_views.user_add, name='userAdd'),
    url(r'user/save/$', user_views.user_save, name='userSave'),
    url(r'user/resetPassword/$', user_views.reset_password, name='userResetPassword'),
    url(r'user/delete/$', user_views.delete, name='delete'),
    # 主页面
    # url(r'index/$', views.index, name='index'),
    # 投票结果页面
    # url(r'results/$', views.results, name='results'),
    # 投票页面
    # url(r'vote_form/$', views.vote_form, name='vote_form'),


    # # ex : /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex : /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex : /polls/5/vote
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


]
