from django.conf.urls import *

urlpatterns = patterns('analysis.analysis.views',
	url(r'^$', 'inicio', name="inicio"),
    #url(r'^salidas/$', 'post', name='salidas'),
    url(r'^output1/$', 'output1', name='output1'),
    url(r'^output2/$', 'output2', name='output2'),
    url(r'^output3/$', 'output3', name='output3'),
    url(r'^output4/$', 'output4', name='output4'),
    url(r'^output5/$', 'output5', name='output5'),
    url(r'^output5b/$', 'output5b', name='output5b'),
    url(r'^output6/$', 'output6', name='output6'),
    url(r'^output7/$', 'output7', name='output7'),
    url(r'^output8/$', 'output8', name='output8'),
    url(r'^output9/$', 'output9', name='output9'),
    url(r'^output10/$', 'output10', name='output10'),
    url(r'^output11/$', 'output11', name='output11'),
    url(r'^output12/$', 'output12', name='output12'),
    url(r'^output13/$', 'output13', name='output13'),
    url(r'^output14/$', 'output14', name='output14'),
    url(r'^output15/$', 'output15', name='output15'),
    url(r'^output16/$', 'output16', name='output16'),
    url(r'^output17/$', 'output17', name='output17'),
    url(r'^output18/$', 'output18', name='output18'),
    url(r'^output19/$', 'output19', name='output19'),
    url(r'^output20/$', 'output20', name='output20'),
    
    )