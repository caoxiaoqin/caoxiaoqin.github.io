---
title: CSS布局
comments: true
date: 2018-09-19 23:44:44
categories: Web
tags: CSS
---
#### 一、标准流

标准流：浏览器对标签默认的布局方式就是标准流。
**标准流布局原则：**
- 块级标签：
a、块级标签一个占一行（不管标签的宽度是否是浏览器宽度）
b、默认宽度是父标签的宽度，默认高度是内容的高度。
c、直接设置宽高**有效**

- 行内标签：
a、多个行内标签可以一行显示。
b、默认宽高是内容的宽高。
c、直接设置宽高**无效。**

- 行内块标签：
a、多个行内块标签可以在一行显示。
b、默认宽高是内容的宽高。
c、直接设置宽高**有效。**

**display属性：转换标签的性质**
block：块级
inline：行内
inline-block：行内块

注意：行内块和其他标签之间默认会有个间隙，而且无法消除，所以一般不建议使用。

#### 二、浮动 -- float
通过给float属性赋值为 left 或者 right 来让标签浮动。浮动会让标签脱流，脱流后原来的标准流布局方式不适用了。
`float:left;` 按照浏览器的左上角为起点。
`float:right`按照浏览器的右上角为起点。

浮动的目的：让竖着显示的可以横着来（针对块）

**浮动的效果：
一行可以显示多个；默认的宽高是内容的大小；可以设置宽度和高度**

注意事项：
a、如果同一级的标签，后面的需要浮动，前面的也需要浮动，否则可能会出现一些显示问题。
b、浮动的标签不占位置，不浮动的占位置。

**利用浮动产生文字环绕效果**
结论：被环绕的标签浮动，文字对应的标签不浮动。

**清除浮动**：不是将标签的浮动给去掉，而是清除因为浮动而产生的高度塌陷的问题。

**高度塌陷**：在文档流中，父元素的高度默认是被子元素撑开的，也就是子元素多高，父元素就多高。
但是当为子元素设置浮动以后，子元素会完全脱离文档流，此时将会导致子元素无法撑起父元素的高度，导致父元素的高度塌陷。
由于父元素的高度塌陷了，则父元素下的所有元素都会向上移动，这样将会导致页面布局混乱。

**高度塌陷产生原因**：父标签不浮动，子标签浮动，并且不设置父标签的高度，就会产生高度塌陷问题。

解决方案：
1、在后面添加一个div空盒子，设置样式为clear：both
```
<div id="" style="clear: both;">
</div>
```
2、给父标签添加样式，设置overflow的值为hidden。

3、万能清除法
```
			#father:after{
				display: block;
				clear: both;
				content: '';
				visibility: hidden;
				height: 0;
				
			}
			#father{
				zoom: 1;
			}
```

#### 三、定位
CSS中可以通过left，right，bottom，top属性来设置标签上下左右的距离。但是要通过position属性设置参考对象。

**absolute**：相对第一个非static/initial(默认值)父标签进行定位。

**relative**：相对于自己在标准流中的位置来定位。（当标签本身不希望去定位，只是想让自己的子标签可以相对自己定位时使用。）

**fixed**：相对于浏览器定位。（滚动时位置相对于浏览器不变）

**sticky**：当网页的内容不超过一屏（不滚动），按照标准流定位；超过一屏就相对浏览器定位。

initial：默认值，没有相对定位。

**技巧：当遇到某个方向的定位无效时，可以尝试让标签浮动然后定位。**

