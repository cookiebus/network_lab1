# -*- coding: UTF-8 -*-
from django.shortcuts import render
from news.models import New

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5' \
        and uchar not in ['年', '月', '日']:
        return True
    else:
        return False

def index(request):
    new_list = New.objects.all()
    if len(new_list) > 7:
        new_list = new_list[:7]

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

    pre_page = 0
    next_page = 2
    max_page = (New.objects.count() - 1) / 7 + 1

    return render(request, 'new_list.html', locals())

