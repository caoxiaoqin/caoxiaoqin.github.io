---
title: hexo博客云服务器端搭建
comments: true
date: 2018-10-16 20:35:26
categories: Hexo
tags: hexo
---

### 云服务器端配置

#### 安装 git 和配置

1、使用`git --version`查看git版本，如果电脑不存在，就进行git安装

2、创建git仓库，用于存放博客网站资源

```
mkdir /home/git/
chown -R $USER:$USER /home/git/
chmod -R 755 /home/git/
```

然后，执行如下命令：

```
cd /home/git/
git init --bare hexoBlog.git
```
3、创建一个新的 git 钩子，用于自动部署

-   在 `/home/git/hexoBlog.git` 下，有一个自动生成的 `hooks` 文件夹。我们需要在里边新建一个新的钩子文件 `post-receive`。

   ```
   vim /home/git/hexoBlog.git/hooks/post-receive
   ```

- 按 `i` 键进入文件的编辑模式，在该文件中添加两行代码（将下边的代码粘贴进去)，指定 Git 的工作树（源代码）和 Git 目录（配置文件等）.

   ```
   #!/bin/bash
   git --work-tree=/home/hexoBlog --git-dir=/home/git/hexoBlog.git checkout -f
   ```

- 修改文件权限，使得其可执行。

   ```
   chmod +x /home/git/hexoBlog.git/hooks/post-receive
   ```
   到这里，我们的 git 仓库算是完全搭建好了。下面进行 Nginx 的配置。

#### Nginx配置

1. 安装 Nginx

```
yum install -y nginx

```

2. 启动 Nginx

```
service nginx start

```

3. 测试 Nginx 服务器

```
wget http://127.0.0.1

```

能够正常获取以下欢迎页面说明Nginx安装成功。

```
Connecting to 127.0.0.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 43704 (43K) [text/html]
Saving to: ‘index.html’

100%[=======================================>] 43,704      --.-K/s   in 0s

2018-03-09 23:04:09 (487 MB/s) - ‘index.html’ saved [43704/43704]

```

4. 测试网页是否能打开
   在浏览器中输入服务器 ip 地址，就是服务器的公网 ip。

5. 配置 Nginx 托管文件目录

   1. 接下来，创建 `/home/hexoBlog`目录，用于 Nginx 托管。

   ```
   mkdir /home/hexoBlog/
   chown -R $USER:$USER /home/hexoBlog/
   chmod -R 755 /home/hexoBlog/

   ```

   2. 查看 Nginx 的默认配置的安装位置

   ```
   nginx -t

   ```

   3. 修改Nginx的默认配置，其中 cd 后边就是刚才查到的安装位置（每个人可能都不一样）

   ```
   vim /etc/nginx/nginx.conf

   ```

   4. 按方向键，找到如下位置

   ```
   server {
       listen 80 default_server;
       listen [::]:80 default_server;
       root /home/hexoBlog;    #需要修改
       
       server_name www.bujige.net; #需要修改
       
       # Load configuration files for the default server block.
       include /etc/nginx/default.d/*.conf;
       location / {
       }
       error_page 404 /404.html;
           location = /40x.html {
       }

   ```

   按`i`键进入插入模式，将其中的 root 值改为 `/home/hexoBlog` （刚才创建的托管仓库目录）。
   将 server_name 值改成你的域名。

   5. 重启 Nginx 服务

   ```
   service nginx restart

   ```

   至此，服务器端配置就结束了。接下来，就剩下本地 hexo 的配置更改了。