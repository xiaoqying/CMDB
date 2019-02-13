from django.db import models

# Create your models here.
class HostList(models.Model):
    hostname = models.CharField(max_length=32,blank=True,null=True,verbose_name='主机名')
    ipaddress = models.CharField(max_length=32,blank=True,null=True,verbose_name='IP地址')
    system = models.CharField(max_length=32, blank=True,null=True, verbose_name='操作系统')
    cpu = models.CharField(max_length=32,blank=True,null=True,verbose_name='CPU')
    mem = models.CharField(max_length=32,blank=True,null=True,verbose_name='内存')
    disk = models.CharField(max_length=32,blank=True,null=True,verbose_name='磁盘')
    region = models.ForeignKey(to='Region',blank=True,null=True,verbose_name='区域')
    # computer_room = models.ManyToManyField(to='ComputerRoom',null=True,verbose_name='机房')
    computer_room = models.ForeignKey(to='ComputerRoom',null=True,verbose_name='机房')
    # application = models.ManyToManyField(to='Application',null=True,verbose_name='应用')
class Region(models.Model):
    name = models.CharField(max_length=32,blank=True,null=True,verbose_name='区域')
    # computer_room = models.ManyToManyField(to='ComputerRoom',null=True,verbose_name='机房')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '区域表'
class ComputerRoom(models.Model):
    name = models.CharField(max_length=32,blank=True,null=True,verbose_name='机房')
    # hosts = models.ManyToManyField(to='HostList', null=True, verbose_name='本机房所属主机')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '机房表'
# class Application(models.Model):
#     name = models.CharField(max_length=16, blank=True, null=True, verbose_name='应用')
################用户表######################################
class UserInfo(models.Model):
    username = models.CharField(max_length=32,blank=True,null=True,verbose_name='用户名')
    password = models.CharField(max_length=128,blank=True,null=True,verbose_name='密码')
    roles = models.ManyToManyField('Role', verbose_name='用户拥有的角色', blank=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = '用户信息'
        verbose_name = '用户信息'


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, verbose_name='名称')
    permissions = models.ManyToManyField('Permission', verbose_name='角色拥有的权限', blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '岗位'
        verbose_name = '岗位'

class Permission(models.Model):
    """
    权限表
    可以做二级菜单的权限   menu 关联 菜单表
    不可以做菜单的权限    menu=null
    """
    url = models.CharField(max_length=32, verbose_name='权限')
    title = models.CharField(max_length=32, verbose_name='标题')
    menu = models.ForeignKey('Menu', null=True, blank=True)
    # 自己关联自己
    parent = models.ForeignKey('self', null=True, blank=True)
    # 写法二
    # parent = models.ForeignKey('Permission', null=True, blank=True)
    name = models.CharField(max_length=32, verbose_name='URL别名')

    class Meta:
        verbose_name_plural = '权限'
        verbose_name = '权限'

    def __str__(self):
        return self.title

class Menu(models.Model):
    """
    菜单表  一级菜单
    """
    title = models.CharField(max_length=32)
    icon = models.CharField(max_length=64, null=True, blank=True, verbose_name='图标')
    # 默认值为1
    weight = models.IntegerField(default=1, verbose_name='显示权重')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '一级菜单'
        verbose_name = '一级菜单'




