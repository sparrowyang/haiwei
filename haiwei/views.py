from django.shortcuts import render


# todo :design main UI
def index(request):

	#渲染内容
    context = {

        'title': '海味',# 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'xxx':'xxxxx'
    }

    return render(request, 'index.html', context)
