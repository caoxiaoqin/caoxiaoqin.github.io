---
title: Django的上传分页和日志
comments: true
date: 2018-10-30 19:03:52
categories: Django
tags: Django
---

### 一、Django文件上传
##### 1.在模型里(models.py) 定义模型	

```
class Article(models.Model):
title = models.CharField(max_length=20)
desc = models.CharField(max_length=100)
img = models.ImageField(upload_to='article')
create_time = models.DateTimeField(auto_now_add=True)

class Meta:
db_table = 'article'

python manage.py makemigrations 创建迁移文件
python manage.py migrate 执行迁移
```

##### 2.添加文章
```
# 上传文章
url(r'^add_article/', views.add_article, name='article'), 

def add_article(request):
if request.method == 'GET':
return render(request, 'articles.html')
if request.method == 'POST':
img = request.FILES.get('img')
title = request.POST.get('title')
desc = request.POST.get('desc')
# 创建文章
Article.objects.create(img=img,
title=title,
desc=desc)

return HttpResponse('创建成功')
```
##### 3.添加跳转页面（articles.html）
```
{% extends 'base.html' %}

{% block title %}
文章首页
{% endblock %}
{# 上传图片时，图片类型设置为file，form表单添加属性enctype="multipart/form-data #}
# enctype="multipart/form-data" 必须要加 不然图片无法保存
{% block content %}
<form action="" method="post" enctype="multipart/form-data">

文章标题：<input type="text" name="title">
<br>
文章内容：<input type="text" name="desc">
<br>
上传图片：<input type="file" name="img">
<br>
<input type="submit" value="提交">
</form>
{% endblock %}
```


### 二、Django文件分页
##### 1.创建新文件夹media

```
在setting.py里面添加配置
# 配置media路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

在day/urls里导入
from day06.settings import MEDIA_URL, MEDIA_ROOT
# 将media文件夹解析为静态文件夹
# django在debug为True的情况下 就可以访问media文件夹下的内容
在day/urls里添加配置
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
```

##### 2.查看文章

```
def show_article(request, id):
if request.method == 'GET':
article = Article.objects.get(pk=id)
return render(request, 'show_article.html', {'article': article})

创建show_article.html

{% extends 'base.html'%}

{% block title%}
展示文章
{% endblock%}

{% block content %}

标题：{{ article.title}}
<br>
内容：{{ article.desc}}
<br>
图片：<img src="/media/{{ article.img}}">
{# 但是默认加载不到这个静态目录，需要在urls.py中进行配置 #}
{% endblock %}
```

##### 3.分页查看

```
注意：方法Paginator（）有两个参数，第一个是查询目标集合，第二个是每页多少条数据。

分页查看文章列表
url(r'^articles/', views.articles, name='articles'),  

def articles(request):
if request.method == 'GET':
page = request.GET.get('page', 1)
# 查询所有文章 并进行分页
articles = Article.objects.all()
# 将所有文章进行分页 每页最多三条数据
paginator = Paginator(articles, 3)
# 获取那一页的文章信息（这里拿的第一页）
arts = paginator.page(page)
return render(request, 'arts.html', {'arts': arts}


创建arts.html
{% extends 'base.html' %}

{% block title %}
分页文章
{% endblock %}

{% block content %}

{% for art in arts %}
<p>id: {{ art.id }} 标题：{{ art.title }}</p>
{% endfor %}
<br>
<p>
{% if arts.has_previous %}
<a href="{% url 'user:articles' %}?page={{ arts.previous_page_number}}">上一页</a>
{% endif %}

{% for i in arts.paginator.page_range %}
<a href="{% url 'user:articles' %}?page={{ i }}">{{ i }}</a>
{% endfor %}

{% if arts.has_next %}
<a href="{% url 'user:articles' %}?page={{ arts.next_page_number}}">下一页</a>
{% endif %}

</p>

{% endblock %}	
说明：

art.has_previous - 有上一页返回True
art.has_next - 有下一页返回True
art.previous_page_number - 返回上一页的页码
art.next_page_number - 返回下一页的页码
art.paginator.page_range - 返回页码的range函数（比如一共5页，返回range（1,6））
```
### 三、Django配置日志
##### 1.创建一个logs文件夹 用于存放日志  

settings.py文件中配置LOGGING日志信息：
`MIDDLEWARE = ['utils.middleware.LoggingMiddleware',]`
```	
# 配置日志

LOGGING = {
# 必须是1
'version': 1,
# True表示禁用日志
'disable_existing_loggers': False,
# 指定写入到日志文件中的日志格式
'formatters': {
'default': {
'format': '%(name)s %(asctime)s %(message)s'
}
},
'handlers': {
'console': {
'level': 'INFO',
'filename': '%s/log.txt' % os.path.join(BASE_DIR, 'logs'),
'formatter': 'default',
# 当日志文件大于5M 就自动备份
'class': 'logging.handlers.RotatingFileHandler',
# 设置最大字节
'maxBytes': 5 * 1024 * 1024,
}
},
'loggers': {
'': {
'handlers': ['console'],
'level': 'INFO'
}
}
}
```
##### 2.创建一个叫utils的文件夹 里面存放中间件  
定义日志处理的中间件，进行日志的打印处理  
定义日志中间件logMiddleware.py文件，定义LoggingMiddleware类，该类继承MiddlewareMixin，并重构`process_request`和`proccess_response`方法：
```
import time
import logging
from django.utils.deprecation import MiddlewareMixin


class LoggingMiddleware(MiddlewareMixin):

def process_request(self, request):
request.init_time = time.time()
request.init_body = request.body
# 记录当前请求访问服务器的时间 请求参数 请求内容
return None

def process_response(self, request, response):
try:
# 记录返回响应的时间坏人访问服务器的时间差 记录返回状态码、
times = time.time() - request.init_time
# 响应状态码
code = response.status_code
# 响应内容
res_body = response.content
# 请求内容
req_body = request.init_body

# 日志信息
msg = '%s %s %s %s' % (times, code, res_body, req_body)
# 写入日志
logging.info(msg)
except Exception as e:
logging.critical('log error, Exception: %s' % e)
return response
```
