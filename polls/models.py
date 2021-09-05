from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('内容', max_length=200)
    pub_date = models.DateTimeField('公開日')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('内容', max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text