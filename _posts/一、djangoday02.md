## 一、创建项目day02
1.进入虚拟环境：`source activate `  
2.创建代码的项目：`pyhton manage.py startproject day02`   
3.更改设置__init__.py设置    
``` 
    import pymysql  
	 pymysql.install_as_MySQLdb()   
```    
4.更改setting.py设置

     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj8',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'PASSWORD': '123456'
    }
	}   
	LANGUAGE_CODE = 'zh-hans'

```

 二、创建应用    
` python manage.py startapp <文件名>`
#### 我先创建了一个名为app的应用：   
`python manage.py startapp app`    
然后在app里面的models.py里定义东西  

   
from django.db import models  
class Student(models.Model):  
     定义s_name字段最长不超过6个字符    
     unique=True 唯一      
    s_name = models.CharField(max_length=6, unique=True)
          
     定义s_age字段    
    s_age = models.IntegerField(default=18)
      
     定义s_gender字段  
    s_gender = models.BooleanField(default=1) 
      
      定义create_time字段 创建时间   
    create_time = models.DateTimeField(auto_now_add=True)
      
    #### 定义operate_time字段 修改时间 auto_now为每次修改 保存每次修改的时间   
    operate_time = models.DateTimeField(auto_now=True)    
	
	class Meta:  
        #### 定义模型迁移导数据库的表名  
        #### 表名为student  
        db_table = 'student'  
```



#### 在day02里settings。py里修改：

```  
INSTALLED_APPS = [     
    'django.contrib.admin',   
    'django.contrib.auth',   
    'django.contrib.contenttypes',   
    'django.contrib.sessions',    
    'django.contrib.messages',   
    'django.contrib.staticfiles',   
    'app', ---为添加的字段  
]    
```



#### 在urls.py里导入views  
`from app import views`
```
urlpatterns = [
    # 127.0.0.1/create_stu
    url(r'^create_stu/', views.create_stu),
]
```
(生成迁移文件)   
`命令：python  manage.py makemigrations `  
 (执行迁移文件)    
`命令：python  manage.py migrate  `  

在views里面导入student  
   `from app.models import Student`    
#### 在views里创建你需要的     
    
    def create_stu(request):    
    ####  创建学生  
    stu = Student()
    stu.s_name = 'caocao'
    stu.s_gender = '0'
    stu.s_age = 18
    stu.save()
    
    #### 第二种创建学生
    Student.objects.create(s_name='tos')
    Student.objects.create(s_name='xiaoh')
    Student.objects.create(s_name='xia')
    Student.objects.create(s_name='cp3')
    Student.objects.create(s_name='kobe')
    return HttpResponse('创建成功')
    ```
在网络查看  
`127.0.0.1：8080/路由地址`   
def sel_stu(request):  
     实现查询所有对象信息 all()  
    
    stus = Student.objects.all()
    
     filter()过滤
    stus = Student.objects.filter(s_name='Tom')
    
     first()获取第一个  
     last()获取最后一个  
    stus = Student.objects.filter(s_name='caocao').first
    
     get只能返回一个值，返回多个值或不存在的值就会报错
    stus = Student.objects.get(s_name='caocao')
    
     同时查询多个条件的语句
    stus = Student.objects.filter(s_age=18, s_gender=0)   
    
     模糊查询like '%xx%' '_xx%'
     包含c的
    stus = Student.objects.filter(s_name__contains='c')  
    
     以x开头
    stus = Student.objects.filter(s_name__startswith='x')
    
    
     大于gt/gte大于等于  小于lt/lte小于等于
    stus = Student.objects.filter(s_age__gt=16)
    
     排序 order_by()
     升序
    stus = Student.objects.order_by('id')
     降序
    stus = Student.objects.order_by('-id')  
    
     查询不满足条件数据 exclude()
    stus = Student.objects.exclude(s_age=19)
    
    
     统计个数count()
    stus_count = stus.count()
    print(stus_count)
    
    
     统计个数len()
     print(len(stus))
     stus.values()查看所有
    
     id=pk
     查询id=2的数据
    stus = Student.objects.filter(id=9)
    print(stus.values())

    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    return HttpResponse('查询成功')


####  ORM对象关系映射   
`-- object-relational-mapping  ` 

all(): 查询所有语句
frist(): 拿到第一数据   
last():拿到最后一个数据   
all()            返回所有数据   

filter()	 返回符合条件的数据   

exclude()        过滤掉符合条件的数据    

order_by()       排序   

values()         一条数据就是一个字典，返回一个列表  
count()：返回当前查询集中的对象个数   

exists()：判断查询集中是否有数据，如果有数据返回True，没有返回False   
get()：只返回一个值 如果返回多个值或没有就会报错   
模型名.objects.all()[0:5] 小标不能为负数   # 相当于limit限制查询集，   

agregate()函数返回聚合函数的值   
  
Avg：平均值   

Count：数量  
    
Max：最大   

Min：最小   

Sum：求和  

例如: Student.objects.aggregate(Max('age'))    


