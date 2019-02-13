from django.shortcuts import render, redirect, HttpResponse
from salt.parsing import ResApi
from django.views import View
from utils import send_salt_api
from utils import form_class
from host import models
import requests
import json


class apilist(View):
    try:
        dic_li = send_salt_api.main()
    except requests.exceptions.ConnectionError:
        print('主机没有反应')
    def get(self, request):
        one_menu = request.session.get('one_menu')
        # print(request.GET.get('name'))
        if '1' == request.GET.get('name'):
            res = ResApi().parsing(self.dic_li)
            for k, v in res.items():
                dic = {}
                hostname = k
                ipaddress = v[0]
                system = v[1]
                mem = v[2]
                obj = models.HostList.objects.filter(ipaddress=ipaddress).first()
                if obj:
                    continue
                else:
                    models.HostList.objects.create(hostname=hostname, ipaddress=ipaddress, system=system, mem=mem)
            return redirect('/hostpage/')
        else:
            res = ResApi().parsing(self.dic_li)
            return render(request, 'apipage.html', locals())

    def post(self, request):
        one_menu = request.session.get('one_menu')
        cmd = request.POST.get('cmd')
        client = request.POST.get('client')
        # print(cmd,client)
        api = send_salt_api.SaltApi
        api_url = send_salt_api.salt_api
        salt = api(api_url)
        salt_client = client
        salt_test = 'test.ping'
        salt_method = 'cmd.run'
        salt_params = cmd
        result = salt.salt_command(salt_client, salt_method, salt_params)[client]
        # print(result['python'])
        # result1 = salt.salt_command(salt_client, salt_test)
        return render(request,'apipage.html',locals())
        res = ResApi().parsing(self.dic_li)
        for k, v in res.items():
            dic = {}
            hostname = k
            ipaddress = v[0]
            system = v[1]
            mem = v[2]
            obj = models.HostList.objects.filter(ipaddress=ipaddress).first()
            if obj:
                continue
            else:
                models.HostList.objects.create(hostname=hostname, ipaddress=ipaddress, system=system, mem=mem)
        return redirect('/hostpage/')

# class SendClient(View):
#     def get(self,req):
#         pass
#     def post(self,req):
#         api = send_salt_api.SaltApi
#         api_url = send_salt_api.salt_api
#         salt = api(api_url)
#         salt_client = '*'
#         salt_test = 'test.ping'
#         salt_method = 'grains.items'
#         result1 = salt.salt_command(salt_client, salt_test)
#         return render(req,'apipage.html',locals())
# # Create your views here.
# res = {}
# res.items()
