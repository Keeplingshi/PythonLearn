# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice


# 首页展示所有问题
def index(request):
    print("44444444444444444444444444")
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# 投票提交
def vote_form(request):
    latest_question_list = Question.objects.all()
    for question in latest_question_list:
        p = get_object_or_404(Question, pk=question.id)
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice_'+str(question.id)])
        except (KeyError, Choice.DoesNotExist):
            print(KeyError)
        else:
            selected_choice.votes += 1
            selected_choice.save()

    return HttpResponseRedirect('/polls/results')


# 投票结果
def results(request):
    print("478777777777777777777")
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/results.html', context)
