---
title: Git
comments: true
date: 2018-09-30 00:02:50
categories: Git
tags: git
---
Git是一个版本控制工具 -- 分布式的版本控制系统
Mercury - python开发的版本控制软件
-----
##### Git操作
配置邮箱和用户名
git config --global user.name <user>
git config --global user.email <email>
---
- git init -- 初始化 -- 将一个文件夹初始化成git本地仓库
- git add <file>  -  将文件添加到暂存区
- git reset HEAD <file>  -  将文件从暂存区移除
- git checkout -- <file>  -  将暂存区的文件恢复到工作区
---
- git status  -  查看暂存区的状态
---
- git commit  -  将暂存区的内容提交到本地仓库
---
- git log  -  查看提交日志（当前版本之前的版本）
- git reflog  -  查看日志（所有的版本）
---
- git reset <id>  -  回到指定版本
- git HEAD^  -  回到上一个版本

##### 代码托管平台  -  用别人提供的Git服务器
全球最大的代码托管平台  -  github.com
国内 gitee.com    coding.net

1、git clone <url>  -  将服务器上的项目克隆到本地
2、现在本地实施版本控制
3、git push  -  将代码推送到服务器（上传）
4、git pull - 将服务器代码同步到本地（下载）-- 看到他人更新
