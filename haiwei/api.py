import json

from django.core import serializers
from django.http import HttpResponse

from haiwei.models import food


def main_data(request):
    items = [
        {
            'id': 1, 'imgid': 'mlj', 'locate': '第一食堂', 'wname': '铁板烧', 'fname': '腊肠炒饭', 'price': '9', 'taste': '适中',
            'other': '',
        },
        {
            'id': 2, 'imgid': 'mlj', 'locate': '第一食堂', 'wname': '铁板烧', 'fname': '牛肉炒饭', 'price': '12', 'taste': '适中',
            'other': '',
        },
        {
            'id': 3, 'imgid': 'mlj', 'locate': '第二食堂', 'wname': '山西面食', 'fname': '阳春面', 'price': '8', 'taste': '清淡',
            'other': '',
        }
    ]

    res = {'status': 'success', 'code': '200', 'items': items}
    return HttpResponse(json.dumps(res, ensure_ascii=False))


def get_type(request):
    items = []
    res = {'status': 'success', 'code': '200', 'items': items}
    return HttpResponse(json.dumps(res, ensure_ascii=False))


def get_id(id_n):
    foods = food.objects.filter(id == id_n)
    res = serializers.serialize('json', foods)
    t = json.loads(res)
    return t
