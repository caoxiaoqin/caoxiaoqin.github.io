---
title: Linux01
comments: true
date: 2018-10-9 00:06:46
categories: Linux
tags: linxu
---
### Linux系统安装软件
- 使用包管理工具进行安装 yum / rpm
yum search <name> 搜索
yum -y install <name1>  安装
yum -y remove <name2> 卸载
yum info <name> 查看信息
yum update <name> 更新
yum list installed  查看目前安装的所有软件
systemctl start nginx 启动服务
- 源代码构建安装
wget  ->  gunzip  -> tar -xvf  ->  make && make install  -> export PATH ...（一次性） 或者 修改.bash_profile配置环境变量
  
压缩文件
-gz文件 ----gzip 压缩 / gunzip 解压缩
-xz文件 ---- xz -z压缩 / xz -d 解压缩

### CentOS安装python3.7
**源码安装**
1、wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
2、解压缩
gunzip Python-3.7.0.tgz
3、解归档
tar -xvf Python-3.7.0.tar
4、安装底层依赖库
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
5、安装前的配置
cd Python-3.7.0 进入目录
./configure --prefix=/usr/local/python3 --enable-optimizations
6、构建安装
make && make install
7、配置PATH环境变量（一次性的）
export PATH=$PATH:/usr/local/python3/bin
8、注册软连接（符合链接）-- 非必要
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
硬链接 - 文件的引用，只要引用数不为零，文件就一直存在，相当于分身（ln）
软链接 - 相当于文件的快捷方式（ln - s）

### vim文本编辑器
三种模式：命令模式、编辑模式、末行模式

- 末行模式

查看行号
1、： + 命令
:set nu / set nonu
高亮显示
:syntax on（默认）/syntax off（关闭）
自动对齐
:set autoindent
制表键为4个空格
:set ts=4

查找和替换
`：1,$s/旧/新/gice` （$代表到最后，s代表替换，g-全局模式，i-忽略大小写，c-确认模式，e-忽略错误）

2、/ + 正则表达式 ---搜索 
n - 正向搜索
N - 反向搜索
3、？ + 正则表达式 - 反向搜索

- 命令模式
hjkl / HML / 0$ / w - 移动光标
ctrl + e / ctrl + y / ctrl + f / ctrl + b 翻页
yy复制 / p粘贴 / dd删除 / u撤销 / ctrl + r取消撤销
ctrl + x --> ctrl + o 代码提示

拆分窗口
：vs 垂直拆分
：sp 水平拆分
ctrl +w --> ctrl +w 窗口切换光标
：wqa 全部窗口保存退出