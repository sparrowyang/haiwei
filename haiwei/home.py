from django.http import HttpResponse
import json

def main_data(request):

    items = [
        {
            'locate':'第一食堂','wname':'铁板烧','fname': '腊肠炒饭','price': '9','taste': '适中','other': '',
        },
        {
            'locate': '第一食堂', 'wname': '铁板烧', 'fname': '牛肉炒饭', 'price': '12', 'taste': '适中', 'other': '',
        },
        {
            'locate': '第二食堂', 'wname': '山西面食', 'fname': '阳春面', 'price': '8', 'taste': '清淡', 'other': '',
        }
    ]

    res = {'status':'200','items':items}
    return HttpResponse(json.dumps(res,ensure_ascii=False))