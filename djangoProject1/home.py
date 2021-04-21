from django.http import HttpResponse
import json

def index():
    json_data = {
        'title':'海味'
    }
    return HttpResponse(json.dumps(json_data))