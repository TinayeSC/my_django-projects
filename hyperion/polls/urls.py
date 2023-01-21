#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:43:41 2023

@author: sam
"""

from django.urls import path, include, re_path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
	
  
]

import user_auth 
from user_auth import views

urlpatterns.append( path('user_auth',views.authenticate_user, name='login'))