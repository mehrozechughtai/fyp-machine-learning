from django.http import HttpResponse
from django.shortcuts import render
from .models import MyClass

# Create your views here.

def index(request):
	context = {}
	return render(request,'mainapp/index.html',context)


