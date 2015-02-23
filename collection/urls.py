'''
Created on 16 Feb 2015

@author: marklewis
'''
from django.conf.urls import patterns, url

from collection import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'))