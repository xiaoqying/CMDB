from builtins import locals
from django.shortcuts import render,HttpResponse,redirect
from host import models
from django.views import View
from utils import form_class
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password, check_password
import hashlib
from host import models
# Create your views here.
class User(View):
    def get(self,request):
        one_menu = request.session.get('one_menu')
        print('user---->',one_menu)
        obj = models.UserInfo.objects.all()
        menu_list=request.session.get('menu_list')

        return render(request,'user.html',locals())

    def post(self, request):
        pass

class add(View):
    def get(self,request):
        one_menu = request.session.get('one_menu')
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
                return redirect('/host/hostpage/')
            else:
                # print(1111)
                return render(request, 'add.html', locals())
        except AttributeError:
            return render(request, 'add.html', locals())
        return redirect('/host/hostpage/')

class delete(View):
    def get(self,request):
        pass

    def post(self, request):
        pass

class update(View):
    def get(self,request):
        pass

    def post(self, request):
        pass