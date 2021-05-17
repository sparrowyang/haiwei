import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from haiwei.models import food


# todo :design main UI
def index(request):
    # 渲染内容
    context = {

        'title': '海味',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'xxx': 'xxxxx'
    }
    return render(request, 'index.html', context)


def all_data(request):
    foods = food.objects.all()
    # res = {'status': 'success', 'code': '200', 'items': foods}
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    # data = {
    #     'patient_name': '张三',
    #     'age': '25',
    #     'patient_id': '19000347',
    #     '诊断': '上呼吸道感染',
    # }
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def location_data(request):
    foods = food.objects.filter(location='request')
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def upload(request):
    context = {

        'title': '海味管理',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'xxx': 'xxxxx'
    }
    return render(request, 'upload.html', context)
