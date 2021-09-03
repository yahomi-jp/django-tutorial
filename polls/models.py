from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('内容', max_length=200)
    pub_date = models.DateTimeField('公開日')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('内容', max_length=200)
    votes = IntegerField(default=0)