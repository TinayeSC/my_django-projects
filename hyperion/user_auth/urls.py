#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:27:02 2023

@author: sam
"""
from django.urls import path, include, re_path
from . import views
from django.apps import apps

app_name = 'user_auth'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('register/',views.registration_page, name='register'),
    path('',views.registration_page, name='register')
]