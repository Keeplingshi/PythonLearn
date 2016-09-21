# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from polls.models import Questionnaire, User


# 登录页面
def login(request):

    return render(request, 'polls/login.html')


# 登录验证
def validate_login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            HttpResponseRedirect('/polls/admin')
        else:
            print("Your account has been disabled!")
    else:
        print("Your username and password were incorrect.")

    return render(request, 'polls/login.html')


# 管理页面首页面
@login_required(login_url='/polls/login/')
def admin(request):

    return render(request, 'polls/admin.html')


# 账号管理页面
@csrf_exempt
def user_list(request):
    question_list = Questionnaire.objects.all()
    paginator = Paginator(question_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(2)
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
