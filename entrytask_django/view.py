# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import JsonResponse
import json
from testmodel.models import entrytask
from django.views.decorators.http import require_http_methods
from django.core import serializers
import traceback

from testmodel.models import entrytask
# def hello(request):
#     return HttpResponse("Hello world ! ")


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

@require_http_methods(["GET"])
def query_account_get_test(request):
    response = {}
    user_name = request.GET.get('user_name')
    product_price = float(request.GET.get('product_price'))
    product_discount = float(request.GET.get('product_discount'))
    product_final_price = round(product_price * product_discount, 2)
    print(product_final_price)

    try:
        entrytasks_filter = entrytask.objects.filter()
        print(entrytasks_filter)
        print(entrytask.objects.all().values('name'))
        entrytasks = entrytask.objects.get(name=user_name)
        print(entrytasks.name)

        if(user_name == entrytasks.name) and (product_final_price < entrytasks.account):        # 逻辑与运算
            print(entrytask.objects.all().values('name'))
            response['result'] = 0
            response['buy'] = 1
            response['account'] = entrytasks.account
            response['list'] = json.loads(serializers.serialize("json", entrytasks_filter))
        else:
            response['result'] = 1
            response['buy'] = 0
            response['account'] = entrytasks.account
            response['list'] = json.loads(serializers.serialize("json", entrytasks_filter))

    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        traceback.print_exc()

    return JsonResponse(response)

# 表单
# def query_account_get_form(request):
#     context = {'foo': 'bar'}
#     return render(request, 'post.html', context)

# 接收GET请求数据
# def query_account_get(request):
#     request.encoding='utf-8'
#     if 'q' in request.GET and request.GET['user_name']:
#         message = '你搜索的内容为: ' + request.GET['user_name']
#     else:
#         message = '你提交了空表单'
#     return HttpResponse(message)

# 接收POST请求数据
# @require_http_methods(["POST"])
def query_account(request):
    # ctx ={}
    # if request.POST:
    #     ctx['rlt'] = request.POST['user_name']
    # return render(request, "post.html", ctx)
    response = {"resCode": '0', "message": 'success',"data": []}
    user_name = json.loads(request.POST.get('user_name'))
    product_price = json.loads(request.POST.get('product_price'))
    product_discount = json.loads(request.POST.get('product_discount'))
    product_final_price = product_price * product_discount
    try:
        response['msg'] = "success"
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        traceback.print_exc()
    return JsonResponse(response)
