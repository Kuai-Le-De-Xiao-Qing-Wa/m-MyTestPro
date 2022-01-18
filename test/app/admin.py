import hashlib
import re

from django.contrib import admin
from django.http import HttpResponse, JsonResponse

from app.models import User as u

# Register your models here.
class User():
    def get_list(request):
        if request.method == "GET":
            ulist = u.objects.all()
            rlist = []
            for user in ulist:
                rlist.append({
                    'id':user.id,
                    'user_name':user.username,
                    'pwd':user.pwd,
                    'dt':user.create_time,
                })
            res = {'code':200,'msg':'123','data':rlist}
            return JsonResponse(res);
        else:
            return JsonResponse({'code':500,'msg':'请求错误'})

    def add_user(request):
        if request.method == "POST":
            req = request.POST
            key_flag = req.get('username') and req.get('pwd') and len(req)==2

            if key_flag:
                # 实例化MD5
                m = hashlib.md5()
                # 对密码进行一次加密
                m.update(req['pwd'].encode())
                # 第二次对密码进行加密处理
                m.update(m.hexdigest().encode())
                username = req['username']
                pwd = m.hexdigest()
                add_res = u(username=username, pwd=pwd)
                add_res.save()
                res = {'code':200,'msg':'添加成功','id':add_res.id,'date':add_res.create_time}
                return JsonResponse(res);
            else:
                return JsonResponse({'code': 500, 'msg': '添加失败'})
        else:
            return JsonResponse({'code': 500, 'msg': '请求错误'})

    def user_info(request,id):
        if request.method == "GET":
            info = u.objects.get(id=id)
            uinfo = []
            uinfo.append({
                'id': info.id,
                'user_name': info.username,
                'pwd': info.pwd,
                'dt': info.create_time,
            })
            res = {'code': 200, 'msg': '添加成功', 'res': uinfo}
            return JsonResponse(res);
        else:
            return JsonResponse({'code': 500, 'msg': '请求错误'})

    def updata_user(request,id):
        if request.method == "POST":
            req = request.POST
            try:
                old_user = u.objects.get(id=id)
                if req.get('username'):
                    username = req['username']
                    old_user.username = username
                if req.get('pwd'):
                    # p = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$"
                    bb = re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$", req['pwd'], flags=0)
                    if bb != None:
                        m = hashlib.md5()
                        # 对密码进行一次加密
                        m.update(req['pwd'].encode())
                        # 第二次对密码进行加密处理
                        m.update(m.hexdigest().encode())
                        pwd = m.hexdigest()
                        old_user.pwd = pwd
                    else:
                        return JsonResponse({"code": "500", "msg": "密码必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间"})

                old_user.save()
                return JsonResponse({"code":200,"msg":"修改成功"})
            except u.DoesNotExist:
                return JsonResponse({"code": "500", "msg": "修改失败"})
        else:
            return JsonResponse({'code':500,'msg':'请求错误'})

    def del_user(request,id):
        if request.method == "DELETE":
            try:
                del_data = u.objects.get(id=id)
                del_data.delete()
                return JsonResponse({'code':200,'msg':'删除成功','id':id})
            except u.DoesNotExist:
                return JsonResponse({'code':500,'msg':'删除失败'})
        else:
            return JsonResponse({'code':500,'msg':'请求错误'})
