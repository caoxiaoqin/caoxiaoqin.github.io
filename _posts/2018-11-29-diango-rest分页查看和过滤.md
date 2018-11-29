### diango-rest分页查看和过滤

settings.py设置配置文件

```
# rest_framework配置
REST_FRAMEWORK = {
    # 设置分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    # 过滤配置
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    )
}
```

在视图文件里：

```
from django.shortcuts import render
from rest_framework import mixins, viewsets

from apps.filters import ArticleFilter
from apps.models import Article
from apps.serializers import ArticleSerializer


class ArticleView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    # 查询数据
    queryset = Article.objects.filter(is_delete=0)
    # 序列化
    serializer_class = ArticleSerializer
    # 过滤
    filter_class = ArticleFilter
```

在apps/filters.py

```
import django_filters

from rest_framework import filters

from apps.models import Article


class ArticleFilter(filters.FilterSet):
    # 127.0.0.1:8080/apps/article/?t=查询内容&desc=内容
    t = django_filters.CharFilter('title', lookup_expr='icontains')
    desc = django_filters.CharFilter('desc', lookup_expr='icontains')
    create_time_min = django_filters.DateTimeFilter('create', lookup_expr='gt')
    create_time_max = django_filters.DateTimeFilter('create', lookup_expr='lt')

    class Meta:
        model = Article
        fields = []
```

通过postman# 127.0.0.1:8080/apps/article/?t=查询内容&desc=内容&create_time_min=时间







1 django 自带的auth模块 实现登录注册

​	登录 auth.login()

​		request.user()赋值

​	退出：auth.logout()

​		request.user匿名用户

​	验证： login_required()

​	权限验证：permission_requeired()

2 自己实现 通过令牌token 

​	登录： 设置cookie  cookie里保存token值

​	退出：清空cookie 删除服务端里的token和用户的关联关系

登录验证：

​	装饰器

​	中间件

3 cookie+ session: （会话的上下文，会话保持）

​	cookie:存放在客户端的

​	session:存放在服务器的

​	登录： request.session[key] = value

​	退出： 删除session中的key

​	登录验证： 获取session中的key值 如果获取到就表示登录， 如果没有获取到就表示没有登录