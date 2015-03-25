# -*- coding:iso-8859-1 -*-
from django.shortcuts import render, HttpResponse
from news.models import New
import urllib
import re, json
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def news(request, id):
    id = int(id)
    cur_page = 0
    news_list = New.objects.all()
    for news in news_list:
        cur_page += 1
        if news.id == id:
            break

    cur_page = (cur_page - 1) / 7 + 1

    while id > 0:
        if New.objects.filter(id=id).exists():
            new = New.objects.get(id=id)
            break
        id -= 1

    if id == 0:
        new = New.objects.all()[0]

    id = new.id - 1

    return render(request, 'news.html', locals())


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5' \
        and uchar not in ['年', '月', '日']:
        return True
    else:
        return False

def page(request, page_id):
    page_id = int(page_id)
    if page_id < 0:
        page_id = 1

    start = (page_id - 1) * 7
    end = page_id  * 7 
    
    max_page = (New.objects.count() - 1) / 7 + 1

    new_list = New.objects.all()[start:end]

    for news in new_list:
        preview = ''
        total = 0
        for ch in news.content:
            if is_chinese(ch):
                preview += ch
                total += 1
                if total > 50:
                    break
        news.preview = preview
        news.save()
    
    pre_page = page_id - 1
    next_page = page_id + 1


    return render(request, 'new_list.html', locals())
    

