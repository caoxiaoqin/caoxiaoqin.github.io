---
title: JS中的事件处理
comments: true
date: 2018-09-26 23:54:09
categories: Web
tags: js
---
### 一、JavaScript中的事件处理

##### 1、在标签上使用onXXX属性来进行事件绑定（不推荐使用）
```
		<button onclick="sayHello()">按钮1</button>
		<script type="text/javascript">
			function sayHello(){
				alert("Hello!");
			}
```

##### 2、通过代码获取标签绑定onXXX属性（不推荐使用）
```
		<button id="button1">按钮1</button>
		
		<script type="text/javascript">
			var button1 = document.getElementById("button1");
			button1.textContent = "点我呀！";
			button1.onclick = sayHello;
			function sayHello(){
				alert("Hello!");
			}
		</script>
```

##### 3、通过diamante获取标签然后使用addEventListener绑定事件（推荐）
方法一：内部JS
```html
		<button id="button1">按钮1</button>
		
		<script type="text/javascript">
			var button1 = document.getElementById("button1");
			//判断因为IE浏览器低版本不兼容
			if (button1.addEventListener){
				button1.textContent = "点我呀！";
				button1.addEventListener("click",sayHello);
				button1.addEventListener("click",sayGoodbye);
				button1.addEventListener("click",function(){
					button1.removeEventListener("click",sayHello); //移除事件监听
					button1.removeEventListener("click",sayGoodbye);
				})
			}else{ 
				//低版本IE浏览器使用的代码
				button1.attachEvent("onclick",sayHello);
				button1.attachEvent("onclick",sayGoodbye);
				button1.attachEvent("click",function(){
					button1.detachEvent("onclick",sayHello); //移除事件监听
					button1.detachEvent("onclick",sayGoodbye);
				})
			}

			function sayHello(){
				alert("Hello!");
			}
			function sayGoodbye(){
				alert("Goodbye！")
			}
		</script>
````
方法二：外部封装JS函数
 ```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<button id="button1">按钮1</button>
		
		<script src="js/new_file.js"></script>
		<script type="text/javascript">
			var button1 = document.getElementById("button1");
			// 绑定事件的回调函数（callback function）
			// 你知道事件发生的时候，但是不知道事件什么时候发生，只是进行绑定。
			bind(button1, "click", sayHello);
			bind(button1, "click", sayGoodbye);
			bind(button1, "click", function(){
				onbind(button1, "click", sayHello);
			})

			function sayHello(){
				alert("Hello!");
			}
			function sayGoodbye(){
				alert("Goodbye！")
			}
		</script>
	</body>
</html>

//js文件
function bind(elem, event, fn){
	if (elem.addEventListener){
		elem.addEventListener(event, fn);
	}else{
		elem.attachEvent("on" + event, fn);
	}
}

function onbind(elem, event, fn){
	if (elem.removeEventListener){
		elem.removeEventListener(event, fn);
	}else{
		elem.detachShader("on" + event, fn);
	}
}

```

**在事件回调函数中获取事件源（易错点）**
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<div id="buttons">
			<button>button1</button>
			<button>button2</button>
			<button>button3</button>
			<button>button4</button>
			<button>button5</button>
		</div>
		
		<script src="js/javascript.js"></script>
		<script type="text/javascript">
			var buttons = document.querySelectorAll("#buttons>button");
			for (var i = 0; i<buttons.length; i+=1){
			//如果希望在事件回调函数中获得事件源
			//应该通过事件对象的target属性去获取事件源		
				bind(buttons[i], "click", function(evt){   
					//取事件源不能用下标去获取
					evt = evt || window.event; //兼容ie代码
					evt.target.textContent = "欧耶";
				})
			}

		</script>
	</body>
</html>

```

### 二、事件回调函数和事件对象

绑定事件监听器的函数都需要传入事件的回调函数，程序员因为事件发生的时候要做什么，但是不知道什么时候发生，所以传入一个函数在将来发生事件的时候，由事件调用，这种就叫回调函数。

回调函数的第一个参数代表事件对象（封装了和事件相关的所有信息），对于低版本的IE，可以通过window.event来获取事件对象。

**事件对象的属性和方法：**
**1、target / srcElement(IE) - 事件源（引发事件的标签）**

**2、阻止事件的默认行为，比如：a标签  --> preventDefault()**
```
					if (evt.preventDefault){
						evt.preventDefault();
					}else{
						evt.returnValue = false; //兼容ie
					}
```

**3、事件的捕获和冒泡**
**事件冒泡   内 --> 外（子代-->父代）（默认 false）
事件捕获   外 --> 内 （true）**

