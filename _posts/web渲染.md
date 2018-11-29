### 模板： 
 
	标签{% tag %}{% endtag %}
		for/if/ifequal/extends/block/comment     
	变量:{{ var }} 
	基本变量标签 {{:name}}  
	基本变量需要使用冒号 ":" 作为标识，一般是简单对象的某个属性。 
{{ block.super }}: 继承原block块里定义的内容
### 父模板：

		{%block xxxx %}   
		{% endblock %}  
### 子模板

		<!--继承父类base.html里面的内容（extends）-->
		{% extends 'base.html' %}
		{%block xxxx %}
		{% endblock %}
 <!--这是注释--> 
   
    {# 注解：这个注解在网页的源代码里面看不到（这是单行注解）#} 
      
    {% comment %}    
        这是多行注解   
        这是多行注解   
    {% endcomment %} 
    
***forloop.counter0从0开始自增序号***    
***forloop.revcounter0以0结束降序的序号***     
***forloop.counter 从1开始打印序号***  
***forloop.revcounter 以1结束打印序号***  
***forloop.first 循环第一次为True***     
***forloop.last 循环最后一次为True*** 

### if和ifequal的写法（效果一样）
	ifequal
	{% ifequal forloop.counter 1 %}
       <em style="color:red">{{ sou.s_name }}</em>
   	{% else %}
       {{ sou.s_name }}
    {% endifequal %}  
     
    if写法
	{% if forloop.counter == 1 %}
       <em style="color:red">{{ sou.s_name }}</em>
   	{% else %}
       {{ sou.s_name }}
    {% endif %}   
python | upper: 把python所有字母大写'PYTHON'     
PYthon | lower: 把PYthon所有字母小写‘python’  
date:'Y年m月d日 H:m:s' 时间格式  
### 引入css、js   
第一步： 先手动创建文件夹static   
第二步： 再手动创建css和js的文件夹 再在其文件夹创建对应的css / js 文件  
第三步： 在setting.py的最后添加     
#### 这是定义静态的路由
`STATIC_URL = '/static/'  `
#### 指定静态目录static的地址 
```
STATICFILES_DIRS = [  
    os.path.join(BASE_DIR, 'static')   
] 
```  

	加载静态文件css的两个方式
	第一种：
	<link href='/static/xxx.css' rel='stylesheet'/>
	第二种：
	 {% load static %}  
    <link href="{% static '/xxx.css'%}" rel="stylesheet">  

