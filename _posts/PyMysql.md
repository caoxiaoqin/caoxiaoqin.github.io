---
title: PyMysql
comments: true
date: 2018-10-17 14:22:45
categories: PyMysql
tags: pymysql
---

#### 一、pip安装模块

```
pip install -i https://pypi.doubanio.com/simple pymysql

# 如果希望pip安装时自动从国内特定网址下载，可以设置全局设置，在用户主目录下新建pip文件夹，再新建pip.ini文件，写入index-url=https://pypi.doubanio.com/simple即可

以后则可以直接pip install pymysql 会自动从指定网址下载。
```
#### 二、操作数据库

```
import pymysql

def main():
    # 1、创建数据库连接
    conn = pymysql.connect(host='localhost', port=3306, db='hrs', user='root', password='123456', charset='utf8')
    # 可以添加autocommit=True执行sql语句会自动提交
    try:
        # 2、创建游标对象
        with conn.cursor() as cursor:
            # 3、向数据库服务器发出sql语句
            result = cursor.execute('delete from tbdept where dno=40')
            if result == 1:
                print('删除成功！')
            conn.commit() # 4、提交操作（默认开启了事务）
    finally:
        # 确保数据库关闭
        conn.close()

if __name__ == '__main__':
    main()
```

#### 三、数据库查询操作

Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

- **fetchone():** 该方法获取下一个查询结果集。结果集是一个对象
- **fetchall(): **接收全部的返回结果行.
- **rowcount:** 这是一个只读属性，并返回执行execute()方法后影响的行数。

