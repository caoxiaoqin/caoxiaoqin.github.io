---
title: JavaScript
comments: true
date: 2018-09-21 23:47:29
categories: Web
tags: js
---
### 一、JS介绍
##### 1、什么是JS
javaScripy = ECMAScript(js语法) + BOM - window(浏览器对象模型) + DOM - document(文档对象模型)
js 是 javascript 的缩写，是一门专门用来控制网页内容的行为的脚本语言。
js 就是 web 标准中的行为标准。

##### 2、在哪儿写 JS 代码
1、写在标签的内容（写在标签的行为相关的属性中，比如按钮的onclicked）。

2、写在 script 标签中（script标签可以放在html 的任何位置，但是一般放在head或者body中）。

3、写在外部的 js 文件中

导入
```
	<script type="text/javascript" src="js/new_file.js">	
	</script>
```

##### 3、js 能做些什么事情
1、js 可以在网页中插入html 代码。
2、可以修改标签的内容。
3、修改标签的样式。

### 二、JS基础语法
##### 1、注释
单行注释：单行注释前面加‘//’
多行注释：
/*这是多行注释
\*这是注释的第二行
*/

##### 2、标识符
要求是由数字、字母、下划线和 $符 组成，数字不能开头。
`var h1`

##### 3、基本数据类型。
注意：JS中大小写敏感，没有元组和集合。

**常规**
Number：数字（包含所有数字）
Boolean（布尔类型）
String（字符串）
Array（数组）
Object（对象）

**特殊**
NaN（不存在的数字）
null（空，一般用来清空变量中的内容）
undefined（变量没有赋值时，默认是undefined）
console.log（）   //在控制台打印内容

##### 4、字面量
Number字面量：所有的数字（支持科学技术法，不支持复数）。

Boolean字面量：true、false（小写）。

String字面量：单引号或者双引号包围的字符集，支持转义字符（和python相同）。

Array字面量：相当于python中的列表。

Object对象字面量：相当于python中的‘字典+对象’
注意：key相当于属性，value相当于属性的值。
```
var dict = {a:100, name:200}
console.log(dict)
```
typeof()查看数据类型。

##### 5、js中的语句
1、一条语句结束后可以写分号，也可以不写，但是一行要写多行就必须写分号。
2、js中没有缩进的语法要求，需要代码的时候使用{}

##### 6、js中变量的声明
**(1)、var声明变量的关键字。**
`var 变量名` 或者 `var 变量=初值`
**(2)、变量名：标识符**
不能是js中的关键字；驼峰式命名（第一个单词的首字母小写，后面每个单词首字母大写），见名知义
`var age ;  var name`
`var age1 = 10, name ,studyId`
一个变量存储多种类型的值。

##### 7、js 中的运算符
包含：数学运算符、比较运算符、逻辑运算符、赋值元素运算符、三目运算符。

