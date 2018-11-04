---
title: CSS基础
comments: true
date: 2018-09-18 23:43:31
categories: Web
tags: CSS
---
#### 一、表单标签
**表单标签 -- form**

表单标签是用来收集用户信息的，是一个容器。
可以将收集到的数据，通过method对应的方式，去发送请求。（发送给action对应的接口）

##### input标签 
单标签

**A、文本输入框和密码输入框（type = text，password）**
```html
		<form action="" method="post">
			<!--a、文本输入框-->
			<span>账号</span>
			<input type="text" name="username" id="" value="账号" placeholder="请输入账号" maxlength="8"/>
			<span>密码</span>
			<input type="password" name="passwd" id="password" value="" placeholder="请输入密码" />
			<input type="submit" value="提交"/>
		</form>
```
（1）、type属性：决定input标签的样式。text（默认）：文本输入框；password：用于输入密码隐藏。
（2）、name属性：区分不同的input对应的值，对标签的显示没有影响。
（3）、value属性：input标签中的值，提交input中的数据给服务器的时候，是以name = value来提交的。（文本输入框中输入的内容就是value的值）。
（4）、placeholder属性：占位符（输入框的提示信息）。
（5）、maxlength属性：约束输入最大位数。

**B、单选按钮（type = radio）**
```
		<input type="radio" name="sex" value="boy" checked="" /><span>男</span>
		<input type="radio" name="sex" value="girl" /><span>女</span>
```
（1）、value：设置这个按钮选中提交的值。
（2）、name值：如果多个按钮只能选中一个，那么这些按钮的name值必须一致。
（3）、一组（name值一样）单选按钮在提交的时候只提交被选中的按钮的name和value值。
（4）、checked：默认初始选择一个。

**C、复选框（type = checkbox）**
```
		<form action="" method="post">
			<input type="checkbox" name="habby" value="篮球"/><span>篮球</span>
			<input type="checkbox" name="habby" value="乒乓球"/><span>乒乓球</span>
			<input type="checkbox" name="habby" value="羽毛球"/><span>羽毛球</span>
			<input type="checkbox" name="habby" value="网球"/><span>网球</span>	
		</form>
```
同一组name值必须一样

**D、普通按钮（type = button）**
```
<input type="button" name="" value="登录" />
```

**E、提交按钮（type = submit）**
```
<input type="submit" name="" id="" value="提交" />
```
自动将当前form中设置了name属性的input标签的值，通过method的方式，提交给action对应的接口。

**F、重置按钮（type = reset）**
```
<input type="reset" name="" id="" value="重置" />
```
将form标签中的input标签所有值恢复初始状态。

**G、文件域（type = file）**
```
<input type="file" name="" id="" value="" />		
```
选择本地文件

#### 二、下拉菜单标签
**下拉菜单标签 -- select**
下拉和多行文本域可以放在form标签里面用于收集信息。

```
		<select name="city">
			<optgroup label="四川省">   
			<option value="成都" selected="selected">成都</option>
			<option value="德阳">德阳</option>
			<option value="眉山">眉山</option>
			<option value="乐山">乐山</option>
			<option value="泸州">泸州</option>
			</optgroup>
			<optgroup label="广东省">   
			<option value="深圳">深圳</option>
			<option value="广州">广州</option>
			<option value="中山">中山</option>
			<option value="佛山">佛山 </option>
			<option value="东莞">东莞</option>
			</optgroup>
		</select>
```
**下拉菜单标签 -- select**
一个select标签对应一个下拉菜单，分组用optgroup属性设置，选项要通过option来列举。selected用来选择默认选项。

#### 三、多行文本域
**多行文本域 -- textarea**
```
<textarea name="message" maxlength="200" placeholder="输入你想写的文字" cols="40"></textarea>
```
（1）、name提交数据对应的名字。
（2）、rows：默认一屏的行数。
（3）、cols：默认的列数。
（4）、placeholder：设置占位符。
（5）、disabled：禁用。

#### 四、div 和 span 标签
**div 和 span 标签是空白标签，没有语意。**
- div是块级标签（一行只能放一个标签）
- span是行内标签（一行可以放多个标签）

块级标签：一个标签占一行
`h1-6 , p , ol , table, hr `
行内标签：一行可以多个标签
 `img , a , input , select , textarea`


