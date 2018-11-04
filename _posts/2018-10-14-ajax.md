---
title: ajax
comments: true
date: 2018-09-29 00:00:01
categories: Web
tags: ajax
---
ajax = Asynchronous + JavaScript + And +  XML（现在XML慢慢已经被JSON取代）

Asynchronous：异步请求（没有中断浏览器的用户体验）从服务器获取数据。
JSON ： 通过DOM操作对页面进行局部刷新

ajax作用：异步加载数据 + 局部刷新页面

效果一：利用api查看美女图片
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<button id="beauty">换一组</button><br/>
		<script src="https://cdn.bootcss.com/jquery/1.12.2/jquery.min.js"></script>
		<script type="text/javascript">
			$(function(){
				$("#beauty").on("click",function(){
					$("a").empty();
					var url = "http://api.tianapi.com/meinv/?key=3cedb24a8f5af4277b3de0b9c841e1d6&num=20"
					$.getJSON(url,function(jsonOBJ){
						for (var i = 0; i < jsonOBJ.newslist.length ; i += 1){
							$(document.body).append(
								$("<a>").html(jsonOBJ.newslist[i].title+"<br/>").attr("href",jsonOBJ.newslist[i].picUrl).attr("width","400")
	
							);
						}
					});
				});
			});
		</script>
	</body>
</html>

```
效果二：api-周公解梦
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>周公解梦在线版</title>
		<style type="text/css">
			#main{
				position: absolute;
				margin: 100px 200px;
				float: left;
				width: 800px;
				height: 400px;
				border: solid black;
			}

		</style>
	</head>
	<body>
		<div id="main">
			<span>解梦：</span>
			<input placeholder="输入您想查询梦的关键字" id="text">
			<button id="confirm">查询</button>
			<hr />
			<span>解析：</span>
			
		</div>
		<script type="text/javascript" src="https://cdn.bootcss.com/jquery/1.12.2/jquery.min.js"></script>
		<script>
			$(function(){
				$("#confirm").on("click",function(){
					var content = $("#text").val().trim();
					if (content.length>0){
						
						//getJSON方法
//						var str1 = encodeURIComponent(content,"utf-8");
//						var url = "http://api.tianapi.com/txapi/dream/?key=3cedb24a8f5af4277b3de0b9c841e1d6&word=" + str1;
//						$.getJSON(url,function(jsonOBJ){
//							$("#main>p").empty();
//							if (jsonOBJ.code == 250){
//								alert("未检索到相关信息！")；
//							}else{	
//								$("#main").append($("<p>").text(jsonOBJ.newslist[0].result))；
//							}
//						});

						//ajax方法
						$.ajax({
							"url":"http://api.tianapi.com/txapi/dream/",
							"type":"get",
							"data":{
								"key":"3cedb24a8f5af4277b3de0b9c841e1d6",
								"word":content
							},
							"dataType": "json",
							"success": function(jsonOBJ){
								if (jsonOBJ.code == 250) {
									alert("未检索到相关信息！");
								}else{
									$("#main").append($("<p>").text(jsonOBJ.newslist[0].result));
								}
							}
					
						});
					}
					

				});
			});
		</script>
	</body>
</html>

```

Bootstrap响应式布局
[Bootstrap](http://www.bootcss.com/)