from django.shortcuts import render


def open(request):
    #渲染内容
    context = {
        'name': '麻辣鸡反',# 这会将模板中{{title}} 字段渲染为冒号右边的字符串
        'dec':'啦啦啦啦啦啦了阿三大赛的阿斯顿阿斯顿阿三开机的阿克苏记得很卡死极好的阿卡教授大声疾呼耷拉是耷拉和耷拉是耷拉上来看将散开来极好的'
    }
    return render(request, 'detail.html', context)