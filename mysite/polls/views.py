from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, "polls/index.html", { 'question_list' : question_list})
    #return HttpResponse("hello world. we are at the polls index.")

def detail(request,question_id):
    question =  Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
   # return HttpResponse("hello world. we are at the polls detail")

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question': question,'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))

def result(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html',{ 'question' : question})
