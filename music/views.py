from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums}
	return render(request,'music/index.html',context)


def details(request,album_id):
	try:
		album = Album.objects.get( pk = album_id )
	except Album.DoesNotExist:
		raise Http404("Album doesnt exist")

	return render(request,'music/details.html', {'album': album } )

def form(request):

	if request.method == "POST":
		para = request.POST.get('paragraph')
		length = len(para)
		context = { 'para': para, 'length': length }
	else:
		para1 = "no data"
		length1 = 0
		context = { 'para': para1, 'length': length1 }
		 
	return render(request,'music/form.html', context)		