# -*- coding: UTF-8 -*-
from django.shortcuts import render
from news.models import New


def index(request):
    new = New.objects.all()[0]
    id = new.id - 1
    return render(request, 'index.html', locals())

