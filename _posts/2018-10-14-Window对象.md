---
title: Window对象
comments: true
date: 2018-09-25 23:50:52
categories: Web
tags: Window
---
**随机数产生方式**
`parseInt(Math.random()*100 + 1)//parseInt取整  Math.random()取0-1(不包括1)的随机数`

**window对象**
```
//window可以不写，默认为window对象。
alert() / prompt() / confirm() / close()
警告框 / 输入框 / 确认框 / 关闭
window.setInterval(delayGo,5000);//setInterval周期执行，时间单位毫秒。
window.setTimeout(delayGo,1000); //只调用一次，但是一般用于函数递归，setTimeout更加灵活。
clearInterval()  /  clearTimeout() //清除计时器
```
```
window.document - 文档对象
window.location - 浏览器地址栏
//location.hostname 返回 web 主机的域名
//location.pathname 返回当前页面的路径和文件名
//location.port 返回 web 主机的端口 （80 或 443）
//location.protocol 返回所使用的 web 协议（http:// 或 https://）
window.history - 历史记录
//history.back() - 与在浏览器点击后退按钮相同
//history.forward() - 与在浏览器中点击向前按钮相同
//history.go(n) - 前进或者后退n步
window.navigator - 浏览器
//navigator.appCodeName - 浏览器代号
//navigator.appName - 浏览器名称
// navigator.appVersion - 浏览器版本
window.screen - 屏幕
//screen.availWidth - 可用的屏幕宽度
//screen.availHeight - 可用的屏幕高度
//screen.colorDepth - 色深
//screen.pixelDepth - 分辨率
```
**拿到html元素(document对象)**
```
document.querySelector("#welcome")//通过选择器拿元素
document.querySelectorAll() //选择器拿到多个元素，返回列表
document.getElementById()//根据id拿元素
document.getElementsByClassName()//根据类名拿元素，返回为列表
document.getElementsByTagName()//根据标签名拿元素，返回为列表
```
**写入到html元素**
```
//div -- 特定标签对应的变量
div.innerHTML //能解释 html 代码
div.textContent //里面只能放文本，代码原样输入
```

**其他知识**
```
Math.random（）随机产生0~1的随机数（前闭后开）
parseInt（）取整
parseFloat（）取小数
```

使用匿名函数并且调用它的方法
![](https://upload-images.jianshu.io/upload_images/13692175-f0428746b42705ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 一、网页上显示当前时间
```html
		<div id="time"></div>
		
		<script type="text/javascript">
			var days = ["日","一","二","三","四","五","六"];
			function showTime(){
				var now = new Date();
				var year = now.getFullYear();
				var month = now.getMonth() + 1;
				var date = now.getDate();
				var hour = now.getHours();
				var minute = now.getMinutes();
				var second = now.getSeconds();
				var day = now.getDay();
				var div = document.getElementById("time");  //得到id为指定的div标签
				div.innerHTML = year + "年" + 
					(month < 10 ? "0":"") + month + "月" + 
					(date < 10 ? "0":"")+ date + "日&nbsp;" +
					(hour < 10 ? "0":"")+ hour + ":" +
					(second < 10 ? "0":"")+ second + "&nbsp;星期" + days[day];
				//div.innerHTML 标签里面的html代码
				//div.textContent 里面只能放文本，代码原样输入
			}
			showTime()  //网页开始没有显示时间，先执行一遍。
			window.setInterval(showTime,1000) //设置时间周期，每1000毫秒执行一次
		</script>
```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-d63ea9852c0b3870.gif?imageMogr2/auto-orient/strip)

#### 二、网页跑马灯
```
		<h1 id="welcome">欢迎来到千峰教育成都校区Python就业班&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h1>
		<script type="text/javascript">
			var str1 = document.getElementById("welcome")
//			document.querySelector("#welcome")//通过选择器拿元素
//			document.querySelectorAll() //选择器拿到多个元素，返回列表
//			document.getElementById()//根据id拿元素
//			document.getElementsByClassName()//根据类名拿元素，返回为列表
//			document.getElementsByTagName()//根据标签名拿元素，返回为列表
			function showStr(){
				var str = str1.textContent;
				str = str.substring(1) + str.charAt(0);//substring-取字串  charAt-取字符
				str1.innerHTML = str;
			}
			showStr();
			window.setInterval(showStr,800);
		</script>
```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-ae91b6d0f7892b66.gif?imageMogr2/auto-orient/strip)


#### 三、网页延时跳转
```
		<h2><span id="counter" >5</span>秒以后自动跳转到百度……</h2>
		<script type="text/javascript">
			var countdown = 5;
			var span = document.getElementById("counter");
			function delayGo(){
				countdown -= 1;
				if (countdown == 0){
					location.href = "http://www.baidu.com";
				}else{
					span.textContent = countdown;
					setTimeout(delayGo,1000); //只调用一次，所以重新调用（setTimeout更加灵活）
				}
				
			}
			window.setTimeout(delayGo,1000); //setTimeout只执行一次
//			window.setInterval(delayGo,5000);//setInterval周期执行
		</script>
```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-c232cd3cb20fdfd5.gif?imageMogr2/auto-orient/strip)


**练习**
----
制作一个程序，随机抽取班级名单，已经抽取到的同学不会继续会抽取
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			#name{
				text-align: center;
				height: 250px;
				width: 600px;
				line-height: 250px;
				color: darkgoldenrod;
				font-size: 90px;
				background-color: #4169E1;
				margin: 170px auto 20px auto;
			}
			#begin{
				height: 80px;
				width: 170px;
				color:crimson;
				background-color:darkgrey;
				font-size: 50px;
				display: block;
				margin: 0px auto;
			}
		</style>
	</head>
	
	<body>
		<div id="name">点击"开始"</div>
		<button onclick="begin()" id="begin">开始</button>
		
		<script type="text/javascript">
			var namelist = ["曹晓芹","吕耐芯","魏世强","樊振霖","何羽","龙汉","吴亮","邓森中",
			"冉钊","曾德浴","李萌","江秀成","李祥","王磊","刘彦材","陈虹州","唐宏进","王建平",
			"李俊橙","于梦娇","王龙","刘诗意","殷安好","刘欢","任思宇","廖鸿业","吕皓洁",
			"李飞江","巫岷骏","张坤","唐小富"];
			var name_now = document.getElementById("name");
			var count = 0;
			function getName(){
				var num = parseInt(Math.random()*namelist.length);
				if (count > 400){
					name_now.textContent = namelist[num];
					count = 0;
					namelist.splice(num,1);
				}else{
					name_now.textContent = namelist[num];
					count += 10;
					window.setTimeout(getName,count);
				}
				if (!namelist.length){
					window.alert("全部随机完，已进行复位~")
					namelist = ["曹晓芹","吕耐芯","魏世强","樊振霖","何羽","龙汉","吴亮","邓森中",
					"冉钊","曾德浴","李萌","江秀成","李祥","王磊","刘彦材","陈虹州","唐宏进","王建平",
					"李俊橙","于梦娇","王龙","刘诗意","殷安好","刘欢","任思宇","廖鸿业","吕皓洁",
					"李飞江","巫岷骏","张坤","唐小富"];
				}
			}
			
			function begin(){
				window.setTimeout(getName,count);	
			}
			
			
		</script>
	</body>
</html>

```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-dd7ce64617f1fb42.gif?imageMogr2/auto-orient/strip)
