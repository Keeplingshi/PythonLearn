# coding=utf-8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from polls.models import Questionnaire


# 验证登录
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/polls/admin')
        else:
            print("Your account has been disabled!")
    else:
        # 如果存在用户名密码，但不正确，则提示
        if username is not None and password is not None:
            context = {'isSuccess': 1}
            return render(request, 'polls/login.html', context)

        return render(request, 'polls/login.html')


# 退出登录
def logout(request):
  auth.logout(request)

  return HttpResponseRedirect("/polls/login")


# 修改密码页面
@login_required
def modify_password_view(request):
    user = auth.get_user(request)
    context = {'user': user}
    return render(request, 'polls/modifyPasswordView.html', context)

# 修改密码
@login_required
def modify_password(request):
    user = auth.get_user(request)
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('password')
    if User.check_password(user, old_password):
        User.set_password(user, new_password)
        User.save(user)
        # 重新登录
        auth.login(request, user)
        return HttpResponse("success")

    return HttpResponse("error")

# 管理页面首页面
@login_required
def admin(request):
    user = auth.get_user(request)
    context = {'user': user}
    return render(request, 'polls/admin.html', context)


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
