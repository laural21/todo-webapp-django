#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:39:09 2019

@author: laura
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deselect/<todo_id>', views.deselectTodo, name='deselect'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted')
]
