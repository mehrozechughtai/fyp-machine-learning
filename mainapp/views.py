from django.http import HttpResponse
from django.shortcuts import render
from .models import MyClass
import nltk
from nltk.corpus import treebank
from nltk.corpus import alpino as alp
from nltk.tag import UnigramTagger, BigramTagger


# Create your views here.

def index(request):
	if request.method == "POST":
		text =  request.POST.get('input')
		tokens = nltk.word_tokenize(text)
		tagged = nltk.pos_tag(tokens)
		context = { 'input': tagged}

	else:
		context = { 'input': "No Data" }
		
	return render(request,'mainapp/index.html',context)


