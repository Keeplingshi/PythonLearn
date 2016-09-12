from django.conf.urls import url

from polls import views

urlpatterns = [
    # ex : /polls/
    # 主页面
    url(r'^$', views.index, name='index'),
    # 投票结果页面
    url(r'results/$', views.results, name='results'),
    # 投票页面
    url(r'vote_form/$', views.vote_form, name='vote_form'),


    # # ex : /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex : /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex : /polls/5/vote
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


]
