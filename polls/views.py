from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    return HttpResponse("Hello, Sanyam")

def index22(request):
    return HttpResponse("Hello, Sanyam Sanyam")

def detail(request, q_id):
    print( q_id)
    return HttpResponse("You are looking   at ques%s " %q_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


    