---
title: pygame
date: 2018-09-04 19:06:52
comments: true
categories: Python
tags: pygame
---
**安装：pip install Pygame**

#### 1、初始化游戏模块
```
pygame.init()
```
#### 2、创建游戏窗口

set_mode((100, 200)) : 单位像素
```
window = pygame.display.set_mode((400, 600)）
#窗口大小：元组，元组中的两个值表示宽度和高度
```
程序结束窗口会自动关闭，所以需要循环或者其他方式让窗口手动关闭。
#### 3、给窗口填充颜色

颜色：计算机三原色（红、绿、蓝），每个颜色对应的值范围是0-255.可以改变三原色的值可以调配出不同的颜色。
颜色值：是一个元组，有三个元素，分别代表红绿蓝（rgb）。
(255, 0 ,0) --> 红色
(0, 0, 0) --> 黑色
(255, 255 , 255) --> 白色
```
window.fill((255, 255, 255))
```
#### 4、让游戏一直运行，直到点关闭按钮才结束
```
while True:
    #获取游戏过程中产生的所有事件
    for event in pygame.event.get():
        # type判断事件的类型（QUIT：点击×）
        if event.type == pygame.QUIT:
            exit() #退出程序
```
**a、事件的type --- 决定发生的是什么事件**

QUIT ： 关闭按钮被点击事件
        
鼠标事件:
MOUSEBUTTONDOWN: 鼠标按下事件
MOUSEBUTTONUP: 鼠标按下松开时对应的事件
MOUSEMOTION：鼠标移动事件
        
键盘事件:
KEYDOWN： 键盘按下
KEYUP:  键盘弹起
        
**b.事件的pos(event.pos) --- 鼠标事件发生的位置(坐标)**
        
**c.事件的key(event.key) --- 键盘事件被按的键对应的编码值**

应用：
```
for event in pygame.event.get():
    # 不同的事件发生后，对应type值不一样
    if event.type == pygame.QUIT:
        print('点击关闭按钮')
        exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # 鼠标按下要做的事情就写在这儿
        print(event.pos)
        print('鼠标按下')
        # 鼠标按下一次画一个球
        # pygame.draw.circle(window, (randint(0, 255), randint(0, 255),\
        #                             randint(0,255)), event.pos, randint(20, 50))
        # pygame.display.flip()

    elif event.type == pygame.MOUSEBUTTONUP:
        print('鼠标弹起', event.pos)
    elif event.type == pygame.MOUSEMOTION:
        # 鼠标按下一次画一个球
        pygame.draw.circle(window, (randint(0, 255), randint(0, 255), \
                                    randint(0, 255)), event.pos, 20)
        pygame.display.flip()
        # print('鼠标正在移动', event.pos)
        pass
    elif event.type == pygame.KEYDOWN:
        print('键盘按下', event.key, chr(event.key))
    elif event.type == pygame.KEYUP:
        print('键盘弹起')
```

