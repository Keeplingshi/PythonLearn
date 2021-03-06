# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 调查问卷
class Questionnaire(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


# 问题
class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, default=1)
    question_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text


# 选择
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


# 选择记录表
class History(models.Model):
    user = models.ManyToManyField(User)
    questionnaire = models.ManyToManyField(Questionnaire)
    choice = models.ForeignKey(Choice)
    order = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.order
