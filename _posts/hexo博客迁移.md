---
title: hexo博客迁移
comments: true
date: 2018-10-15 19:27:34
categories: Hexo
tags: hexo
---

### 方法一：把原来的配置文件进行备份转移

#### 1、复制配置文件

其中只需要把 source、themes、scaffolds配置文件_config.yml备份即可，其他相关文件会自动生成。

#### 2、安装Node.js

`sudo apt-get install nodejs`
`sudo apt-get install npm`

#### 3、安装hexo

`sudo npm install -g hexo`

####  4、新建项目文件夹，cd进入

`hexo init`

#### 5、将备份的文件覆盖到新文件夹

使用`hexo g && hexo s`查看本地能否运行
创建新的markdown文件`hexo new 文件名`

上传文件 `hexo clean && hexo g && hexo d`


#### 遇到问题1：

`hexo deploy ` 后出现错误：`ERROR Deployer not found: git`

#### 解决：

`npm install `--`save hexo-deployer-git`即可

####  遇到问题2：

`hexo deploy` 后依然出错：`Error: *** Please tell me who you are.`

#### 解决：

`git config --global user.email "you@example.com"`

`git config --global user.name "Your Name"`

### 方法二：

待补充...