#### 5、图片相关
获取本地的一张图片，返回图片对象
image.load(路径) 
**（1）获取图片，创建图片对象**
```
image = pygame.image.load('./files/luffy4.jpg')
```
**获取图片的宽和高**
```
image.get_size() ： 获取屏幕宽和高，返回一个元组（宽、高）
```
**形变：**
a、缩放
`transform.scale(缩放对象，目标大小)`
将制定的对象缩放到指定的大小，会返回缩放后的对象。
```
new_image = pygame.transform.scale(image,(100,100))
```
b、旋转缩放（指定缩放比例）
`transform.rotozoom(Surface, angle, scale)`
Surface:旋转缩放对象
angle：旋转角度( 0~360)
scale：缩放比例（初始为1）
c、旋转
`transform.rotate(Surface, angle)`
Surface：旋转对象
angle：旋转角度（0~360）
**（2）渲染图片（将图片画在纸上）**
```
window.blit(渲染对象， 位置)
```
位置：坐标（x，y）
```
window = blit(image, (0,0))
```
坐标计算如下图：
![](https://upload-images.jianshu.io/upload_images/13692175-634fb6606cff822e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###### （3）展示内容(将纸展示)

一般第一次用这个方法
```
pygame.display.flip()
```
一定范围刷新
```
pygame.display.update()
```
#### 6、文字相关
###### （1）、字体对象

a、系统字体（一般不支持中文）
`font = pygame.font.SysFont('Times', 30)`
SysFont(name, size, bold=False, italic=False)
bold : 是否加粗
italic：是否倾斜
b、自定义字体对象（支持 ttf 文件）
Font(字体文件路径，字体大小)
font = pygame.font.Font('./file/aa.ttf', 30)

###### （2）、根据字体去创建文字对象
render(text, antialias, color，background=None)
text : 需要显示的文字（字符串）
antialias：是否平滑（布尔）
color：（颜色）
background：背景颜色
```
text = font.render('hello', True, (0, 0, 255))
```
（3）、渲染文字
window.blit(text, (50,50))
（4）、展示内容
pygame.display.flip()

#### 7、图形相关
##### （1）、直线
###### a、线段
`pygame.draw.line(Surface, color, start_pos, end_pos, width=1)`
Surface：画在哪儿
color：线的颜色
start_pos：起点
end_pos：终点
width：宽度
```
#水平线
pygame.draw.line(window, (255, 0, 0), (50, 100), (200, 100))
```
###### b、多条线段（折线）
lines(Surface, color, closed, pointlist, blend=1)
colsed：是否闭合
```
pygame.draw.lines(window, (0, 255, 0), False, [(100,200), (150,120), (140,150)])
```
###### c、圆
`pygame.draw.circle(Surface,color,pos,radius,width=0)`
Surface:圆心半径
color:颜色
pos:位置
radius:半径
width:线段，0->填充
```
pygame.draw.circle(window,(255,255,0),(250,275),100,0)
```
###### d、矩形
`pygame.draw.rect(Surface,color,Rect,width=0)`
Surface:画在哪儿
color:颜色
Rect:范围(元组，元组中有四个元素，分别是x,y,width,height)
width:线宽，0->填充
```
pygame.draw.rect(window,(255,0,0),(0,0,50,100))

```
###### e、多边形
```
pygame.draw.polygon(Surface,color,pointlist,width=0)
```
###### f、椭圆
```
pygame.draw.ellipse(Surface.color,Rect,width=0)
#内切矩形原理
```
###### g、弧线
```
pygame.draw.arc(Surface,color,Rect,start_angle,end_angle,width=1)
#start_angle: 0-2pi
#stop_angle:
#pi --- 180°   1° --- pi/180
#59° = pi/180 * 59
```
##### （2）、展示
`pygame.display.flip()`

#### 8、一些游戏效果原理
##### （1）、动画原理
```
import pygame

if __name__ == '__main__':
    # 初始化
    pygame.init()
    window = pygame.display.set_mode((400, 600))
    window.fill((255, 255, 255))
    pygame.display.flip()

    # 球的圆心坐标
    x = 100
    y = 100
    r = 50
    add = 4
    y_speed = 2
    # 游戏循环
    while True:

        # 延迟
        # pygame.time.delay(10)

        # 将之前纸上的内容给覆盖
        window.fill((255, 255, 255))
        # 不断的画圆
        pygame.draw.circle(window, (255, 0, 0), (x, y), r)
        pygame.display.update()

        # 改变y值让圆在垂直方向移动
        y += y_speed
        # r += add
        # if r >= 120 or r <= 20:
        #     add *= -1
        # 边界检测
        if y > 600 - r:
            y = 600 - r
            y_speed = -2
        elif y < 50:
            y = 50
            y_speed = 2

        # 事件检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
```
设置延迟：毫秒
`pygame.time.delay（毫秒）`
##### （2）、按住不放原理
```
import pygame

if __name__ == '__main__':
    # 游戏初始化
    pygame.init()
    window = pygame.display.set_mode((400, 600))
    window.fill((255, 255, 255))
    # pygame.display.flip()

    # 1.显示一张图片
    image = pygame.image.load('./files/luffy4.jpg')
    # 缩放
    image = pygame.transform.rotozoom(image, 0, 0.5)
    window.blit(image, (100, 100))
    # 获取图片的宽度和高度
    image_w, image_h = image.get_size()

    pygame.display.flip()

    # 用来存储图片是否移动
    flag = False

    # 保存图片的坐标
    image_x, image_y = 100, 100

    # 游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # 鼠标按下
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 判断按下的位置是否在图片上
                m_x, m_y = event.pos
                if image_x<=m_x<=image_x+image_w and image_y<=m_y<=image_y+image_h:
                    flag = True
            elif event.type == pygame.MOUSEBUTTONUP:
                flag = False
            # 鼠标移动事件
            # (鼠标在移动并且flag是True)
            if event.type == pygame.MOUSEMOTION and flag:
                # 填充背景色,覆盖原来的内容
                window.fill((255, 255, 255))
                # 在鼠标移动的位置渲染图片
                # window.blit(image, event.pos)
                center_x, center_y = event.pos
                image_x, image_y = center_x - image_w/2, center_y-image_h/2
                window.blit(image, (image_x, image_y))
                # 更新屏幕的显示
                pygame.display.update()
```

##pygame小游戏


##### 1、小球碰撞
```
"""__author__=星辰"""
import pygame
import random
from time import sleep
if __name__=='__main__':
    pygame.init()
    window = pygame.display.set_mode((800,600))
    window.fill((255,255,255))
    pygame.display.flip()
    list_balls=[]
    while True:

        if list_balls:
            for ball in list_balls:
                x,y=ball['pos']
                r=ball['re']
                index=list_balls.index(ball)
                if index<len(list_balls)-1:
                    while index+1<len(list_balls):
                        ball2=list_balls[index+1]
                        x2,y2=ball2['pos']
                        if (x2-x)**2+(y2-y)**2<=(2*r)**2:
                            if x>=x2:
                                ball['xs']=1
                                ball2['xs']=-1
                            if x<=x2:
                                ball['xs'] = -1
                                ball2['xs'] = 1

                            if y>=y2:
                                ball['ys']=-1
                                ball2['ys']=1
                            if y<=y2:
                                ball['ys']=1
                                ball2['ys']=-1
                        index +=1

                if x+r>=800:
                    xs = -1
                    ball['xs']=xs
                if x-r<=0:
                    xs = 1
                    ball['xs'] = xs
                if y+r>=600:
                    ys = -1
                    ball['ys']=ys
                if y-r<=0:
                    ys=1
                    ball['ys'] = ys
                x += ball['xs']
                y += ball['ys']
                ball['pos']=(x,y)
                pygame.draw.circle(window,ball['rgb'],(x,y),ball['re'],ball['width'])
            sleep(0.01)
            pygame.display.flip()

            window.fill((255,255,255))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                dic_ball = {}
                dic_ball['rgb']=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                dic_ball['pos']=event.pos
                dic_ball['re']=20
                dic_ball['width']=0
                dic_ball['xs']=[-1,1][random.randint(0,1)]
                dic_ball['ys']=[-1,1][random.randint(0,1)]
                # pygame.draw.circle(window,dic_ball['rgb'],dic_ball['pos'],dic_ball['re'],dic_ball['width'])
                list_balls.append(dic_ball)
                pygame.display.flip()
                sleep(0.01)
                window.fill((255,255,255))
```
##### 2、接球游戏
```
import pygame
import random
from time import sleep
if __name__=='__main__':
    pygame.init()
    mx = 0
    my = 300
    m_width=100
    m_height=10
    window = pygame.display.set_mode((600,400))
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(mx,my,m_width,m_height),0)
    pygame.display.flip()



    xs=1
    ys=1
    x=random.randint(0,600)
    y=random.randint(0,400)


    while True:
        pygame.draw.circle(window, (255, 0, 0), (x, y), 20, 0)
        pygame.draw.rect(window, (255, 0, 0), (mx, my, m_width, m_height), 0)
        pygame.display.update()  # 可以刷新指定的范围
        x +=xs
        y +=ys
        window.fill((255,255,255))
        if mx<=(x+20)<=mx+m_width and y+20>=300 :
            if xs>0:
                xs = 1
            else:
                xs = -1
            ys = -1
        elif x+20==600 :
            xs = -1
        if (x-20)==0:
            xs = 1
        if (y-20)==0:
            ys = 1
        if (y+20)>320:
            exit(0)


        sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEMOTION:
                mx,my=event.pos
                mx=mx-m_width/2
                my=300

```
##### 3、大球吃小球
```
import pygame
import random
from time import sleep
if __name__=='__main__':
    pygame.init()
    window = pygame.display.set_mode((800,600))
    window.fill((255,255,255))
    pygame.display.flip()
    list_balls=[]
    while True:

        if list_balls:
            for ball in list_balls:
                x,y=ball['pos']
                r1=ball['re']
                if r1>=150:
                    ball['re']=10
                    r1=10
                index=list_balls.index(ball)
                if index<len(list_balls)-1:
                    while index+1<len(list_balls):
                        ball2=list_balls[index+1]
                        r2 = ball2['re']
                        x2,y2=ball2['pos']
                        if (x2-x)**2+(y2-y)**2<=(r1+r2)**2:
                            if r1>r2:
                                ball['re']=int(r1+r2/2)
                                list_balls.remove(ball2)
                            if r1<=r2:
                                ball2['re'] =int(r2 + r1 / 2)
                                list_balls.remove(ball)
                        index +=1

                if x+r1>=800:
                    xs = -1
                    ball['xs']=xs
                if x-r1<=0:
                    xs = 1
                    ball['xs'] = xs
                if y+r1>=600:
                    ys = -1
                    ball['ys']=ys
                if y-r1<=0:
                    ys=1
                    ball['ys'] = ys
                x += ball['xs']
                y += ball['ys']
                ball['pos']=(x,y)
                pygame.draw.circle(window,ball['rgb'],(x,y),ball['re'],ball['width'])
            sleep(0.001)
            pygame.display.flip()

            window.fill((255,255,255))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                dic_ball = {}
                dic_ball['rgb']=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                dic_ball['pos']=event.pos
                dic_ball['re']=random.randint(10,30)
                dic_ball['width']=0
                dic_ball['xs']=[-1,1][random.randint(0,1)]
                dic_ball['ys']=[-1,1][random.randint(0,1)]
                # pygame.draw.circle(window,dic_ball['rgb'],dic_ball['pos'],dic_ball['re'],dic_ball['width'])
                list_balls.append(dic_ball)
                pygame.display.flip()
                sleep(0.01)
                window.fill((255,255,255))

```