from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Frage: %s." % question_id)

def results(request, question_id):
    response = "Antworten von Frage: %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Sie stimmen ab für Frage: %s." % question_id)
