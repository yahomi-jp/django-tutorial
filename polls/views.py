from polls.models import Question
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    question = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question': question
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)