### MVC(Mode View Controller)
Model: 即数据存取层。用于封装于应用程序的业务逻辑相关的数据，以及对数据的处理。说白了就是模型对象负责在数据库中存取数据

View: 即表现层。负责数据的显示和呈现。渲染的html页面给用户，或者返回数据给用户。

Controller: 即业务逻辑层。负责从用户端收集用户的输入，进行业务逻辑处理，包括向模型中发送数据，进行CRUD操作。

### Django的模式简介 - MVT模式
严格来说，Django的模式应该是MVT模式，本质上和MVC没什么区别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同。

Model： 负责业务与数据库(ORM)的对象

View： 负责业务逻辑并适当调用Model和Template

Template: 负责把页面渲染展示给用户

注意： Django中还有一个url分发器，也叫作路由。主要用于将url请求发送给不同的View处理，View在进行相关的业务逻辑处理。
 
 
### 安装虚拟环境
##### 1、安装VIRTUALENV  
`pip install virtualenv`   

###  创建虚拟环境
#####  2、进入你需要创建虚拟环境的目录
```virtualenv --no-site-packages djenv     
参数说明： --no-site-packages 是获取一个纯净的python虚拟环境  
         -p + <版本路径>指定python版本   
         djenv 是文件名 可以随意（但需见名知意） 
```
###   3、进入和退出env   
```
进入: cd djenv  再使用activate命令
注意：mac 需要 source activate命令才能进入  
退出： deactivate
```
### 二、安装Django  
安装django
`pip install django==1.11`
 查看：
pip list      
pip freeze   

    
安装数据库的驱动 
  
`pip install pymysql`

### 三、创建Django项目
`django-admin startproject<文件名>`
例如：django-admin startproject day01   

用pycharm打开项目，并使用创建好的虚拟环境

Django目录结构：

  .   
  ├── day01   
  │   ├── __init__.py  
  │   ├── settings.py  
  │   ├── urls.py   
  │   └── wsgi.py    
  └── manage.py 
终端启动:

`python manage.py runserver IP:PORT`
 django启动项目:python manage.py runserver 8080
 8080 是指定端口  

 
修改manage.py 中：

`LANGUAGE_CODE = 'zh-hans' `- 字体

`ALLOWED_HOSTS = ['*']`

启动添加0.0.0.0表示允许所有ip访问


### 四、连接数据库
修改manager.py文件

seettings.py数据库配置
DATABASES = {  
   'default': {  
      'ENGINE': 'django.db.backends.mysql',  
      'NAME': 'dj6',  
      'USER': 'root',    
      'PASSWORD': '123456',  
      'HOST': '127.0.0.1',  
      'PORT': 3306  
  }  
} 

### 安装数据库的驱动
pip install pymysql

```  
修改__init__.py文件
在__init__ 设置里面 

因为python3不能直接连接数据库

import pymysql

pymysql.install_as_MySQLdb()
```
### 生成一些的对应表（映射模型的数据库）

`python manage.py migrate`

### 创建管理用户
```
python manage.py  createsuperuser
createsuperuser例如：admin + 密码
```


访问管理后台（admin）网络查看  
` http://127.0.0.1:8000/admin/login/?next=/admin/`



 
 




