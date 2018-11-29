---
title: JS修改元素标签
comments: true
date: 2018-09-27 23:57:10
categories: Web
tags: js
---
**根据拿到元素访问其他节点**
元素访问子节点 - children
元素访问父节点 - parentNode
元素访问兄弟节点 - previousSibling / nextSibling

### JS中拿到元素的的一些操作
#### 1、修改元素样式
`var closeBtn = document.getElementById("closeBtn");`
**可以直接对closeBtn对元素样式进行操作**
`closeBtn.parentNode.style.display = "none"; //关闭父节点的显示`
区别：
`closeBtn.parentNode.style.visibility = "hidden"; //隐藏父节点，但是位置还占着`

#### 2、读取元素样式
读样式方法，通过`document.defaultView.getComputedStyle()`来读取样式。
```
var ad = document.getElementById("ad");
var currentStyle = document.defaultView.getComputedStyle(ad);
consle.log(currentStyle.width)
consle.log(currentStyle.height)
```
流氓广告-- 无法关闭，点击后广告变大
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<style type="text/css">
		*{
			margin: 0;
			padding: 0;
		}
		#ad{
			background-color:blueviolet;
			float: right;
			right: 0;
			position: fixed;
			width: 200px;
			height: 200px;
		}
		#ad button{
			float: right;	
		}
	</style>
	<body>
		
		<div id="ad">
			这里是广告
			<button id="closeBtn">关闭</button>
		</div>
		
		
		<script type="text/javascript">				
			var closeBtn = document.getElementById("closeBtn");
			closeBtn.addEventListener("click",function(){				
//				拿到元素的style属性只能进行修改,不能读取
//				closeBtn.parentNode.style.display = "none"; //点击关闭按钮关闭广告
//				closeBtn.parentNode.style.visibility = "hidden"; //隐藏div，但是位置还占着
								
//				读样式方法，通过得到的currentStyle来读取样式。
				var ad = document.getElementById("ad");
				var currentStyle = document.defaultView.getComputedStyle(ad);
				//	点击广告变大
				ad.style.width = (parseInt(currentStyle.width) + 20) + "px";
				ad.style.height = (parseInt(currentStyle.height) + 20) + "px";
			});
		
		</script>
	</body>
</html>
```

#### 3、删除
**必须父元素操作，才能删除子元素**
`ul.removeChild(li);  //删除子标签li`
 
#### 4、添加
**必须是父元素才能对子元素进行添加操作**
```
var div = document.createElement("div"); // 创建元素,然后对创建的元素进行操作
divFather.appendChild(div);    //添加子标签(加在最后)
divFather.insertBefore(div,位置);   //添加子标签（指定位置）
```

练习
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			*{
				margin: 0;
				padding: 0;
			}
			#main{
				width: 800px;
				height: 400px;
				margin: 10px auto;
				border:black solid;
				overflow: hidden;
			}
			#button1{
				width: 50px;
				height: 30px;
				font-size: 18px;
				margin-left: 300px;
			}
			#button2{
				width: 50px;
				height: 30px;
				font-size: 18px;
				margin-left:500px;
			}
			#main div{
				width: 80px;
				height:80px;
				float:left;
			}
			
		</style>
	</head>
	<body>
		<div>
			<div id="main"></div>
			<button id="button1">添加</button>
			<button id="button2">闪烁</button>
		</div>
		
		
		<script type="text/javascript">
			var main = document.getElementById("main");
			var button1 = document.getElementById("button1");
			var button2 = document.getElementById("button2");
			var flag = true;
			var glint1 = 0;
			button1.addEventListener("click",function(){
				var div1 = document.createElement("div");
				div1.style.backgroundColor = randomColor();
				main.insertBefore(div1,main.firstChild);					
			})
			
			button2.addEventListener("click",function(){
				if (flag){
					glint1 = setInterval(glint,200);			
				}else{
					clearInterval(glint1);
				}
				button2.innerHTML = flag?"暂停":"闪烁";
				flag = !flag;
			});
			
			
			function glint(){
						var divAll = document.querySelectorAll("#main div");
						for (var i = 0; i<divAll.length; i+=1){
							divAll[i].style.backgroundColor = randomColor();
						};
					}
			
			function randomColor(){
				var red = parseInt(Math.random()*256);
				var green = parseInt(Math.random()*256);
				var blue = parseInt(Math.random()*256);
				return "rgb(" + red + ", " + green + ", " + blue + ")";
			}
		</script>
	</body>
</html>

```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-2b40b5307ea1def2.gif?imageMogr2/auto-orient/strip)


----
**练习**
1、鼠标按住拖动效果
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			#div1{
				width: 100px;
				height: 100px;
				background-color: #5F9EA0;
				position: absolute;
				left: 0px;
				top: 0px;
			}
		</style>
	</head>
	<body>
		<div id="div1"></div>
		
		<script type="text/javascript">
			var div1 = document.getElementById("div1");
			var originalX = 0;
			var originalY = 0;
			var flag = false;
			
			div1.addEventListener("mousedown",function(evt){
				originalX = evt.clientX - div1.offsetLeft;   //记录事件发生的鼠标到left的距离
				originalY = evt.clientY - div1.offsetTop;
				flag = true;
			});
			
			
			div1.addEventListener("mousemove",function(evt){
				if (flag){
					div1.style.left = (evt.clientX - originalX)+"px";
					div1.style.top = (evt.clientY - originalY)+"px";	
				}
			});
			
			
			div1.addEventListener("mouseup",function(evt){
				flag = false;
			});
		</script>
	</body>
</html>

```
效果：
![](https://upload-images.jianshu.io/upload_images/13692175-dd84fe2eeccd1c48.gif?imageMogr2/auto-orient/strip)



