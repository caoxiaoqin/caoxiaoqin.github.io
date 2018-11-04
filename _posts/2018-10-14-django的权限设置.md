---
title: django的权限设置
comments: true
date: 2018-10-31 19:26:21
categories: Django
tags: Django
---
### Django的权限项
Django用permission对象存储权限项，   
每个model默认都有三个permission，即add model, change model和delete model。   
例如: 
定义一个名为学生Student模型，当迁移表后，会在auth_permission中自动创建相应的三个  `permission：add_student, change_student和delete_student`   
Django还允许自定义permission。

#### 自定义权限     
在自定义模型的Meta元中添加permissions参数  

在models.py中自定义权限  

```
from django.contrib.auth.models import AbstractUser, User
from django.db import models

a
class MyUser(AbstractUser):
# 拓展django自带的auth_user表 可以自定义新增的字段
class Meta:
# django默认给每个模型初始化三个权限
# 默认是change delete add 权限
permissions = (
('add_my_user', '新增用户权限'),
('change_my_user_username', '修改用户名权限'),
('change_my_user_password', '修改用户密码权限'),
('all_my_user', '查看用户权限'),
)    
```
并在settings.py文件中添加如下设置：

```
# 告诉django User模型修改为自定义的MyUser模型
AUTH_USER_MODEL = 'user.MyUser'
```
注意：在数据库的auth_permission表中，会新增权限，包括自带的对Users管理的权限，和自定义的四个权限。

添加/删除权限  
采用直接分配权限的方法，给用户添加额外的权限既用户表Users和权限Permission模型以及中间表user_permission之间的关联关系。  
用户Users模型和权限Permission之间是ManyToManyField()多对多关联关系，关联字段为user_permission。
#### 创建用户和添加权限
```
def add_user_permission(request):
if request.method == 'GET':
# 创建用户
user = MyUser.objects.create_user(username='caocao', password='12345',)
# 指定刚创建的用户 并分配给她权限(新增权限，查看用户权限)
permissions = Permission.objects.filter(codename__in=['add_my_user',
'all_my_user']).all()
for permission in permissions:
# 添加权限
user.user_permissions.add(permission)
# 删除刚创建的用户的新增用户的权限
# user.user_permissions.remove(权限对象)
return HttpResponse('创建用户权限成功')
```

语法：

```
其中xxx的关联字段可以进行查看
添加权限：user对象.xxx.add(permission对象1, permission对象2)
删除权限：user对象.xxx.remove(permission对象1, permission对象2)
清空权限：user对象.xxx.clear()
```

##### 用户名caocao 有查看用户列表的权限 才能访问视图函数
```

@permission_register
def index(request):
# 用户名coco 有查看用户列表的权限 才能访问视图函数，
if request.method == 'GET':
return render(request, 'index.html')

```
#####  function.py中定义装饰器
```
# 定义装饰器：
# 1外层函数内嵌内层函数
# 2外层函数返回内存函数
# 3内层函数调用外层函数的参数
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect, HttpResponse


from user.models import MyUser


def permission_register(func):
def check_in(request):
# 获取用户
user = MyUser.objects.filter(username='caocao').first()
# 验证权限
user_permiss = user.user_permissions.filter(codename='all_my_user').first()
if user_permiss:
return func(request)
else:
return HttpResponse('没有权限访问')
return check_in
```
#### Django显示权限项
##### 自定义查询权限
视图函数：

```
def show_user_permission(request):
# 查看对应用户的权限
if request.method == 'GET':
# 获取对应用户 交给前端显示
user = MyUser.objects.get(username='caocao')
return render(request, 'permissions.html', {'user': user})
```
permissions.html文件

```

{% block content %}
{# 在前端取数据，用all代替all(), 用0代替第一个元素 #}
{# 查询用户的权限 #}
{% for permission in user.groups.all.0.permissions.all %}
{{ permission.name}}
{% endfor %}
<br>
{# 通过用户直接查找权限 #}
{%  for per in user.user_permissions.all %}
{{ per.name }}
{% endfor %}
{% endblock  %}
```
### Django自带查询权限方法
```
拿到当前登录系统用户
user = request.user

# 获取当前用户对于的组权限
user.get_group_permissions()

# 获取当前用户所有的权限
user.get_all_permissions()

# 判断是否有某个权限
user.has_perm('perm)  # perm ==> '应用名.权限'
user.has_perms('perm_list')   # perm_list ==> '应用名.权限集合'
```
### Django自带权限验证装饰器
```
# django自带的权限验证,如果有对应权限，才能访问，否则返回到登录页面，在settings.py文件中定义返回页面
@permission_required('对应权限')  # 对应权限 ==> 应用名.权限(permissions.add_my_user)
```
### settings.py文件中自定权限验证不通过的返回页面
```
登录验证/权限验证不通过，则跳转地址
LOGIN_URL = '/permissions/login/'
```
