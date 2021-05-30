import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from haiwei.models import food


# todo :design main UI


def index(request):
    # 渲染内容
    theme = request.session.get('theme', None)
    customlr = request.session.get('customlr',None)
    context = {
        'title': '海味',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'customlr':customlr,
        'theme': theme,
        'xxx': 'xxxxx'
    }
    return render(request, 'index.html', context)

def setting(request):
    customlr = request.session.get('customlr',None)
    theme = request.session.get('theme',None)
    context = {
        'title': '海味',  # 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'customlr':customlr,
        'theme':theme,
        'checked':'',
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
    foods = food.objects.filter(taste=request.GET['taste'])
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    data = {'status': 'success', 'code': '200', 'items': t}
    # print(request.GET['location'])
    return HttpResponse(json.dumps(data, ensure_ascii=False))


# 上传
def upload(request):
    f = request.POST['fname']
    w = request.POST['wname']
    l = request.POST['location']
    p = request.POST['price']
    t = request.POST['taste']
    i_1 = request.POST['img']
    # i_2 = request.POST['imgid_2']
    o = request.POST['others']
    food.objects.create(
        imgid_1=i_1,
        # imgid_2=i_2,
        location=l,
        wname=w,
        fname=f,
        price=p,
        taste=t,
        others=o
    )
    return render(request, 'uploads.html')


def r_upload(request):
    user = request.session.get('user',None)
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