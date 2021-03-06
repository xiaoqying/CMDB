from builtins import locals
from django.shortcuts import render,HttpResponse,redirect
from host import models
from django.views import View
from utils import form_class,init_menu
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
            one_menu=init_menu.InitMenu().initMenu(user)
            print('全体散开',one_menu)
            #
            # for i in one_menu:
            #
            #     for j in one_menu[i]:
            #
            #         print('->>>>',j)
            #判断用户名是否存在
            if obj:
                #判断密码是否对应正确,使用django自带加密算法功能
                if  check_password(pwd,obj.password):
                    obj1 = models.UserInfo.objects.filter(username=user).first().roles.all()
                    # a=obj1.roles.all()
                    menu_list = []
                    permission_list =[]
                    obj2 = models.Menu.objects.all()
                    for i in obj2:
                        if i.title not in menu_list:
                            menu_list.append(i.title)
                    request.session['menu_list'] = menu_list
                    # print('+++++',menu_list)
                    for i in obj1:
                        for j in i.permissions.all():
                            permission_list.append(j.url)
                            # print(permission_list)
                            # if j.menu.title not in menu_list:
                            #     menu_list.append(j.menu.title)
                            #     print('-',j.menu.title,j.url)
                            # request.session['menu_list'] = menu_list
                    request.session['permission_list']=permission_list
                    request.session['one_menu']=one_menu
                    # print(permission_list)
                    # print( request.session.get('permission_list'),request.session.get('menu_list'))
                    # print(check_password(pwd,obj.password),pwd,obj.password)
                    # res = redirect('/host/hostpage/')
                    # res = render(request, 'hostpage.html', locals())
                    # res.set_cookie('username', user, max_age=1110)
                    #
                    # return res
                    # return redirect('/host/index')

                    return render(request, 'hostpage.html', locals())
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
        one_menu = request.session.get('one_menu')
        # print('hostpage---->',request.session.get('menu_list'))
        menu_list=request.session.get('menu_list')
        obj_li = models.HostList.objects.all()
        p = Paginator(obj_li, 10)
        last_page = max([i for i in p.page_range])
        get_page = int(request.GET.get('page', 1))
        permission_list=request.session.get('permission_list')
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
        one_menu = request.session.get('one_menu')
        form =form_class.HostForm()
        return render(request,'add.html',locals())
    def post(self,request):
        one_menu = request.session.get('one_menu')
        form = form_class.HostForm(data=request.POST)
        # print('add_post')
        try:
            if form.is_valid():
                # print(form.cleaned_data)
                # print(type(form.cleaned_data['region_id']))
                models.HostList.objects.create(**form.cleaned_data)
                return redirect('/host/hostpage/')
            else:
                # print(1111)
                return render(request, 'add.html', locals())
        except AttributeError:
            return render(request, 'add.html', locals())
        return redirect('/host/hostpage/')
#删
class delete(View):
    def post(self,request,*args):
        print(222222222,args)
        one_menu = request.session.get('one_menu')
    def get(self,request,*args,**kwargs):
        # print(request.META['HTTP_REFERER'])
        one_menu = request.session.get('one_menu')
        url = request.META['HTTP_REFERER']
        get_id = int(request.GET.get('id'))
        models.HostList.objects.filter(id=get_id).delete()
        # return redirect('/hostpage/')
        return redirect(url)
#改
class update(View):
    def get(self,request,getid):
        one_menu = request.session.get('one_menu')
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
        one_menu = request.session.get('one_menu')
        try:
            form = form_class.HostForm(data=request.POST)
            # print('post',getpid)
            if form.is_valid():
                # print(form.cleaned_data)
                ong = models.HostList.objects.filter(id=getpid).update(**form.cleaned_data)
                # ong.update(**form.cleaned_data)
                return redirect('/host/hostpage/')
        except AttributeError:
            return render(request,'update.html',locals())
        return redirect('/host/hostpage/')

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
                return redirect('/host/login/')
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
        request.session.clear()
        print(request.COOKIES.get('password'))

        return redirect('/host/login/')
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
class index(View):
    def get(self,request):
        menu_list = request.session.get('menu_list')
        permission_list = request.session.get('permission_list')
        print('index_page---->',menu_list)
        return render(request,'base.html',locals())
    def post(self,request):
        pass

class login1(View):
    def get(self,request):
        print('---------------->',request.session.get('one_menu'))
        one_menu = request.session.get('one_menu')
    #     for i in models.Menu.objects.all():
    #         menu_list.append(i.title)
    #         one_menu[i.title] = {}
    #     print('menu_list----->>>',one_menu)
    #     if obj:
    #         a = obj.roles.all().first().permissions.all()
    #         # print(a)
    #         for i in a:
    #
    #             for j in range(0,len(menu_list)):
    #                 try:
    #                     if i.menu.title == menu_list[j]:
    #                         # one_menu['主机管理']={}
    #                         one_menu[menu_list[j]][i.title]=i.url
    #                 except KeyError:
    #                     print('5555555')
    #
    #
    #             # print(i.menu.title,'----->',i.title,'+++++++>',i.url)
    #             # one_menu['one_menu']=i.menu.title
    #             # two_menu['two_menu']=i.title
    #             # url_list['url_list']=i.url
    #         print(one_menu)
    #         # print(a.name)
    #
    #     # print(obj)
    #     return HttpResponse('1111111111')
    def post(self,request):
        pass


