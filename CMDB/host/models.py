from django.db import models

# Create your models here.
class HostList(models.Model):
    hostname = models.CharField(max_length=32,null=True,verbose_name='主机名')
    ipaddress = models.CharField(max_length=32,null=True,verbose_name='IP地址')
    system = models.CharField(max_length=32, null=True, verbose_name='操作系统')
    cpu = models.CharField(max_length=32,null=True,verbose_name='CPU')
    mem = models.CharField(max_length=32,null=True,verbose_name='内存')
    disk = models.CharField(max_length=32,null=True,verbose_name='磁盘')
    region = models.ForeignKey(to='Region',null=True,verbose_name='区域')
    # computer_room = models.ManyToManyField(to='ComputerRoom',null=True,verbose_name='机房')
    computer_room = models.ForeignKey(to='ComputerRoom',null=True,verbose_name='机房')
    # application = models.ManyToManyField(to='Application',null=True,verbose_name='应用')
class Region(models.Model):
    name = models.CharField(max_length=32,null=True,verbose_name='区域')
    # computer_room = models.ManyToManyField(to='ComputerRoom',null=True,verbose_name='机房')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '区域表'
class ComputerRoom(models.Model):
    name = models.CharField(max_length=32,null=True,verbose_name='机房')
    # hosts = models.ManyToManyField(to='HostList', null=True, verbose_name='本机房所属主机')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '机房表'
# class Application(models.Model):
#     name = models.CharField(max_length=16, blank=True, null=True, verbose_name='应用')

class UserInfo(models.Model):
    username = models.CharField(max_length=32,null=True)
    password = models.CharField(max_length=32,null=True)

