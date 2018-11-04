---
title: Linux02
comments: true
date: 2018-10-12 00:07:35
categories: Linux
tags: linux
---
计算机网络分层架构模型
Internet --- TCP/IP协议族
TCP --- Transfer Control Protocol - 传输控制协议
UDP --- User Datagram Protocol - 用户数据报协议
IP --- Internet Protocol - 网际协议

TCP/IP模型
应用层（定义应用级的协议） - HTTP、SMTP、POP3、FTP、SSH、ICQ/QQ……
传输层（端到端传输数据） - TCP/UDP……
网络层/网际层（寻址和路由） - IP/ICMP……
物理链路层（数据分帧+校验） - 冗余校验码……

启动、关闭、重启服务和查看服务状态
systemctl start <name>
systemctl stop <name>
systemctl restart <name>
systemctl status <name>
systemctl enable <name> 开启开机自启动
systemctl disable <name> 关闭开机自启动
低版本使用service命令：
service <name> start
......

常用的防火墙服务有firewall和iptables
systemctl start firewalld 开启防火墙
firewall-cmd --add-service=httpd  开启服务
firewall-cmd --permanent --add-port=443/tcp 永久开启 开启端口
firewall-cmd --query-port=443/tcp 查看端口是否开启
firewall-cmd --query-service=httpd 查看服务是否开启
再重启防火墙生效

top - 按CPU占用率从高到低排列进程

如果需要把运行中的进程终止掉 - Ctrl + C
如果需要把运行中的进程放在后台 - Ctrl + Z
中止输入 - Ctrl + D

执行命令时在命令后面加上&符号，就可以把命令置于后台运行
jobs - 查看后台进程
bg %编号 - 把后台暂停的进程运行
fg %编号 - 把后台进程在前台运行

----
##### 分享一个“自慰神器”
可以在启动配置文件里面添加shell语句
`~/.bash_profile`  这里修改只有root才能看到    
`/etc/profile` 这里修改，登录的用户都能看到
下面是添加的代码：
```
 username=`whoami`
 if [ "$username" = "root" ]
 then
     echo "热烈欢迎『洁帅大大』登录阿里云服务器，阿里云全体员工在此全体起立，鼓掌！！！"
     echo ""
     echo "您是超级管理员，掌控雷电，为非作歹，无所不能~~"
     echo ""
 else
     read -p "请爸爸输入名字:" realname
     echo "热烈欢迎『$realname』登录阿里云服务器，阿里云全体员工在此起立，鼓掌！！！"
     echo "记住，你只是一个普通用户！"
     echo ""
 fi

```
效果：
超级用户登录：
```
Last login: Fri Oct 12 16:49:49 2018 from 125.70.30.209

Welcome to Alibaba Cloud Elastic Compute Service !

热烈欢迎『洁帅大大』登录阿里云服务器，阿里云全体员工在此全体起立，鼓掌！！！

您是超级管理员，掌控雷电，为非作歹，无所不能~~

[root@aliyun ~]# 
```
普通用户登录：
```
请爸爸输入名字:星辰
热烈欢迎『星辰』登录阿里云服务器，阿里云全体员工在此起立，鼓掌！！！
记住，你只是一个普通用户！

[deathfeeling@aliyun ~]$ 
```