#### 四、盒子模型
html中所有可见的标签都是一个盒子模型：包括长和宽决定的content、padding、border、margin。
其中content、padding、border是可见的，margin是不可见的。
![](https://upload-images.jianshu.io/upload_images/13692175-934c0a4ce5c85c94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



**1、content（内容）**：设置width 和height影响的就是内容部分的大小。添加子标签、内容都是放在内容部分的。

**2、padding（内边距）**：内容外围，可见部分，如果标签有背景颜色，那么这个部分的颜色和内容一致。
```html
padding-left: 20px;
padding:10px; /*所有*/
padding:10px 20px; /*上下和作业*/
padding:10px 20px 30px 40px; /*顺时针*/
```

**3、border（边框）**：border在padding的外围，如果没有padding，就在内容的外围，可以设置颜色。
`border:宽度 风格 颜色`
样式：solid（实线）、dashde（虚线）、dotted（点划线）double（双线）

**4、margin（外边距）**：不可见。主要用来占位。

#### 五、其他常用属性
**1、字体相关属性**
- 字体颜色：color
- 字体大小：font-size
- 字体名：font-family
- 字体加粗：font-weight：bolder（更粗的）、bold（加粗）、normal（常规）、100-900
- 字体倾斜：font-style：italic、oblique、normal

**2、文本修饰 -- text-decoration**
none：取消修饰
underline：下划线
overline：上划线
line-through：删除线

**3、对齐方式**
text-align：left、right、center（文字水平方向居中）

margin：0px auto;（水平居中）
一行内容在垂直方向居中，可以通过将line-height的值设置为父标签的height值。（垂直居中）
```html
height:40px;
line-height:40px;
```

**4、首行缩进 -- text-indent**
`text-indent:2em`
em代表一个空格的长度

**5、字间距 -- letter-spacing**
`letter-spacing:2em`

**6、背景图片**
格式：`babackground-image:图片地址、是否平铺 x方向坐标 y方向的坐标 颜色`
no-repeat/repeat/repeat-x/repeat-y(不平铺、平铺、x方向平铺、y方向平铺)

`background-image: url(img/beauty.png) no-repeat center center yellow;`   center表示在水平或者垂直方向居中。
默认图片不够时，背景图片会平铺。

**7、设置圆角**
```
border-radius: 20px;
border-bottom-left-radius: 20px;
```

#### 六、补充
**制作网页首页title图标**
![](https://upload-images.jianshu.io/upload_images/13692175-f71a7cb24ddba76e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**一般写网页前一定要先将标签默认的margin值和padding值关闭。**
```html
*{ 
  margin:0;
  padding:0;
  position:relative;
}
```

**实现元素居中**
[CSS中垂直居中的11种方式](https://www.cnblogs.com/zhouhuan/p/vertical_center.html)
[CSS中元素6种水平居中](https://www.w3cplus.com/css/elements-horizontally-center-with-css.html)


**练习**
----
HTML代码

```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>京东-欢迎登录</title>
		<link rel="stylesheet" type="text/css" href="css/test.css"/>
	</head>
	<body>
		<div id="logo">
			<img src="img/logo.png" />
		</div>
		<div id="logo_test">
			<font>欢迎登录</font>
		</div>
		<div id="q">
			<img src="img/q-icon.png" />
			<div id="q1">
				<font id="id1">登录页面，调查问卷</font>
			</div>
		</div>
		<div id="tiaowen" style="background-color: blanchedalmond;">
			<p align="center">依据《网络安全法》，为保障您的账户安全和正常使用，请尽快完成手机号验证！ 新版《京东隐私政策》已上线，将更有利于保护您的个人隐私。</p>
		</div>
		<div id="bgpic">
			<img src="img/bg.png" width="1280px"/>
		</div>
		
		<div id="login" style="background-color:white;">
			<div id="d01">
				<p><font size="1">京东不会以任何理由要求您转账汇款，谨防诈骗。</font></p>
			</div>
			<div id="login1">
				<font size="5" id="saoma">扫码登录</font>
			</div>
			<div id="login2">
				<font size="5" id="denglu">账户登录</font>
			</div>
			<p id="forget">忘记密码</p>
			
			<div id="qq">
				<!--<div id="qq_img">-->
				<img src="img/qq.png" style="float: left;"/>
				<!--</div>-->
				<font size="2" id="qq1">QQ</font>
				<img src="img/weixin.png" id="vx1" />
				<font size="2" id="vx2">微信</font>
				<img src="img/right.png" id="zhuce01"/>
				<font size="3" id="zhuce02">立即注册</font>
			</div>	
		</div>
		
		
		<div id="user">
			
			<form action="" method="post">
				<img src="img/user.png" />
				<input type="text" name="user" id="user01" value="" placeholder="邮箱/用户名/已验证手机"/><br />
				<img src="img/password_icon.png" />
				<input type="password" name="password" id="password" value="" placeholder="密码"/><br />
				<div id="">
					<input type="submit" name="" id="form_login" value="登录" />
				</div>
			</form>
		</div>

		<font size="2" id="p1">关于我们 </font>
		<font size="2" id="shu1">丨</font>
		<font size="2" id="p2">联系我们 </font>
		<font size="2" id="shu2">丨</font>
		<font size="2" id="p3">人才招聘 </font>
		<font size="2" id="shu3">丨</font>
		<font size="2" id="p4">商家入驻 </font>
		<font size="2" id="shu4">丨</font>
		<font size="2" id="p5">广告服务</font>
		<font size="2" id="shu5">丨</font>
		<font size="2" id="p6">手机京东</font>
		<font size="2" id="shu6">丨</font>
		<font size="2" id="p7">友情链接</font>
		<font size="2" id="shu7">丨</font>
		<font size="2" id="p8">销售联盟</font>
		<font size="2" id="shu8">丨</font>
		<font size="2" id="p9">京东社区</font>
		<font size="2" id="shu9">丨</font>
		<font size="2" id="p10">京东公益</font>
		<font size="2" id="shu10">丨</font>
		<font size="2" id="p11">English Site</font>
		<font size="2" id="p12">Copyright © 2004-2018  京东JD.com 版权所有</font>
	</body>
</html>

```

CSS代码
```
body{
	margin: 0px;
}
#zhuce02:hover,#vx2:hover,#qq1:hover,#forget:hover,#id1:hover,#p1:hover,#p2:hover,#p3:hover,#p4:hover,#p5:hover,#p6:hover,vp7:hover,#p8:hover,#p9:hover,#p10:hover,#p11:hover{
	color: red;
	text-decoration: underline;
}
#logo{
	position: absolute;
	left: 130px;
	top: 24px;
}
#logo_test{
	position: absolute;
	left: 320px;
	top: 45px;
	font-size: 25px;
}
#q{
	position: absolute;
	left: 992px;
	top: 75px;
}
#q1{
	position: relative;
	left: 30px;
	top:-22px;
	font-size: 13px;
}
#tiaowen{
	position: absolute;
	width: 100%;
	top: 100px;
	font-size: 13px;
}
#bgpic{
	position: absolute;
	width: 100%;
	top: 143px;
}
#login{
	position: relative;
	width: 348px;
	height: 400px;
	left: 850px;
	top: 148px;
}
#d01{
	position: absolute;
	height: 40px;
	padding: 0px 42px;
	line-height: 10px;
	background-color: blanchedalmond;
	text-align: center;
}
#login1{
	position: absolute;
	top: 50px;
	left: 50px;
}
#login2{
	position: absolute;
	top: 50px;
	left: 210px;
}
#forget{
	position: absolute;
	top: 225px;
	left: 260px;
	font-size: 10px;
}

#user{
	position: absolute;
	top: 280px;
	left: 890px;
}
#user01{
	position: relative;
	top: -14px;
	left: -7px;
	height: 30px;
	width: 230px;
}
#password{
	position: relative;
	top: -14px;
	left: -7px;
	height: 30px;
	width: 230px;
}
#form_login{
	position: absolute;
	top:150px;
	left: -30px;
	height: 34px;
	width: 270px;
	margin-left: 28px;
	margin-right: 28px;
	background-color: rgb(229,56,60);
}
#qq{
	position: absolute;
	left: 19px;
	top: 360px;
}
#qq1{
	float: left; 
	position:absolute; 
	left: 25px;
	top: 5px;
}
#vx1{
	float: left; 
	position:absolute; 
	left: 52px;
}
#vx2{
	float: left; 
	position:absolute; 
	left: 80px;
	top: 5px;
	width: 50px;
}
#zhuce01{
	float: left; 
	position:absolute; 
	left: 200px;
}
#zhuce02{
	float: left; 
	position:absolute; 
	left: 226px;
	top: 2px;
	width: 100px;
}
#saoma:hover,#denglu:hover{
	color: rgb(229,56,60);
	font-weight:bold ;
}

#p1{
	position: absolute;
	top: 605px;
	left: 200px;

}
#shu1{
	position: absolute;
	top: 605px;
	left: 260px;
}
#p2{
	position: absolute;
	top: 605px;
	left: 280px;
}
#shu2{
	position: absolute;
	top: 605px;
	left: 340px;
}
#p3{
	position: absolute;
	top: 605px;
	left: 360px;
}
#shu3{
	position: absolute;
	top: 605px;
	left: 420px;
}
#p4{
	position: absolute;
	top: 605px;
	left: 440px;
}
#shu4{
	position: absolute;
	top: 605px;
	left: 500px;
}
#p5{
	position: absolute;
	top: 605px;
	left: 520px;
}
#shu5{
	position: absolute;
	top: 605px;
	left: 580px;
}
#p6{
	position: absolute;
	top: 605px;
	left: 600px;
}
#shu6{
	position: absolute;
	top: 605px;
	left: 660px;
}
#p7{
	position: absolute;
	top: 605px;
	left: 680px;
}
#shu7{
	position: absolute;
	top: 605px;
	left: 740px;
}
#p8{
	position: absolute;
	top: 605px;
	left: 760px;
}
#shu8{
	position: absolute;
	top: 605px;
	left: 820px;
}
#p9{
	position: absolute;
	top: 605px;
	left: 840px;
}
#shu9{
	position: absolute;
	top: 605px;
	left: 900px;
}
#p10{
	position: absolute;
	top: 605px;
	left: 920px;
}
#shu10{
	position: absolute;
	top: 605px;
	left: 980px;
}
#p11{
	position: absolute;
	top: 605px;
	left: 1000px;
}
#p12{
	position: absolute;
	top: 630px;
	left: 505px;

}

```

效果如下
![](https://upload-images.jianshu.io/upload_images/13692175-b93533a5aeaeccfd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
