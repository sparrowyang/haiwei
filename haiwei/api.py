from django.http import HttpResponse
import json


'''
api 函数模板
参数: request 请求参数
返回值是一个 json 数据，供js解析
def get_xxxxx(request):
	items = []
	
	# do something here.
	
	res = {'status':'success','code':'200',items':items}
	return HttpResponse(json.dumps(res,ensure_ascii=False))
'''


def main_data(request):

    items = [
        {
            'id':1,'imgid':'mlj','locate':'第一食堂','wname':'铁板烧','fname': '腊肠炒饭','price': '9','taste': '适中','other': '',
        },
        {
            'id':2,'imgid' : 'mlj','locate': '第一食堂', 'wname': '铁板烧', 'fname': '牛肉炒饭', 'price': '12', 'taste': '适中', 'other': '',
        },
        {
            'id':3,'imgid':'mlj','locate': '第二食堂', 'wname': '山西面食', 'fname': '阳春面', 'price': '8', 'taste': '清淡', 'other': '',
        }
    ]

    res = {'status':'success','code':'200','items':items}
    return HttpResponse(json.dumps(res,ensure_ascii=False))
	
def get_type(request):
	item = []
	res = {'status':'success','code':'200','items':items}
	return HttpResponse(json.dumps(res,ensure_ascii=False))