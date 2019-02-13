## 相关版本
- Django==>1.11
- python==>3.5.2
- pip==>8.1.1
- requests==>2.21.0
## 新系统安装启动教程
```python
###########安装python3.5.2#############
# wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
# tar -zxf Python-3.5.2.tgz 
# cd Python-3.5.2
# ./configure --prefix=/usr/local/python3.5
# make -j8 && make install -j8
# ln -s /usr/local/python3.5/bin/python3.5 /usr/bin/python3.5
###########安装pip################
# wget https://files.pythonhosted.org/packages/41/27/9a8d24e1b55bd8c85e4d022da2922cb206f183e2d18fee4e320c9547e751/pip-8.1.1.tar.gz
# tar -zxf pip-8.1.1.tar.gz -C /usr/local/
# cd /usr/local/pip-8.1.1/
# python3.5 setup.py install
# pip -V
########安装模块###########
# pip install django==1.11
# pip install requests==2.21.0
########启动#########
# python3.5 manage.py runserver 0.0.0.0:8080
```
## 启动及登录
- **注意:启动之前，需要修改‘CMDB\utils\send_salt_api.py’文件**
  + salt_api： 你自己salt-api的服务器ip 
  + username： salt-api用户名 
  + password： salt-api密码 
- linux启动
  + python manage.py runserver 0.0.0.0:8080
- windows启动
  + python manage.py runserver 127.0.0.1:8080
- 登录用户名密码
  + test 123456789
  + 后台：admin admin123456
- 访问login页面 127.0.0.1:8080/host/login 
## host目录
- modles.py
  + 建立数据库表结构
    + 使用了一对多ForeignKey
    + 权限表使用了多对多ManyToManyField
- urls.py
  + 定义host相关url
    + 增
    + 删
    + 改
    + 查
- views.py    
  + 定义了增删改查的具体功能实现
    + 在login与register中使用django自带的make_password, check_password功能，进行对密码加密
      + 使用了cookies进行验证
    + 在hostpage中使用form表单对数据进行处理
    + 在logout中，进行删除cookies操作
- 其他暂未使用
## Middleware目录
- MiddleWare.py
  + 在Order中设定白名单，对用户进行cookies验证
## salt目录
- urls.py
  + 定义salt相关url
- parsing.py
  + ResApi中定义了两个函数
    + info() 将salt-api的数据拿过来进行处理
    + parsing()将处理后的数据进行一一对应，反馈给用户的数据可以直接使用，目前只有4个数据（主机名，ip，操作系统，内存）
- viesw.py
  + 在apilist中定义get，post方法
    + 将parsing.py中反馈过来的数据进行展示给用户
- 其他暂未使用
## static目录
- 该目录下存放bootstrap文件，用于前端渲染
- 存放了bootstrap模板  可以测试使用
## templates目录
- add.html 
  + 用于hostpage中‘新增数据’的功能
- update.html
  + 用于hostpage中‘更新数据’的功能
- apipage.html
  + 提供与minion端进行交互的功能
- base.html
  + 父模版，用于给其他页面继承
- hostpage.html
  + 展示所有资产信息，有增删改的功能，还未实现查，其中刷新调用了send_salt_api.py的功能
- login.html
  + 登录界面
- register.html
  + 注册界面
## utils目录
- form_class.py
  + UserForm 用户表单
  + RegisterForm 注册表单
  + HostForm 资产信息表单
- send_salt_api.py
  + 用于与远程客户端进行通讯，并返回saltapi的数据
- init_menu.py
  + 用于初始化用户权限信息
## user目录
- urls.py 存放url
- views.py 定义对应功能
  
## 存在的问题BUG
- 很多功能都有缺陷 仅供参考 