**数学运算符**：+、-、*、/、%、\*\*(js7才有)、++（自加1）、--（自减1）
注意：
```
b = a++：在赋值时先赋值，再加一
b = ++a：先加1，再赋值。 
```
**比较运算符**：>,<,==,>=,<=,!=,===,!==,>==,<==.
结果都是布尔值。
==：是否相等（判断值是否相等）
===：是否完全相等（判断值和类型是否相等）
![](https://upload-images.jianshu.io/upload_images/13692175-4d0ef2be2285b4e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**逻辑运算符**
&&（与）、||（或）、！（非）

**赋值运算符**
=，+=，-=，*=，/=，%=，%=……

**三目运算符 -- ？：**
语法：
`表达式1?值1:值2` --->  判断表达式1的值是否为真，为真整个运算的结果就是值1，否则值2.

运算顺序：数学>比较>逻辑>三目>赋值

##### 8、js中的分支语句
**if语句**
```
if(条件语句1){
  代码段1
}else if(条件语句2){
  代码段2
}else{
  代码段3
}
```
执行过程：先判断条件语句1是否为true，为true就执行代码段1，再判断条件2……
```
var a = 2
if(!(a%2)){
	console.log('偶数')
}else{
	console.log('奇数')
}

偶数
```
**swith语句**
```
switch(表达式){
	case 值1:{
		代码段1
	}
	case 值2:{ 
		代码段2
	}
	···
	default:{
		
	}
}
```
执行过程：先计算表达式的值，然后用这个值去和后边case关键字后面的值一一对比，找到第一个和表达式的值相等的case，然后将这个case作为入口，依次执行这个case后边所有的代码。直到遇到switch和break结束。如果没有找到和表达式的值相等的case就执行default后面的代码。
```
练习一：打印星期
var week = 4
switch(week){
	case 0:{
		console.log("星期天")
		break
	}
	case 1:{
		console.log("星期一")
		break
	}
	case 2:{
		console.log("星期二")
		break
	}
	case 3:{
		console.log("星期三")
		break
	}
	case 4:{
		console.log("星期四")
		break
	}
	case 5:{
		console.log("星期五")
		break
	}
	case 6:{
		console.log("星期六")
		break
	}
}

练习二：输入成绩查看分数划分
var score = 3
switch(score){
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:{
		console.log("不及格")
		break
	}
	case 6:{
		console.log("及格")
		break
	}
	case 7:{
		console.log("良好")
		break
	}
	case 8:{
		console.log("良好")
		break
	}
	case 9:{
		console.log("优秀")
		break
	}
	case 10:{
		console.log("优秀")
		break
	}
	default:{
		console.log("输入不正确！")
	}
}
```

##### 9、循环
js中的循环结构分为：for循环和while循环。
**for-in循环**
```
for var 变量 in 序列{
	循环体
}
```
执行过程：依次从序列中取元素中对应的索引值，每取一个执行一次循环体。
```
var str = 'abcd'
for (var i in str){
	console.log(str[i])
}
//遍历字符串和数组，取对应的下边，遍历对象，取对应的属性名
a
b
c
d
```

**for循环**
```
for(表达式1；表达式2；表达式3){
  循环体
}
```
执行过程：先执行表达式1，再判断表达式2的结果是否为true，如果为true，就执行循环体，执行完循环体再执行循环体3，然后再判断表达式2的结果是否为true，直到表达式2的结果为false为止。

**while循环**
```
while（条件语句）{
  循环体
}
```

**do - while循环**
```
do{
  循环体
}while（条件语句）
```
```
var sum = 0
var i = 1
do{
	sum += i
	i++
}while(i<=100)
console.log(sum)
```

##### 10、函数
```
function 函数名（参数列表）{
  函数体
}
```
函数调用时要保证每个参数都有值！不支持不定长参数。
js中函数如果没有返回值，那么返回值是undefined

逗号表达式：如果多个表达式之间用逗号隔开，整个表达式的结果是最后那个值。

注意：js中不能同时返回多个值（因为不支持元组）

js中，函数也可以作为变量

 **函数的另外一种声明方式**
```
var 变量 = function(参数列表){
  函数体
}
```

##### 11、数据类型
new 类型名（值）  -->  可以将其他类型的数据转换成相应类型的值。
**a、数字类型 -- Number**：所有的数字类型。
**b、布尔 -- Boolean**：true和false
`var bool = new Boolean（"a"） //true`
总结：所有为0为空的转换成布尔是false，NaN，null，undefined都是false
**c、字符串 -- String**
- 获取单个字符：通过字符串[下标]
- js中下标只支持0~长度-1，不支持负值。并且不支持切片
- 获取字符串长度：**字符串.length**
- 运算符：比较和加操作
如果其他的数据类型和字符串相加，都是现把其他数据类型转换成字符串，然后做字符串的拼接操作。

**d、数组**
有序，可变的，元素类型可以是任意的数据