from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from CoInf.models import *

def index(request):
    return HttpResponse("Hello. You're at the CoInf index.")
# Create your views here.

class CompresCreateView(CreateView):
	model = Compres
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "compres.html"
	fields = ['numero','departament','material','quantitat','pressupost']



def detail(request, question_id):
    return HttpResponse("You're looking at incidence %s." % incidencies_id)

def results(request, question_id):
    response = "You're looking the information of the incidence %s."
    return HttpResponse(response % incidencies_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

