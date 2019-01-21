from django.shortcuts import render,HttpResponse,redirect
from host import models
from django.views import View
from utils import form_class
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password, check_password
import hashlib
#登录页面
class login(View):
    def get(self,request):
        form = form_class.UserForm()
        return render(request, 'login.html',locals())
    def post(self,request):
        form = form_class.UserForm(request.POST)
        #判断输入数据是否存在
        if form.is_valid():
            user = form.cleaned_data['user']
            pwd = form.cleaned_data['pwd']
            # pwd = make_password(form.cleaned_data.get('pwd'),'pbkdf2_sha256')
            # print(pwd)
            obj = models.UserInfo.objects.filter(username=user).first()
            #判断用户名是否存在
            if obj:
                #判断密码是否对应正确,使用django自带加密算法功能
                if  check_password(pwd,obj.password):
                    # print(check_password(pwd,obj.password),pwd,obj.password)
                    res = redirect('/hostpage/')
                    res.set_cookie('username',user,max_age=1110)
                    return res
                else:
                    #密码不正确
                    error_msg = '用户名或密码错误！'
                    return render(request, 'login.html', locals())
            else:
                # 密码不正确
                error_msg = '用户名或密码错误！'
                return render(request,'login.html',locals())
        #如果输入数据不存在
        else:
            form = form_class.UserForm(request.POST)
            return render(request, 'login.html',locals())
#资产管理
class hostpage(View):

    def get(self,request,*args,**kwargs):
        obj_li = models.HostList.objects.all()
        p = Paginator(obj_li, 10)
        last_page = max([i for i in p.page_range])
        get_page = int(request.GET.get('page', 1))
        try:
            obj_li = p.page(get_page)  # obj_li此时已经重新赋值，有分页的方法
        except PageNotAnInteger:
            obj_li = p.page(1)
        except EmptyPage:
            obj_li = p.page(p.num_pages)
        return render(request, 'hostpage.html', locals())
    def post(self):
        pass
#增
class add(View):
    def get(self,request):
        form =form_class.HostForm()
        return render(request,'add.html',locals())
    def post(self,request):
        form = form_class.HostForm(data=request.POST)
        # print('add_post')
        try:
            if form.is_valid():
                # print(form.cleaned_data)
                # print(type(form.cleaned_data['region_id']))
                models.HostList.objects.create(**form.cleaned_data)
                return redirect('/hostpage/')
            else:
                # print(1111)
                return render(request, 'add.html', locals())
        except AttributeError:
            return render(request, 'add.html', locals())
        return redirect('/hostpage/')
#删
class delete(View):
    def post(self,request,*args):
        print(222222222,args)
    def get(self,request,*args,**kwargs):
        # print(request.META['HTTP_REFERER'])
        url = request.META['HTTP_REFERER']
        get_id = int(request.GET.get('id'))
        models.HostList.objects.filter(id=get_id).delete()
        # return redirect('/hostpage/')
        return redirect(url)
#改
class update(View):
    def get(self,request,getid):
        getid = getid
        obj = models.HostList.objects.filter(id=getid).first()
        form = form_class.HostForm(
            initial={
                'hostname':obj.hostname,
                'ipaddress':obj.ipaddress,
                'cpu':obj.cpu,
                'mem':obj.mem,
                'disk':obj.disk,
                'region':obj.region,
                'system':obj.system,
            }
        )
        return render(request,'update.html',locals())

    def post(self,request,getpid):
        try:
            form = form_class.HostForm(data=request.POST)
            # print('post',getpid)
            if form.is_valid():
                # print(form.cleaned_data)
                ong = models.HostList.objects.filter(id=getpid).update(**form.cleaned_data)
                # ong.update(**form.cleaned_data)
                return redirect('/hostpage/')
        except AttributeError:
            return render(request,'update.html',locals())
        return redirect('/hostpage/')

#注册页面
class register(View):
    def get(self,request):
        form = form_class.RegisterForm()
        # print('register_get')
        return render(request, 'register.html', locals())
    def post(self,request):
        form = form_class.RegisterForm(request.POST)
        if form.is_valid():
            print('加密前')
            obj=models.UserInfo.objects.filter(username=form.cleaned_data.get('username')).first()
            if not obj:
            #,使用django自带加密算法功能，将密码加密
                form.cleaned_data['password'] = make_password(form.cleaned_data.get('password'),'pbkdf2_sha256')
                models.UserInfo.objects.create(**form.cleaned_data)
                return redirect('/login/')
            else:
                error_msg = '用户名已存在'
                return render(request,'register.html',locals())
        else:
            print('errors--->',form.errors)
            return render(request,'register.html',locals())
#退出
class logout(View):
    def post(self,request):
        pass
    def get(self,request):
        request.COOKIES.clear()
        print(request.COOKIES.get('password'))

        return redirect('/login/')
#查询
class search(View):
    def get(self):
        pass
    def post(self):
        pass

# #认证COOKIES
# def auth(func):
#     def inner(request,*args,**kwargs):
#         v = request.COOKIES.get('username')
#
#         if not v:
#             return redirect('/login/')
#         return func(request,*args,**kwargs)
#     return inner
# #CBV
# @method_decorator(auth,name='dispatch')
# class Order(View):
#     def get(self,request):
#         v = request.COOKIES.get('username')
#
#         print(v)
#         return render(request,'hostpage.html',locals())
#
#     def post(self,request):
#         v = request.COOKIES.get('username')
#         print(v)
#
#         return render(request, 'hostpage.html', locals())