from django.shortcuts import render
from raasite.models import Member
from django.http import HttpResponse
from django.template import loader, Context


# Create your views here.
def index(request):
	temp = loader.get_template("index.html")
	cont = Context()
	return HttpResponse(temp.render(cont)) 

def members(request):
	members = Member.objects.all()
	temp = loader.get_template("members.html")
	cont = Context({'members':members})
	return HttpResponse(temp.render(cont))
