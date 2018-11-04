---
title: socket编程
date: 2018-09-12 19:16:48
comments: true
categories: Python
tags: socket
---
socket又叫套接字，就是进行数据通信两端。分为服务器套接字和客户端套接字。
套接字编程：自己写服务器或者客户端，进行数据传输。

python对socket编程的支持：提供一个socket库（内置）
```
import socket
```

### 一、服务器端（socket）

###### 1、创建套接字对象
```
def creat_server():
    """
    socket(family,type)
    a.family：确定IP协议类型
    AF_INET:ipv4（默认）
    AF_INET6:ipv6
    b.type:传输协议类型
    SOCK_STREAM:TCP协议（默认）
    SOCK_DGRAM:UDP协议
    """
    server = socket.socket()
```
###### 2、绑定IP地址和端口
```
    """
    端口：一台电脑上一个端口标记一个唯一的服务。范围0~65535,0~1014是著名端口，专门标记一个特殊服务，一般不适用。
    注意：同一端口同一时间只能绑定一个服务。
    """
    server.bind(("10.7.153.113",8080))
```
###### 3、监听（客户端请求）
```
    """
    listen(个数)
    同一时间能够连接的客户端个数。
    """
    server.listen()
```
###### 4、让服务器处于运行状态
```
    while True:
        print('监听状态！')
        """
        连接客户端（建立连接）,返回连接对象和客户端地址。
        这句代码会阻塞线程，直到有客户端来请求当前服务器为止。
        """
        connect, addr = server.accept()

        print(addr)
```
###### 5、服务器给客户端发送消息
```
        """
        send(data)
        date：python3中要求类型是bytes，python2中可以是字符串。
        字符串 >>>> 二进制 ：
        1、字符串.encode（编码方式）默认utf-8
        2、bytes(字符串，编码方式)默认None
        """
        connect.send('你好！'.encode())
        connect.send(bytes('你好','utf-8'))
```
###### 6、接收从客户端发送过来的消息
```
        """
        recv(bufsize)
        bufsize:每次能够接收的最大字节数
        返回值：接收到的数据（二进制）
        二进制 >>> 字符串：
        1、二进制.decode()
        2、str(二进制，编码方式)
        注意：recv方法也会阻塞线程。
        """
        recv_data = connect.recv(1024)
        print(recv_data.decode())
        print(str(recv_data, 'utf-8'))
```
###### 7、断开连接
```
        connect.close()
```

### 二、客户端（socket）

###### 1、创建套接字对象
```
import socket
def creat_client():
    client = socket.socket()
```
###### 2、连接服务器
```
    """
    connect(服务器地址,端口)
    """
    client.connect(('10.7.153.113', 8080))
```
###### 3、接收服务器发送的消息
```
    data = client.recv(1024)
    print(data.decode(encoding='utf-8'))
```
###### 4、给服务器发送消息
```
    client.send('我是客户端~~'.encode())
```
###### 5、断开连接
```
    client.close()
```

