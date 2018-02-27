# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
import models
import json


# 转换成json形式
def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr


# 查询首页新闻类型
def type_list(request):
    all_type = models.messageType.objects.all()
    all_dicts = toDicts(all_type)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询新闻信息
def list(request):
    typ = request.GET.get('id')
    print id
    all_objs = models.main_message.objects.all()
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询服务类型
def service_list(request):
    all_type = models.service_type.objects.all()
    all_dicts = toDicts(all_type)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询类型子类别
def service_detail_list(request):
    all_type = models.service_detail_type.objects.all()
    all_dicts = toDicts(all_type)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询服务信息
def service_message(request):
    all_type = models.service_message.objects.all()
    all_dicts = toDicts(all_type)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)
