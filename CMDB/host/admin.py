from django.contrib import admin
from host import models
# Register your models here.

class PermissionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'menu', 'parent', 'name']  # 展示的字段
    list_editable = ['url', 'menu', 'parent', 'name']  # 编辑的字段


class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'weight']  # 展示的字段
    list_editable = ['icon', 'weight']  # 编辑的字段


admin.site.register(models.Permission, PermissionModelAdmin)
admin.site.register(models.Role)
admin.site.register(models.UserInfo)
admin.site.register(models.Menu, MenuModelAdmin)
