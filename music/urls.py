from django.conf.urls import url
from . import views


urlpatterns = [

	#by default url /
    url(r'^$' , views.index, name='index'),

    #for showing the details #/music/712->id
    url(r'^(?P<album_id>[0-9]+)/$' , views.details, name='details'),

    #for sample form
    url(r'^myform/$' , views.form, name='form'),
]
