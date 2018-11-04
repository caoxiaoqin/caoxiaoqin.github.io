---
title: Break和Continue
date: 2018-08-24 18:52:12
comments: true
categories: Python
tags: 
---
## break 、continue 、else、print的用法 
补充：python控制台输入函数--- input（）函数
 **n = input（'请输入：'）**
说明：
1、程序运行到input，会停下来，等待输入才继续执行
2、输入结束：遇到return就结束
3、获取的输入内容的类型是字符串（不管输入时什么）

### 1、 break:
程序执行中，只要遇到break，就结束包含break的最近的一个循环

练习：
```
#练习：随机生成一个整数，然后去猜，猜中为止
import random 

number = random.randint(0,100)
count = 0
while True:
  input_number = int(input('请输入0~100中想要输入的数字：'))
  if input_number < number: 
    print('小了小了~~\n')
  elif input_number == number:
    print("恭喜你答对了！")
    break
  else :
    print(' 大了大了~~\n')


结果：
请输入0~100中想要输入的数字：50
 大了大了~~

请输入0~100中想要输入的数字：25
小了小了~~

请输入0~100中想要输入的数字：37
恭喜你答对了！

```
### 2、continue
continue:循环执行到continue后，结束当次循环，跳转到下次循环
### 3、else
else：循环结束后要执行的代码

比如：
```
while 条件语句：
  循环体
else：
  循环后要执行的语句
```
###### “while-else”是一个整体，如果break，结束出整个循环，不会执行else中的内容
### 4、print
格式：
```
print(*objects, sep=' ', end='\n', file=sys.stdout)
```
说明：
objects --表示输出的对象。输出多个对象时，需要用 , （逗号）分隔。
sep -- 用来间隔多个对象。
end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符。
file -- 要写入的文件对象。

（1）、一个print（）打印完内容后，默认会换行。
（2）、一个print（）可以打印多个内容，多个内容之间用空格隔开。
（3）、设置一个print打印结尾结束后的样式（默认换行）。
end = 字符串
（4）、同时打印多个内容，中间的间隔（默认空格）
sep = ' '

