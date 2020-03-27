from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.urls import reverse 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    template=loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)
    # return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    return HttpResponse("Hello, Sanyam")

def index22(request):
    return HttpResponse("Hello, Sanyam Sanyam")

def detail(request, q_id):
    # return render(request,'polls/details.html',{'question':Question.objects.get(pk=q_id)})
    return render(request,'polls/details.html',{'question':get_object_or_404(Question, pk=q_id)})
    # return HttpResponse("You are looking   at ques%s " %q_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




    