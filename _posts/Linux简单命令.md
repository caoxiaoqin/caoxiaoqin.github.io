---
title: Linux简单命令
comments: true
date: 2018-10-8 00:04:53
categories: Linux
tags: linux
---
[Linux命令大全](http://www.runoob.com/linux/linux-command-manual.html)
查看手册 -- **man + 命令** or  **命令 --help**
------
- clear 清屏
- w / last /who /  who am i  获取登录信息
- ps 查看进程
- kill （kill -9 ） 杀死进程（强行杀死进程）
- adduser 创建用户
- userdel 删除用户
- su 切换用户
- cd 切换
- pwd 查看当前路径
- ls 查看文件和文件夹
- history  查看历史命令（！编号：执行对应编号的命令）
- mkdir 创建文件夹
- rmdir 删除空文件夹
- cp 复制文件和目录
- rm 删除
- touch 创建文件修改文件最后访问时间
- mv 移动或者改名
- echo 回声
- head/tail 查看文件开头/结尾
- less/more 分屏查看文件
- wc 统计行数，单词，字节
- sort <file>排序
- uniq <file> 去重（相邻行）
- alias 别名（alias rmd="rm -rf"）
- unalias 取消别名
- diff 比较
- vim -d 比较（详细）
- ln 
硬链接 - 文件的引用，只要引用数不为零，文件就一直存在，相当于分身（ln）。
软链接 - 相当于文件的快捷方式（ln - s）。
-----
- ">" 输出重定向
- ">>" 追加输出重定向
- "2>" 错误输出重定向
- "<" 输入重定向
- "|" 管道（进程间通信）- 把前一个进程的输出作为后一个进程的输入

>: 会重写文件，如果文件里面有内容会覆盖。  

>>这个是将输出内容追加到目标文件中。如果文件不存在，就创建文件。  

>>：追加文件，也就是如果文件里面有内容会把新内容追加到文件尾。  
>   是定向输出到文件，如果文件不存在，就创建文件；如果文件存在，就将其清空。一般我们备份清理日志文件的时候，就是这种方法：先备份日志，再用`>`，将日志文件清空（文件大小变成0字节）。  
