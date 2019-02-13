#/usr/bin/python
#coding:utf8
from host import models
class InitMenu(object):
    def initMenu(self,username):
        obj = models.UserInfo.objects.filter(username=username).first()
        menu_list = []
        one_menu = {}
        for i in models.Menu.objects.all():
            menu_list.append(i.title)
            one_menu[i.title] = {}
        # print('menu_list----->>>', one_menu)
        if obj:
            a = obj.roles.all().first().permissions.all()
            # print(a)
            for i in a:

                for j in range(0, len(menu_list)):
                    try:
                        if i.menu.title == menu_list[j]:
                            # one_menu['主机管理']={}
                            one_menu[menu_list[j]][i.title] = i.url
                    except KeyError:
                        print('5555555')

                # print(i.menu.title,'----->',i.title,'+++++++>',i.url)
                # one_menu['one_menu']=i.menu.title
                # two_menu['two_menu']=i.title
                # url_list['url_list']=i.url
        print('menu_list----->>>', one_menu)
        return one_menu