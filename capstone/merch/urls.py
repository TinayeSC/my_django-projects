#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:43:41 2023

@author: sam
"""

from django.urls import path, include, re_path
from . import views


app_name = 'merch'
urlpatterns = [
    path('', views.clothes, name='merch')
  
]