#### 五、CSS基础
CSS是web标准中的表现标准，用来规定网页上内容的布局和样式（CSS又叫样式表）。
目前广泛使用的是CSS3。

##### 1、CSS用法
- 固定语法：
   - 选择器{ 属性1：属性值1 ； 属性2：属性值2；…… }
A、选择器：确认样式的对象。
B、属性：固定支持和拥有的，顺序任意。
C、属性值：
(1).数值：
用来表示大小，后面必须跟单位px（像素）或者%（所占百分比）
(2).颜色：
 颜色对应的英语单词
/ #加R-G-B对应的16进制的值（一个颜色值对应2位16进制值）
 直接用RGB值：rgb（R，G，B），rgba（R，G，B，Alpha-透明度） R,G,B范围是0\~255，Alpha范围0\~1

- 常见属性
color ， background-color ，width ， height， font-size ……

**A、内联样式表**
将样式表写在标签的style属性中（每个可见的标签都有style属性）。
```
<p style="background-color: cornflowerblue;color: red;">这是CSS样式表</p>
```
**B、内部样式表**
将样式表写在 head标签的 style标签里面。
```
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			h1{
				background-color: skyblue;
				color: saddlebrown;
			}
		</style>
	</head>
```
```
		<h1>我是标题1</h1>
		<h1>我是标题2</h1>
```

**C、外部样式表**
将样式表写在一个CSS文件中，然后再把head标签中通过 link标签导入。
```
<link rel="stylesheet" type="text/css" href="css/form.css"/>
```

注意：不管在什么情况下，内联样式表的优先级最高。内部和外部样式表执行越后，优先级越高。

##### 2、常用选择器
（1）标签/元素选择器：直接将标签名作为选择器，同时选中网页中所有同类型的标签。
`a{}  ---  选中所有a标签`

（2）id 选择器：通过在id属性值前面加#，就构成了id选择器。选中 id 等于对应值得标签。
id 属性：所有的标签都有 id 属性。
`#p1{}   ---   选中 id 值是 p1 的标签`

（3）class选择器：通过在class 属性值前加 .（点） ，就构成了类选择器。选中class等于对应的值的标签。
`<h1 class="c1">我是class选择器</h1>`
`.c1{}   ---   选中所有class的值是c1的标签`

（4）群组选择器：多个单独的选择器之间使用逗号隔开。选中所有的单独的选择器
`a，p，#p1，.c1{}  ---   选中所有对应的标签`

（5）包含选择器：多个选择器之间使用空格隔开。依次往下寻找，直到最后一个选择器。
`div .c1 p{}   ---   选中div标签中的class值为c1标签中的p标签。`

（6）通配符\*：直接将\*作为选择器。选中当前页面中所有的标签。
`*{}   ---   选中所有标签，包括body标签`

（7）父子选择器：a>b{}
（8）兄弟选择器：a~b{}
（9）相邻兄弟选择器：a+b{}
（10）属性选择器：a[b = c] 
##### 3、伪类选择器
前面的元素选择器、id选择器、class选择器选中的都是标签。而伪类选择器选中的是标签的某个状态，一般使用于超链接和按钮等。
**（1）、语法：**
`标签：状态{}`
说明：
link：初始状态
visited：访问后的状态
active：被激活对应的状态（鼠标点击时）
hover：鼠标悬停在标签上的状态
focus：成为焦点（输入框中用的比较多）

标签：可以通过不同的选择器去选中。

**（2）、爱恨原则：LoVeHAte -- 先爱后恨**
如果想要给一个标签同时给link\visited\hover\active中的两个或者两个以上的状态设置样式，必须遵守爱恨原则。不遵守可能会出问题。


##### 4、选择器的优先级
**(1)、就近原则**
**(2)、具体性原则**
id>类>标签[...]>标签>通配符
**(3)、重要性原则**
`color:red  !important;`

通过不同的选择器选中了同一个标签，谁的优先级高就谁有效。权重值大 --> 高优先级
权重值相同时，后写的选择器优先级高。

权重值
伪类选择器：0001
通配符：0001
元素选择器：0001
class选择器：0010
id选择器：0100
群组选择器：看单独每一个的权重。
包含选择器：多个选择器的权重和。

注意：不管选择器的权重有多高，内联样式的优先级都是最高的。
