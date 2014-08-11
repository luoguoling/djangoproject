__author__ = 'Administrator'
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^list/$','servermangerapp.views.list',name='servermangerapp_list'),
                       url(r'^head/$','servermangerapp.views.view',name='view'),
                       url(r'^head1/$','servermangerapp.views.view1',name='view1'),
                       url(r'^head2/$','servermangerapp.views.view2',name='view2'),
                       url(r'^head3/$','servermangerapp.views.view3',name='view3'),
                       url(r'^head4/$','servermangerapp.views.view4',name='view4'),
                       url(r'^upload/$','servermangerapp.views.upload',name='upload'),
                       url(r'^uploadmysql/$','servermangerapp.views.uploadmysql',name='uploadmysql'),
                       url(r'login/$','servermangerapp.views.login',name='login'),
                       url(r'index/$','servermangerapp.views.index',name='index'),
                       url(r'logout/$','servermangerapp.views.logout',name='logout'),
                       )
