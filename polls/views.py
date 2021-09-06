from django.http.response import HttpResponseRedirect
from polls.models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.


class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published inthe future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(DetailView):
    model = Question
    template_name = "polls/result.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))