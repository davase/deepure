from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from app01.models import *
import json

#用户注册
def register(request):
    if request.method=='POST':
        #code 0:正常代码  -1:代码错误
        code = 0
        #message 返回信息
        message = ""
        resultdata = {}
        body=request.body
        data = json.loads(body)
        name = data.get('name', '')
        mpno = data.get('mpno', '')
        openid = data.get('openid', '')
        sex = data.get('sex', '')
        age = data.get('age', '')
        bmi = data.get('bmi', '')
        bodyfatratio = data.get('bodyfatratio', '')
        other = data.get('other', '')
        if name =="":
            code = -1
            message = "姓名不能为空"
        if mpno =="":
            code = -1
            message = "手机号不能为空"
        # if openid =="":
        #     code = -1
        #     message = "open_id不能为空"
        if sex =="":
            code = -1
            message = "性别不能为空"
        if age =="":
            code = -1
            message = "年龄不能为空"
        if bmi =="":
            code = -1
            message = "bmi不能为空"
        if bodyfatratio =="":
            code = -1
            message = "体脂率不能为空"
        if other =="":
            code = -1
            message = "锻炼习惯不能为空"
        if code == 0:
            if Deepureuser.objects.filter(mpno=mpno, openid=openid).all():
                #用户已报名
                code = "-1"
                message="用户已报名"
            else:
                #用户未报名
                # user_result = Deepureuser(name=name, mpno=mpno, openid=openid, sex=sex, age=age, bmi=bmi,
                #                       bodyfatratio=bodyfatratio, other=other)
                # res = user_result.save()
                # user_result = Deepureuser(name=name, mpno=mpno, openid=openid,sex=1,age=2, bmi=23.12, bodyfatratio=20.1,other='1,2,3,4')
                task_info = Deepureuser.objects.create(name=name, mpno=mpno, openid=openid, sex=sex, age=age, bmi=bmi,
                                      bodyfatratio=bodyfatratio, other=other)
                if task_info.id > 0:
                    message = "数据添加成功"
                else:
                    code = -1
                    message = "用户添加失败"
            resultdata = {"code": code, "message": message}
        else:
            # 返回错误信息
            resultdata = {"code":code,"message":message}
        return JsonResponse(resultdata)

#用户注册
def userregister(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'sumbituser.html', context)