---
title: django_pages01
comments: true
date: 2018-10-25 20:09:04
categories: django
tags: Django
---
alt+enter：快捷键

autofield charfield integerfield booleanfield datetimefield    
filter()查询满足条件的   
first()   
last()最后   
edxclude() 排除满足条件的   
all()查询所有  
order_by()排序   
values()     
__contains() 包含   
__startwith() 以什么开头  
__endwith() 以什么结尾   
__gt() 大于  
__gte() 大于等于  

## 一、删除
在urls.py添加   
url(r'del_stu/', views.del_stu),   
在views里添加一个函数    

def del_stu(request):   
Student.objects.filter(s_name='caocao').delete()  
return HttpResponse('删除成功')  


## 二、 更新
在urls.py添加   
***`url(r'update_stu/', views.update_stu),`***  
在views里添加一个函数    

def update_stu(request):  
Student.objects.filter(s_name='被更新的据').update(s_name='更新数据')    
return HttpResponse('更新成功')  

##### from django.db.models import Q, F 需要导入
##### 或者条件
***`stus = Student.objects.filter(Q(s_age=18) | Q(s_gender=1))`***
##### 且条件
***`stus = Student.objects.filter(Q(s_age=18) & Q(s_gender=1))`***
##### 非条件
***`stus = Student.objects.filter(~Q(s_age=18))`***
##### chinese成绩大于math成绩
***`stus = Student.objects.filter(chinese__gt=F('math'))`***   



## 创建返回页面
#### 1.创建一级文件夹名为**templates**
#### 2.settings.py里修改 TEMPLATES   
`'DIRS': [os.path.join(BASE_DIR, 'templates')],`
#### 3.在templates里创建一个html的文件
```
{% for stu in students %}
<p> 姓名: {{ stu.s_name }}, 年龄: {{ stu.s_age }}</p>
{% endfor %}
这里返回的是所有的学生姓名和年龄
```



## 关联关系  
1)一对一： oneToOneField 

```
class A:   
id = xxxx  
b = oneToOneField(B)  
class B:   
id = xxxx 
已知a对象 查找b对象： a.b  
已知b对象 查找a对象： b.a
``` 
2) 一对多 ： ForeignKey

```
# 假设A为多
class A:
id = xxxx
b = ForeignKey(B)
class B: 
id = xxxx 
已知a对象 查找b对象： a.b  
已知b对象 查找a对象： b.a_set

``` 

3)多对多： manyToManyField

```
class A:
id = xxxx
b = manyToManyField(B)
class B: 
id = xxxx 

已知a对象 查找b对象： a.b  
已知b对象 查找a对象： b.a_set

b.a_set.add（内容）-->写入关键表中
b.a_set.remove（内容）---->删除关键表里的指定内容


```

## 执行成功之后就跳转到（all_stu）路径里
return HttpResponseRedirect('/all_stu/')




