import json
import random

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from haiwei import models
from haiwei.models import food
# todo :design main UI
from haiwei.settings import BASE_DIR


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


def id_data(request):
    foods = food.objects.filter(id=request.GET['id'])
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def fname_data(request):
    foods = food.objects.filter(fname__contains=request.GET['fname'])
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def location_data(request):
    foods = food.objects.filter(location=request.GET['location'])
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    # print(request.GET['location'])
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def taste_data(request):
    foods = food.objects.filter(taste=request.GET['taste'])
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    # print(request.GET['location'])
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def random_data(request):
    # 随机函数
    foods = food.objects.filter(id=-1)
    while not foods.exists():
        random_id = random.randint(0, 99)
        foods = food.objects.filter(id=random_id)
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


# 上传
def upload(request):
    if request.method == 'POST':
        food = models.food(
            fname=request.POST['fname'],
            wname=request.POST['wname'],
            location=request.POST['location'],
            price=request.POST['price'],
            taste=request.POST['taste'],
            # imgid_1=request.POST['img'],
            # i_2 = request.POST['imgid_2']
            others=request.POST['others'],
            imgid_1=request.FILES.get('img')
        )
        food.save()
    # food.objects.create(
    #     imgid_1=i_1,
    #     # imgid_2=i_2,
    #     location=l,
    #     wname=w,
    #     fname=f,
    #     price=p,
    #     taste=t,
    #     others=o
    # )
    return render(request, 'uploads.html')


def r_upload(request):
    context = {

        'title': '海味管理',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'xxx': 'xxxxx'
    }
    return render(request, 'uploads.html', context)
