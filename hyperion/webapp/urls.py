#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:28:56 2023

@author: sam
"""

from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
]