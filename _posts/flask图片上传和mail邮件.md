### flask图片上传

##### 1.图片需存放的路径

```
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.path.abspath(__file__) 拿到的是当前操作文件的绝对路径
	'/Users/apple/Desktop/python-caocaocao/6flask/day05/app/views.py'
	
	
# os.path.dirname(os.path.abspath(__file__)) 拿到的是当前操作文件的绝对路径的上一级的绝对路径
   '/Users/apple/Desktop/python-caocaocao/6flask/day05/app'


# 拿到的是当前操作文件的绝对路径的上两级的绝对路径os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   '/Users/apple/Desktop/python-caocaocao/6flask/day05'

```

```
MEDIA_ROOT = os.apth.join(os.path.join(BASE_DIR,'static'), 'media')

os.path.join(BASE_DIR, 'static')拿到的路径是：
'/Users/apple/Desktop/python-caocaocao/6flask/day05/static'

MEDIA_ROOT = '/Users/apple/Desktop/python-caocaocao/6flask/day05/static/media'
```

##### 2.获取图片

```
upload_img = request.files.get('img')
# 获取文件或图片： files
```

##### 3.保存图片到本地（指定的路径）

```
path = os.path.join(MEDIA_ROOT, upload_img.filename)
upload_img.save(path)
```

##### 4.保存图片到数据库

```
models.py： 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 创建存放图片的数据库表
class UploadImg(db.Model):
    id = db.Column(db.Integer, 
                   primary_key=True,autoincrement=True)
    img = db.Column(db.String(100), nullable=False)
```

```
up_img = UploadImg()
upload_path = upload_img.filename
up_img.img = upload_path
db.session.add(up_img)
db.session.commit()
return render_template('img.html', img=up_img)
```

### Flask-mail

`pip install flask-mail`

##### 1.邮箱配置

```
class Config():
    # 邮箱配置
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'cao_xiao_qin@126.com'
    MAIL_PASSWORD = 'cao13518479723'
```

##### 2.发送消息

```
@blue.route('/mail_hello/')
def mail_hello():
	msg = Message('title',
				  sender=Config.MAIL_USERNAME,
				  recipients=['915710285@qq.com'])
	msg.body = '比你优秀的人 还比你努力'
	mail.send(msg)
	return 'success'

# Config.MAIL_USERNAME = 'cao_xiao_qin@126.com'
# title： 标题
# sender: 发送者
# recipients ：接受者
# body： 发送的内容
# send(): 发送
```

