import json
import random

from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from haiwei import models
from haiwei.models import food


# todo :design main UI


def index(request):
    # 渲染内容
    theme = request.session.get('theme', None)
    customlr = request.session.get('customlr', None)

    if customlr == None:
        request.session['theme'] = 'amber'

    context = {
        'title': '海味',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'customlr': customlr,
        'theme': theme,
        'xxx': 'xxxxx'
    }
    return render(request, 'index.html', context)


def setting(request):
    customlr = request.session.get('customlr', None)
    theme = request.session.get('theme', None)
    context = {
        'title': '海味',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'customlr': customlr,
        'theme': theme,
        'checked': '',
        'xxx': 'xxxxx'
    }
    return render(request, 'setting.html', context)


def save_settting(request):
    lr = request.GET['customlr']
    theme = request.GET['theme']
    request.session['customlr'] = lr
    request.session['theme'] = theme
    data = {'status': 'success', 'code': '200'}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


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
    tastes = request.GET['taste']
    print(tastes)
    tastes = tastes.split("*")
    print(tastes)
    foods = food.objects.filter(taste__in=tastes)
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def random_data(request):
    # 随机函数
    foods = food.objects.filter(id=-1)
    id_s = []
    for i in range(0, 10):
        id_s.append(random.randint(0, 100))
    print("test",1)
    while not foods.exists():
        foods = food.objects.filter(id__in=id_s)
    print("test",2)
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


# 上传
def upload(request):
    if request.method == 'POST':
        foods = models.food(
            fname=request.POST['fname'],
            wname=request.POST['wname'],
            location=request.POST['location'],
            price=request.POST['price'],
            taste=request.POST['taste'],
            others=request.POST['others'],
            imgid_1=request.FILES.get('img')
        )
        foods.save()
    return render(request, 'uploads.html')


def r_upload(request):
    user = request.session.get('user', None)
    context = {
        'title': '海味管理',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'xxx': 'xxxxx'
    }
    if user != 'admin':
        return render(request, 'login.html', context)
    return render(request, 'uploads.html', context)


def r_login(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    if uname == 'admin' and pwd == 'admin':
        request.session['user'] = 'admin'
    return HttpResponseRedirect('/uploads/')

def r_logout(request):
    request.session['user'] = None
    data = {'status': 'success', 'code': '200', 'msg': 'logout successful!'}
    return HttpResponse(json.dumps(data, ensure_ascii=False))