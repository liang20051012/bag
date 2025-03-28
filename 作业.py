import random
import string
import time
from typing import Tuple
import pyautogui
import pymsgbox
import pyperclip
from cnocr import CnOcr
from pyautogui import locateOnScreen

# 1.输出字符串“Hello Python!”
# str="Hello Python!"
# print(str)
# 2. 遍历[1,2,3,4,5,6]列表
# list1=[1,2,3,4,5,6]
# for i in list1:
#     print(i)
# 3.遍历{"name":"张三","age":18}字典
# dist1={"name":"张三","age":18}
# for k in dist1 :
#     print(i)
#     print(dist1[k])
# 4.每输出三遍"你好世界",在输出一行"*",重复输出三次
# i=0
# k=0
# while i<3 :
#     while k<3 :
#         print("你好世界")
#         k+=1
#     print("*")
#     k=0
#     i+=1
# 输出九九乘法表
# while方法
# i=1
# while i<=9:
#     j=1
#     while j<=9:
#         if(i>=j):
#             print(i,"*",j,"=",i*j,end="  ")
#         j+=1
#     i+=1
#     print()
# for方法
# for j in [1,2,3,4,5,6,7,8,9]:
#     for i in range(1,j+1):
#         print(i, "*", j, "=", i * j, end="  ")
#     print()
# 类金山打字通小游戏
# def show_menu():
#     print("请输入想要的功能")
#     print("1.开始游戏")
#     print("2.退出游戏")
# def random_str():
#     len=10
#     str_list=string.ascii_letters
#     random_str=""
#     random_list=random.sample(str_list,len)
#     rand_str=random_str.join(random_list)
#     return rand_str
# show_menu()
# ac=input()
# if ac=="1":
#     rand_str1=random_str()
#     print(rand_str1)
#     began_time=time.time()
#     in_str=input("输入相同的字符串")
#     end_time=time.time()
#     use_time=end_time-began_time
#     avg_time=use_time/10
#     if in_str==rand_str1:
#         print("输入正确")
#         print("所花时间为",use_time,"平均每个字母花费时间",avg_time)
#     else:
#         print("输入错误")
# elif ac=="2":
#     print("退出了")
# else:
#     print("输入错误")
# continue循环实验
# i=1
# while i<10:
#     i+=1
#     if i%2==0:
#         continue
#     print(f"{i}是奇数")
# 1.定义一个无参函数 函数内部定义 元组 a=(1,2,3,4,5) 使用下标获取元组第一个值打印 并调用函数名
# def yuan():
#     list1 = (1, 2, 3, 4, 5)
#     print(list1[0])
# yuan()
# 2.使用range()中的步长 输出0~10以内的偶数
# for i in range(0,10,2):
#     print(i)
# 3.使用try,except 异常函数 在try里打印1/0 报出异常在except里打印 0不能当被除数
# try:
#     print(1/0)
# except:
#     print("被除数不能为0")
# 判断b是否为素数
# b=int(input())
# a=b//2
# while a>1:
#     if b%a==0:
#         print("%d不是素数"%(b))
#         break
#     a=a-1
# else:
#     print("%d是素数"%(b))
# 画一个正方形螺旋线
# distance=200
# while distance>0:
#         pyautogui.drag(distance,0,duration=0.5)
#         distance-=5
#         pyautogui.drag(0, distance, duration=0.5)
#         pyautogui.drag(-distance, 0, duration=0.5)
#         distance -= 5
#         pyautogui.drag(0, -distance, duration=0.5)
# 获取鼠标当前位置
# input()
# res=pyautogui.position()
# # print(res)
# 1.编写一个鼠标连续移动的循环，模拟幽灵鼠标效果
# x=2244
# y=622
# for i in range(10):
#     pyautogui.moveTo(x, y)
#     x+=100
#     y+=100
#     time.sleep(2)
# 2.实现鼠标点击功能，点击指定位置
# while True:
#     x=int(input("输入X坐标"))# 要用int()转为整数类型 ，  input 默认是str字符类型
#     y=int(input("输入Y坐标"))
#     pyautogui.click(x=x,y=y,clicks=2)
# 3。实现鼠标滚动功能，向下滚动800像素
# time.sleep(2)
# pyautogui.scroll(-800)
# 4使用键盘控制相关函数，实现文本输入和复制粘贴功能
# while True:
#     text=input("输入文本")
#     pyperclip.copy(text)
#     pyautogui.hotkey("ctrl","v")
#     print()
# 1.写一个“人生模拟器”。选项有“财富”，“健康”，“快乐”，“我全都要”
# pymsgbox.confirm(text="人生模拟器",buttons=["财富","健康","快乐","我全都要"])
# 2.猜字小游戏
# a=random.randint(0,10)
# while True:
#     res=int(pymsgbox.prompt(text="来个数字"))
#     if res==a :
#          print("对")
#          break
#     elif res>a :
#         print ("大了")
#     elif res<a  :
#         print("小了")
#     else :
#         print("快点输")
# 3。输入 查找信息 自动打开浏览器
# res=pymsgbox.prompt(text="输入想要搜索的东西")
# list1=pyautogui.locateCenterOnScreen("liulanqi.png",confidence=0.9)
# pyautogui.click(x=list1.x,y=list1.y,clicks=2)
# time.sleep(2)
# pyperclip.copy(res)
# pyautogui.hotkey("ctrl","v")
# pyautogui.press("enter")
# 截图功能+识别文本
# x=0
# y=0
# w=0
# h=0
# for i in range(4):
#     print(f"来输第{i+1}个点")
#     time.sleep(3)
#     dian=pyautogui.position() #获取点坐标
#     print(dian)
#     if i==0:
#         x=dian.x
#         y=dian.y
#     if i==2:
#         w=dian.x-x
#         h=dian.y-y
# res=(x,y,w,h)
# pyautogui.screenshot("text.png",region=res)
# img="text.png"
# ocr1=CnOcr()
# date=ocr1.ocr(img)
# for i in date:
#     print(i["text"])
# 指定收集淘宝商品数据
# time.sleep(2)
# loc = pyautogui.locateOnScreen("money.png")
# #print(loc)
# top=680
# w=470
# chang=810
# kuan=494
# img_region_y = int(loc.top - 680)
# img_region_x=int(loc.left)
# img_region = [(img_region_x,img_region_y,kuan,chang), (img_region_x+w, img_region_y,kuan, chang), (img_region_x+w*2, img_region_y,kuan,chang),
#               (img_region_x+w*3+80, img_region_y,kuan, chang), (img_region_x+w*4+150, img_region_y-50,kuan,chang)]
# for i in range(len(img_region)):
#     pyautogui.screenshot(f"{i}.png", region=img_region[i])
# pymsgbox.alert(text="截图已经完毕")
# ocr1=CnOcr()
# img_masg=[]
# for i in range(len(img_region)):
#     img_text=[]
#     res = ocr1.ocr(f"{i}.png")
#     # print(res)
#     for j in res:
#         img_text.append(j["text"])
#     img_masg.append(img_text)
# ac=int(input("请问你要找哪一个商品的信息"))
# print(img_masg[ac-1])
import requests
# 1使用requests.get 请求  http://httpbin.org/get
# def one():
#     url="http://httpbin.org/get"
#     response=requests.get(url)
#     print(response)
# one()
# 2使用requests下载图片(百度Logo)
# def two():
#     url="https://search-operate.cdn.bcebos.com/7e85570b817e17e8f3ae93134cc78451.gif"
#     res=requests.get(url)
#     with open("baidu.gif","wb")as f:
#         f.write(res.content)
#     print("保存成功")
# two()

