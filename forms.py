#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:47:06 2019

@author: laura
"""

from django import forms

class TodoForm(forms.Form):
  content = forms.CharField(
            widget = forms.TextInput(
                    attrs={'class':'form-control', 'placeholder':'todo', 
                           'aria-label':'Todo', 'aria-describedby':'add-btn'}))
  