停止事件传播（捕获和冒泡） -- `stopPropagation()`
IE浏览器只有冒泡 -- `cancelBubble = true`

**猜数字游戏（网页版）**
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>

	</head>
	<body>
	
		<input type="number" id="input" placeholder="猜0~10的数字"/>
		<input type="button" id="confirm" value="确定">	
		
		<script type="text/javascript">
			var count = 0;
			var num = parseInt(Math.random()*11);
			var guess = document.getElementById("input");
			var confirm = document.getElementById("confirm");
			confirm.addEventListener("click", guess_number);
			// 判断回车
			guess.addEventListener("keydown",function(evt){
				evt = evt || window.event;
				if (evt.keyCode == 13 || evt.which == 13){
					guess_number();
				}
			})
			
			function guess_number(){
				var thyAnswer = parseInt(guess.value);
				count += 1;
				if (thyAnswer > num){
					alert("大了大了~");
				}else if(thyAnswer < num){
					alert("小了小了~");
				}else if(thyAnswer == num){
					alert("恭喜你猜对了，一共猜了"+count+"次！");
					confirm.disabled = true; //禁止按钮
					guess.disabled = true;  //禁止输入框
				}
				guess.value = "";  //清除文本框内容
				guess.focus();  //获得焦点
	
			}
		</script>
	</body>
</html>
```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-79cbfa53d85b8dd7.gif?imageMogr2/auto-orient/strip)

### 三、JS中创建对象常用方法
1、
![](https://upload-images.jianshu.io/upload_images/13692175-6f215fff8a7c4b3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2、
![](https://upload-images.jianshu.io/upload_images/13692175-4cf4b1ab7a84ffe4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


----
**练习**

一.图片3s自动切换，鼠标事件触发停止切换。
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			#span{
				color: #008000;
				text-align: center;
				font-size: 20px;
			}
			#pic{
				margin-left: 120px;
			}
		</style>
	</head>
	<body>
		<p id="span">每3s切换一次图片,鼠标放上停止切换，离开时继续切换</p><br/>
		<img src="img/slide-1.jpg" id="pic"/>
		
		<script type="text/javascript">
			var slipeImg = document.getElementById("pic");
			var timer = setInterval(slipe,3000);
			var count = 1;
			slipeImg.addEventListener("mouseover",overSlipe);
			slipeImg.addEventListener("mouseout",outSlipe);
			
			function overSlipe(){
				clearInterval(timer);
			}
			function outSlipe(){
				timer = setInterval(slipe,3000);
			}
			function slipe(){
				if (count == 4){
					count = 1
					slipeImg.src="img/slide-" + count + ".jpg";
				}else{
					count += 1;
					slipeImg.src="img/slide-" + count + ".jpg";
				}
			}
		</script>
	</body>
</html>
```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-0a06e5337ed46f3b.gif?imageMogr2/auto-orient/strip)

二、实现上题的功能的前提下，点击小图标可以切换到对应的图片
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			#pic{
				margin-left: 450px;
			}
			#pic_small{
				margin-left: 460px;	
			}
		</style>
	</head>
	<body>
		
		<img src="img/pic1.jpg" id="pic"/>
		<div id="pic_small">
			<img src="img/thumb-1.jpg" id="small1"/>
			<img src="img/thumb-2.jpg" id="small2"/>
			<img src="img/thumb-3.jpg" id="small3"/>
		</div>
		
		<script type="text/javascript">
			var slipeImg = document.getElementById("pic");
			var timer = setInterval(slipe,3000);
			var count = 1;
			slipeImg.addEventListener("mouseover",overSlipe);
			slipeImg.addEventListener("mouseout",outSlipe);
			
			var thumbs = document.querySelectorAll("#pic_small>img");
			thumbs[0].addEventListener("click",fun1);
			thumbs[1].addEventListener("click",fun2);
			thumbs[2].addEventListener("click",fun3);


			function fun1(){
				slipeImg.src="img/pic1.jpg";
			}
			function fun2(){
				slipeImg.src="img/pic2.jpg";
			}	
			function fun3(){
				slipeImg.src="img/pic3.jpg";
			}
			
			function overSlipe(){
				clearInterval(timer);
			}
			function outSlipe(){
				timer = setInterval(slipe,1000);
			}
			function slipe(){
				if (count == 3){
					count = 1
					slipeImg.src="img/pic" + count + ".jpg";
				}else{
					count += 1;
					slipeImg.src="img/pic" + count + ".jpg";
				}
			}
		</script>
	</body>
</html>

```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-73334813bdef8410.gif?imageMogr2/auto-orient/strip)
