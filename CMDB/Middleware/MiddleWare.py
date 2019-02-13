from django.shortcuts import render,HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin

# #认证COOKIES
# def auth(func):
#     def inner(request,*args,**kwargs):
#         v = request.COOKIES.get('username')
#         if not v:
#             return redirect('/login/')
#         return func(request,*args,**kwargs)
#     return inner
#CBV
# @method_decorator(auth,name='dispatch')
class Order(MiddlewareMixin):
    white_list = ['/login/','/register/','/admin/','/admin/login/?next=/admin/']
    def process_request(self, request):
        url = request.path_info
        if not  url in self.white_list   :
            if not request.COOKIES.get('username'):
                return redirect('/login/')
