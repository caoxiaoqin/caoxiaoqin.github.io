flask: [flask.pocoo.org/extensions]

 注意：在有装饰器的情况下 反向解析不成功 必须强行指定地址

### 1. session 
Session和Cookie的结合使用，一般有两种存储方式:

**第一种**: session数据存储在客户端: Flask采用'secure cookie'方式保存session，
即session数据是使用base64编码后保存在客户端的cookie中。  
也就是说无须依赖第三方数据库保存session数据。

 代码：

```
@blue.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'caocao' and password == '123456':
            # 模拟校验用户名和密码成功 则向session中存登录成功后的用户id
            session['user_id'] = 1
            # 有装饰器的时候 反向解析不了 必须强行指定下地址
            # return redirect(url_for('user.index'))
            return redirect('/app/index/')
        else:
            return redirect(url_for('login.html'))

# 装饰器必须写在路由的面  不然不生效
@blue.route('/index/')
@login_re
def index():
    user_id = session['user_id']
    return '我是首页, 用户id为%s' % user_id
```

装饰器：

```
def login_re(func):
    def index_my():
        try:
            user_id = session.get('user_id')
        except Exception as e:
            return redirect(url_for('user.login'))
        return func()
    return index_my
```



**第二种**: session数据存储在服务端，分为以下三步骤:

步骤1: 当客户端发送请求到服务端的时候，服务端会校验请求中cookie参数中的sessionid值，如果cookie中不存在sessionid则认为客户端访问服务端时，是发起了一个新的会话。

步骤2: 如果是新的会话，则服务端会传递给客户端一个cookie，并在cookie中存储一个新的sessionid值，并将相关数据保存在session中。

步骤3: 客户端下次再发送请求的时候，请求上下文对象会携带cookie，通过校验cookie中的sessionid值，即可判断是否是同一会话。

步骤4: 如果校验会话是同一会话，则可以从session中获取到之前保存的数据。

访问者的标识问题服务器需要识别来自同一访问者的请求。这主要是通过浏览器的cookie实现的。 访问者在第一次访问服务器时，服务器在其cookie中设置一个唯一的ID号——会话ID(session)。 这样，访问者后续对服务器的访问头中将自动包含该信息，服务器通过这个ID号，即可区 隔不同的访问者

 `pip install Flask-Session`

```python
# 配置session存储数据库
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
# 初始化Flask对象app
# 第一种写法
Session(app)
# 第二种写法
sess = Session()
sess.init_app(app)
```



### 2. 使用redis

1) 先下载：redis  把redis放在/uer/local/redis 进入到目录redis

2) 编译测试： sudo make test

3编译安装： sudo make install

4)启动redis服务:  redis-server

5)开启redis客户端： redis-cli



 ### 3. flask模板 继承（html）

`{% extends 'xxx.html' %}`

```
引入static中的css
第一种方式
<link rel="stylesheet" href="/static/css/style.css">
第二种方式
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

#####  继承block里已填充的内容

```
Django中继承： {{ block.super() }} 
 flask中继承：  {{ super() }} 
```

##### 标签： {% 标签 %}

```
{% if %} {% for %} {% block %} ...
```

##### 变量 ：{{ 变量 }}

```
loop.first 是否是第一次循环 （返回true和false）

loop.last 是否是最后一次循环 （返回true和false）

loop.index 从1开始排序

loop.revindex 倒序 最后一个是1

loop.index0 从0开始排序

loop.revindex0 倒序 最后一个是0

```

##### 过滤器（常用）

```
upper
lower
safe
length
```

### 4. 在HTML里声明函数

***虽然可以写在HTMl的文件里 但建议单独创建一个HTML文件放代码***

在tamplates--->function.html 用于放代码

```
<!--声明函数-->
{% macro hello() %}
    <p>你好，曹曹</p>
{% endmacro %}


{% macro say(name) %}
    <p>你好，{{ name }}</p>
{% endmacro %}
```

##### 在其他页面导入并调用function里的函数

```
    {% from 'function.html' import hello %}
    {% from 'function.html' import say %}

    <!--调用函数-->
    {{ say('李白') }}
    {{ hello() }}
```

### 5. 模型层

##### 使用flask-sqlalchemy库

`pip install flask-sqlalchemy`

##### 创建模型

```
from flask_sqlalchemy import SQLAlchemy
# 拿到SQLAlchemy对象
db = SQLAlchemy()


# 第一步声明模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=True)

	# 表名：__tablename__ = '表名'
    __tablename__ = 'day02_user'
    
    
    
约束： unique, nullable, default，String
```

##### 创建数据库的连接

	
	数据库连接格式: mysql+pymysql://用户名:密码@host:port/数据库名
	# 数据库的配置
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
	#在数据库中创建一个数据库(flask6) 用于存储数据
	
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	
	# 初始化APP和db
	db.init_app(app)
##### 迁移模型

```
@blue.route('/create_db/')
def create_db():
    # 第一次迁移模型
    db.create_all()
    return '创建成功'
```

##### 删除模型

```
@blue.route('/drop_db/')
def drop_db():
    # 删除模型
    db.drop_all()
    return '删除模型成功'
```

