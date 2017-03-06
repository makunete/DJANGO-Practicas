from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the CoInf index.")
# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at incidence %s." % incidencies_id)

def results(request, question_id):
    response = "You're looking the information of the incidence %s."
    return HttpResponse(response % incidencies_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

