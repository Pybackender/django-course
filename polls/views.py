from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Choice, Question
from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView


# def index(request):
#     demo = []
#     latest = Question.objects.order_by("-pub_date")[:5]
#     # for i in latest:
#     #     demo.append(i.question_text)
#     # output = ", ".join(demo)
#     context = {
#         "latest":latest
#     }
#     return render(request,"polls/index.html", context)
class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "latest"
    queryset = Question.objects.order_by("-pub_date")[:5]


###############################################################

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Questio doesnot exisit ...")
#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question":question}
    
#     return render(request, "polls/detail.html", context)

class DetailView(DetailView):
    model= Question
    template_name = "polls/detail.html"
   
###################################################################
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question":question
#     }
#     return render(request, "polls/result.html", context)


class ResultsView(DetailView):
    model = Question
    template_name = "polls/result.html"
###################################################################


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        select_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice."
        }
        return render(request, "polls/detail.html", context)
    else:
        select_choice.votes = F('votes') + 1
        select_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))