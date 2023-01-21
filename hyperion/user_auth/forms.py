#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:52:10 2023

@author: sam
"""

from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import  User

# Create your forms here.

        
        
        
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
 
        fields = ['first_name','last_name','username','email','password1','password2']
        