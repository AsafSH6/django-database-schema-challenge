# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpRequest
from django.shortcuts import render


def index(request):
    return HttpRequest("Supppp?")
