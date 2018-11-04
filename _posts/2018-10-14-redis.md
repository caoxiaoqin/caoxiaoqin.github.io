---
title: redis命令
comments: true
date: 2018-10-18 17:54:27
categories: redis
tags: redis 
---
拷贝redis.conf文件到用户主目录
vim redis.conf
bind 修改成自己的内网地址
端口默认 6379
requirepass demo 取消注释，设置口令
# Redis可以实现数据的持久化存储，即将数据保存到磁盘上。 
# Redis的持久化存储提供两种方式：RDB与AOF
appendonly yes 打开AOF模式
```

### 三、启动Redis服务

`redis-server redis.conf > redis.log &`  

说明：输入重定向到redis.log中 ， & 后台运行

```
[root@aliyun ~]# redis-cli -h 172.18.6.69(内网ip)
172.18.6.69:6379> auth demo    
# 验证口令
OK
172.18.6.69:6379> ping
# 检验连接是否成功
PONG
```

现在只能连接自己服务器的redis，因为连接的是内网。

如果希望连接别人的redis，或者自己开放redis，需要防火墙添加端口并且连接公网ip。

**停止redis可以杀掉进程，或者查找jobs后台运行程序终止**

`redis-benchmark -h 172.18.6.69` 基准测试，可以查看服务器性能

### 四、Redis数据类型

**五大数据类型：1、字符串类型（String）；2、哈希表（Hash）：用来保存对象；3、列表（List）；4、集合（Set）：可以去重；5、有序集合（SortedSet）**

查看[Redis中文文档](redisdoc.com)，里面有详细的使用说明

[redis命令大全](http://redisdoc.com)

**redis-server redis.conf >>redis.conf & ：后台**   
**redis-cli -h 172.18.120.124 -a Cao_xiao_qin：开启redis服务器**  

查看服务器的性能   
redis-benchmark -h 172.18.120.124 
##进入redis服务命令 
>>set + key +值： 创建一个键值对  
get + key ： 查到键值对的值  
strlen + key : 查看字符串的长度  
flushall :清空所有数据  
flushdb  : 清空当前数据  
setnx +key    
setex +key    
ttl(time to live):  
keys * :查看所有的key   
mget key1 key2 ..: 查看1  2 的值  
hset + 字典名1 + key1 value1：为字典添加一组键值对  
hget + 字典名1 + key1 ：查看key1的值  
hgetall + 字典名1 ：查看字典里所有的键值对   
hmset +字典名1 +  key1 value1  key3 value3  key2 value2：添加多个键值对  
hdel +字典1 +key1 ：删除字典1 里的key1 的值  
del +字典1：删除字典  
hexists +字典1 +key1：查看字典里是否有key1   
type key1:查看key1的数据类型  
srandmember +集合：取集合里的东西（不拿走）  
spop +集合：取集合里的东西（拿走)  
zadd 集合 20 apple 12 bannana：添加有序集合   
zrange 集合 0 -1 ：取集合里的所有的（有序）  
zrange 集合 0 -1 withscores：  
1)"bannan"  
2) "12"  
3) "apple"  
4) "20"  
zrangebyscore 指定值的范围 10 15：  
1）"bannan"  
zrank 集合名 apple：拿到元素的排位  
(integer) 1    

-----
multi :开启事务环境  
在添加list1 set1 stu1 。。。  
exec : 执行（提交）   
discard: 放弃执行    
shutdown:关闭
******
-----

***在py里连接redis***   
client=redis.StrictRedis(host='',port='',password='')   