**实例一：通信**
```
# 服务器端
"""__author__=Deathfeeling"""

import socket

def creat_server():
    """写一个服务器"""
    # 1、创建套接字对象
    server = socket.socket()

    # 2、绑定IP地址和端口
    server.bind(("10.7.153.113",8080))

    # 3、监听（客户端请求）
    server.listen(5)
    print('监听状态！')
    connect, addr = server.accept()
    
    # 4、让服务器处于运行状态
    while True:
        mesag = input('服务器：')
        connect.send(mesag.encode())

        #6、接收从客户端发送过来的消息
        recv_data = connect.recv(1024)
        print(recv_data.decode())

    #7、断开连接
    connect.close()

creat_server()

# 客户端
"""__author__=Deathfeeling"""

import socket

def creat_client():
    # 1、创建套接字对象
    client = socket.socket()

    # 2、连接服务器
    """
    connect(服务器地址)
    """
    client.connect(('10.7.153.113', 8080))

    while True:
        # 3、接收服务器发送的消息
        data = client.recv(1024)
        print(data.decode(encoding='utf-8'))

        # 4、给服务器发送消息
        mesag = input('客户端：')
        client.send(mesag.encode())

    # 5、断开连接
    client.close()

creat_client()
```
**实例二：下载图片**
```
#图片服务器
"""__author__=Deathfeeling"""

import socket

server = socket.socket()
server.bind(('10.7.153.113', 8082))
server.listen(100)

while True:
    connect,addr = server.accept()

    with open('./beauty.png','rb') as f:
        data = f.read()
    connect.send(data)

    connect.close()

#图片客户端
"""__author__=Deathfeeling"""

import socket

client = socket.socket()
client.connect(('10.7.153.113',8082))

#创建一个空的二进制数据
all_data = bytes()
data = client.recv(1024)
while data:
    print('正在接收~~~')
    #拼接二进制数据，得到完整的图片
    all_data += data 
    data = client.recv(1024)
print('接收完毕！')
#写入在本地
with open('./new.png','wb') as f:
    f.write(all_data)
client.close()
```
### 三、网络请求
**get方法**
```
"""__author__=Deathfeeling"""

import requests

# 1、准备url
url = 'https://www.apiopen.top/satinApi?type=1&page=1'

# 2、发送请求（get）
"""
get(url,参数对应的字典)
post(url,参数对应的字典)
"""
response = requests.get(url)
# requests.get('https://www.apiopen.top/satinApi',{'type'=1,'page'=1})
# print(response)

# 3、通过相应获取服务器返回的数据
# a、获取字符串类型的数据
print(response.text)

# b、获取json的数据
print(response.json)

# c、获取二进制格式的数据
print(response.content)

# d、获取响应头（了解）
print(response.headers)

```
###### post类似，但是需要有对应的post接口。


**练习**
-----

1. 客户端和服务器聊天，可以一直聊天，直到一方发送’拜拜’。然后就可以和下一个人一直聊     
```
#服务端
"""__author__=Deathfeeling"""

import socket

def creat_server():
    """写一个服务器"""
    # 1、创建套接字对象
    server = socket.socket()

    # 2、绑定IP地址和端口
    server.bind(("10.7.153.113",8080))

    # 3、监听（客户端请求）
    server.listen(5)
    print('监听状态！')
    while True:
        connect, addr = server.accept()
        # 4、让服务器处于运行状态
        while True:
            mesag = input('服务器：')
            if mesag == '拜拜':
                print('客户端已下线！')
                connect.close()
                break
            else:
                connect.send(mesag.encode())

            # 6、接收从客户端发送过来的消息
            recv_data = connect.recv(1024)
            if recv_data.decode() == '拜拜':
                print('客户端已下线！')
                break
            else:
                print('客户端：', recv_data.decode())


creat_server()

#客户端
"""__author__=Deathfeeling"""

import socket

def creat_client():
    # 1、创建套接字对象
    client = socket.socket()

    # 2、连接服务器
    """
    connect(服务器地址)
    """
    client.connect(('10.7.153.113', 8080))
    while True:
        # 3、接收服务器发送的消息
        data = client.recv(1024)
        print('服务器：', data.decode(encoding='utf-8'))

        # 4、给服务器发送消息
        mesag = input('客户端：')
        if mesag == '拜拜':
            client.send(mesag.encode())
            print('已下线！')
            client.close()
        else:
            client.send(mesag.encode())


creat_client()
```

2. 下载网络图片（https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2808438283,4249462766&fm=26&gp=0.jpg）到本地

```
"""__author__=Deathfeeling"""
import requests

url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2808438283,4249462766&fm=26&gp=0.jpg'
pic = bytes()
response = requests.get(url)
pic += response.content
with open('./pic.jpg','ab') as f:
    f.write(pic)
```

下载的图片如下：
![pic.jpg](https://upload-images.jianshu.io/upload_images/13692175-71fc7380f0b5762d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
