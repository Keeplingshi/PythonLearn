# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from polls.models import Questionnaire


# 管理页面首页面
def admin(request):

    return render(request, 'polls/admin.html')


# 账号管理页面
@csrf_exempt
def user_list(request):
    question_list = Questionnaire.objects.all()
    paginator = Paginator(question_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'polls/user/userList.html', {'contacts': contacts})

# # 首页展示所有问题
# def index(request):
#     print("44444444444444444444444444")
#     latest_question_list = Question.objects.all()
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# # 投票提交
# def vote_form(request):
#     latest_question_list = Question.objects.all()
#     for question in latest_question_list:
#         p = get_object_or_404(Question, pk=question.id)
#         try:
#             selected_choice = p.choice_set.get(pk=request.POST['choice_'+str(question.id)])
#         except (KeyError, Choice.DoesNotExist):
#             print(KeyError)
#         else:
#             selected_choice.votes += 1
#             selected_choice.save()
#
#     return HttpResponseRedirect('/polls/results')
#
#
# # 投票结果
# def results(request):
#     print("478777777777777777777")
#     latest_question_list = Question.objects.all()
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/results.html', context)
