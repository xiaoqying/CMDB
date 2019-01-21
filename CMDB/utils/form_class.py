from django import forms
from django.forms import fields
from django.forms import widgets
from host import models

class UserForm(forms.Form):
    user = fields.CharField(error_messages={'required':'用户名不能为空'})
    pwd = fields.CharField(
        max_length=10,
        min_length=4,
        error_messages={'required':'用户名不能为空'},
        widget=widgets.PasswordInput(attrs={'class': 'form-contorl'})
    )
#注册form
class RegisterForm(forms.Form):
    username = fields.CharField(error_messages={'required': '用户名不能为空'})
    # user = forms.CharField()
    password = fields.CharField(
        max_length=10,
        min_length=3,
        error_messages={'required': '用户名不能为空'},
        widget = widgets.PasswordInput(attrs={'class': 'form-contorl'}))
    pwd2 = fields.CharField(
        max_length=10,
        min_length=3,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.PasswordInput(attrs={'class': 'form-contorl'})
    )
    def clean(self):
        username = self.cleaned_data.get('username')
        models.UserInfo.objects.filter(username=username)
        try:
            pwd_confirm = self.cleaned_data.get('password')
            if self.cleaned_data.get('pwd2') == self.cleaned_data.get('password'):
                del self.cleaned_data['pwd2']
                return self.cleaned_data
            else:
                from django.core.exceptions import ValidationError
                self.add_error('pwd2', ValidationError('密码输入不一致'))
                return self.cleaned_data
        except KeyError:
            return self.cleaned_data
#资产列表form
class HostForm(forms.Form):
    hostname = fields.CharField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        widget=widgets.TextInput(attrs={'class':'form-contorl'})
    )
    ipaddress = fields.GenericIPAddressField(
        required=True,
        error_messages={'required': '不能为空','invalid':'输入不合规'},
        widget=widgets.TextInput(attrs={'class': 'form-contorl'})
    )
    system = fields.CharField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        widget=widgets.TextInput(attrs={'class': 'form-contorl'})
    )
    cpu = fields.IntegerField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        widget=widgets.TextInput(attrs={'class': 'form-contorl'})
    )

    disk = fields.CharField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        widget=widgets.TextInput(attrs={'class': 'form-contorl'})
    )
    mem = fields.CharField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        widget=widgets.TextInput(attrs={'class': 'form-contorl'})
    )
    region_id = fields.ChoiceField(
        required=True,
        # initial=0,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        choices=[],
        widget=widgets.Select(attrs={'class': 'form-control'})
    )
    computer_room_id=fields.ChoiceField(
        required=True,
        # initial=0,
        error_messages={'required': '不能为空', 'invalid': '输入不合规'},
        choices=[],
        widget=widgets.Select(attrs={'class': 'form-control'})
    )

    # computer_room
    def __init__(self, *args, **kwargs):
        super(HostForm, self).__init__(*args, **kwargs)
        # print(models.ComputerRoom.objects.values_list('id', 'name'))
        self.fields['computer_room_id'].choices = models.ComputerRoom.objects.values_list('id', 'name')
        self.fields['region_id'].choices = models.Region.objects.values_list('id', 'name')
        # print('-----------',models.Region.objects.values_list('id', 'name'))