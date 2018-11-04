---
title: jQuery
comments: true
date: 2018-09-28 23:58:56
categories: Web
tags: jQuery
---
口号：Write Less Do More
*****
1.解决了浏览器兼容性问题
2.封装了常用的操作，用更少的代码做更多的事。

##### 引入jQuery
1.使用自己项目中的jquery.min.js。
2.使用CDN服务器上的jQuery文件。

##### 如何使用jQuery
jQuery对象的本质是一个伪数组
- 有length属性
- 可以通过下标获取数据

**window.jQuery属性  --> $**

**1、$函数的参数是一个函数 - 传入的函数是页面加载完成之后要执行的回调函数**

**2、$函数的参数是选择器字符串 - 获得页面上的标签而且转换成JQuery对象。**
说明：为什么要获取jQuery对象 - 因为jQuery对象有更多封装好的方法可供调用。
- 绑定/反绑定：on()/off()/one()
- 获取/修改标签内容：text()/html()
- 获取/修改标签属性：attr(name, value)
- 添加子节点：append()后 / prepend()前面
- 删除/清空节点：remove() / empty()
- 修改样式表：css({'color':'red',……}) - 修改多个样式  （一个参数是读样式，两个是修改样式）
- 获取节点：parent() / children() / prev() /next() 
 - 后两个是兄弟节点

**3、$函数的参数是标签字符串 - 创建标签并且返回对应的jQuery对象。**

**4、$函数的参数是原生JS对象 - 将原生JS对象转换成JQuery对象。**
- 如果bar是一个jQuery对象 可以通过bar[0] / bar.get[0]

四种$使用方法例子：
```
		<script>
			$(function(){
				function deleteItem(evt){
					$(evt.target).parent().remove();
				}
				$("#fruits a").on("click",deleteItem);
				$("#ok").on("click",function(){
					var fruitName = $("#container input[name=fruit]").val().trim();
					if (fruitName.length > 0)	{
						$("#fruits").append($("<li>").text(fruitName).append($("<a>").text("x").attr("href","javascript:viod(0);").on("click",deleteItem)));
					}
				});
			});
		</script>
```
具体jQuery用法可以参考：[jQuery API 手册](http://www.runoob.com/manual/jquery/)
