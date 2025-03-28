import time

import pyautogui as ag
import pymsgbox
from cnocr import CnOcr

# 按下单个按键
# ag.press("enter")
# 按组合键
# ag.hotkey("ctrl","a")
# 鼠标点击
# ag.click(x=,y=,clicks=)
# 鼠标移动
# ag.moveTo()
# 鼠标移动相对位置
# ag.moveRel()
# 鼠标拖动
# ag.dragTo()
# ag.dragRel()
# 截图                         这的参数一定要是int整数类型
# ag.screenshot("文件名称.png",region=(x,y,width,height))
# ag.locateOnScreen() #只能找到图片文件所在位置得左上角得点
# ag.center()#找到图片中心点
# ag.locateAllOnScreen()#能够找到所有得和图片相似得地方
# ag.locateCenterOnScreen()#可以找到我们图片的中心位置
# cnocr  识别图片中得中文得工具
# 1.导入cnocr中的CnOcr
# 2.获取我们的图片地址
# ./ 找到同级得位置，然后写文件夹名称，再加上/写图片名称或者文件夹名称
# ../ 退到上一级文件夹，如果要多级返回那就多写几个就好了
# 3.创建CnOcr对象
# 4.分析图片
# 5.打印图片内容

# 1. 找到我们要获取信息的位置
# 第一张图片的左上角是197，305  宽高250*410
time.sleep(2)
loc = ag.locateOnScreen("money.png")
top = 340
# int(数据)  强制将我们括号中的数据转换成int类型
img_region_y = int(loc.top - 340)
print(type(img_region_y))
# print(loc)
img_region = [(197, img_region_y, 250, 410), (442, img_region_y, 250, 410), (695, img_region_y, 250, 410),
              (952, img_region_y, 250, 410), (1204, img_region_y, 250, 410)]
# # ag.screenshot("0.png",region=img_region[0])
# # 2. 根据我们选择的区域进行截图
# # len(数据)  它是用来求括号中的数据有多少个元素  求个数
# print(len(img_region))
for i in range(len(img_region)):
    #     # 如果图片名称相同，那么我们会覆盖原照片
    #     # print(i)
    #     # print(f"{i}") 他的输出结果是我们变量i得值
    #     # 这是一种叫做format得输出方式  在我们字符串引号之前加上f
    #     # 字符串里面用大括号{}括住我们的变量名，那么在输出的时候变量名才会被翻译成相对应得值
    ag.screenshot(f"{i}.png", region=img_region[i])
pymsgbox.alert(text="截图已经完毕")
# # 3. 使用cnocr识别截图内容
# ocr1=CnOcr()
# for i in range(len(img_region)):
#     res=ocr1.ocr(f"{i}.png")
#     for j in res:
#         print(j["text"])
#     print("**********************")
ocr1=CnOcr()
img_masg=[]
for i in range(len(img_region)):
    img_text=[]
    res = ocr1.ocr(f"{i}.png")
    # print(res)
    for j in res:
        img_text.append(j["text"])
    img_masg.append(img_text)
# input录入进来的内容统统都是字符串数据类
ac=int(input("请问你要找哪一个商品的信息"))
ac-=1
print(img_masg[ac])