# from PIL import Image, ImageSequence
# def play_gif(file_path):
#     gif = Image.open(file_path)
#     for frame in ImageSequence.Iterator(gif):
#         frame.show()
#         time.sleep(0.1)  # 控制帧之间的间隔时间
# if __name__ == "__main__":
#     play_gif("baidu.gif")
# import pygame
# from pygame.locals import *
# def play_gif(file_path):
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
#     clock = pygame.time.Clock()
#     gif = pygame.image.load(file_path)
#     gif_rect = gif.get_rect()
#     frames = []
#     for i in range(gif.get_width() // gif_rect.width):
#         frame = gif.subsurface((i * gif_rect.width, 0, gif_rect.width, gif_rect.height))
#         frames.append(frame)
#     index = 0
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 return
#         screen.fill((0, 0, 0))
#         screen.blit(frames[index], (100, 100))
#         pygame.display.flip()
#         index = (index + 1) % len(frames)
#         clock.tick(10)  # 控制帧之间的间隔时间
# if __name__ == "__main__":
#     play_gif("baidu.gif")
#     pygame.init()
#     screen = pygame.display.set_mode((800, 800))
#     clock = pygame.time.Clock()
#     gif_image = pygame.image.load('baidu.gif')
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         screen.blit(gif_image, (0, 0))
#         pygame.display.flip()
#         clock.tick(30)  # 控制帧率
# pygame.quit()
# from PIL import Image
# import matplotlib.pyplot as plt
# # 打开GIF文件
# gif_image = Image.open('baidu.gif')
# # 显示GIF
# plt.imshow(gif_image)
# plt.axis('off')  # 不显示坐标轴
# plt.show()
# 显示gif
# import tkinter as tk
# from PIL import Image, ImageTk, ImageSequence
# class GIFPlayer(tk.Label):
#     def __init__(self, master, gif_path):
#         im = Image.open(gif_path)
#         self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(im)]
#         super().__init__(master, image=self.frames[0])
#         self.index = 0
#         self.delay = 100  # 控制帧之间的间隔时间（毫秒）
#         self.after(self.delay, self.play)
#     def play(self):
#         self.index = (self.index + 1) % len(self.frames)
#         self.config(image=self.frames[self.index])
#         self.after(self.delay, self.play)
# if __name__ == "__main__":
#     root = tk.Tk()
#     player = GIFPlayer(root, "baidu.gif")
#     player.pack()
#     root.mainloop()
# 3使用requests 调用 天气API  获取城市等相关数据
# def three():
#     appid="48561619"
#     appsecret="oLMJK3Qq"
#     city=input("输入城市\n")
#     url=f"http://gfeljm.tianqiapi.com/api?unescape=1&version=v61&appid={appid}&appsecret={appsecret}"
#     #url= "http://gfeljm.tianqiapi.com/api?unescape=1&version=v61&appid=48561619&appsecret=oLMJK3Qq"
#     str1=url+f"&city={city}"
#     res=requests.get(str1)
#     dict1=res.json()    #转换为字典
#     print(dict1["wea"])
# three()
#青云客API         http://api.qingyunke.com/
# 同一级目录：<img src="photo.jpg">
# 下一级目录：<img src="images/photo.jpg">
# 上一级目录：<img src="../photo.jpg">
#2使用 BS4 获取   https://www.thepaper.cn/newsDetail_forward_26649723  文章内容

