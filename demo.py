import pyautogui as ag
import pymsgbox as mb
# 这里的as 相当于取名字  我们加上as之后 就不能用pyautogui来点出方法了 得用as 后面的名字点出方法
# pyautogui.ralet(text="警告内容",title="警告")  #依赖于 pymsgbox这个库
# pymsgbox.alert(text="",title="")
# mb.alert(text="警告内容",title="警告")
# 选择框
# mb.confirm(text="",title="",buttons=["111","222","333"])
# 输入框
# mb.prompt(text="",title="")
# 密码框
# mb.password(mask="@")
# 截图用的是
# ag.screenshot(x=,y=,region=)

# ocr 识别
# import cnocr   # 这样导包是将包里面的所有内容导入到我们的程序
from cnocr import CnOcr  #只从cnocr这个库中导入CnOcr这一个方法
# 现阶段我们要用的cnocr这个包中的方法只有一个   CnOcr
# CnOcr  实际上就是面向对象的一个方法 它使用实例化我们的一个cnocr对象
# img="./img/ocr_1.png"  # 拿图片地址
# ocr1=CnOcr()  # 创建识别图片信息的人
# res = ocr1.ocr(img) # 指挥ocr1这个人去识别图片  图片地址写在我们的括号中 他会得到一个结果
# # print(res)
# # print(res[0]["text"])
# for i in res:
#     print(i["text"])

# cnocr 使用步骤
# 1.导包 这里只要导入CnOcr 所以只要写from cnocr import CnOcr
# 2.找到图片地址
# 3.创建识别图片的人（实例化cnocr对象）
# 4.对象调用ocr方法进行图片识别
# 5.通过for循环或者while循环输出我们识别到的信息


#
# # 1.导包 这里只要导入CnOcr 所以只要写from cnocr import CnOcr
# from cnocr import CnOcr
# # 2.找到图片地址
# img="./img/ocr_2.png"
# # 3.创建识别图片的人（实例化CnOcr对象）
# ocr2=CnOcr(det_model_name="naive_det")
# # ocr2=CnOcr()
# # 4.对象调用ocr方法进行图片识别
# res=ocr2.ocr(img)
# # 5.通过for循环或者while循环输出我们识别到的信息
# for i in res:
#     print(i["text"])

# from cnocr import CnOcr
#
# img_fp = './img/ocr_3.png'
# ocr = CnOcr(rec_model_name='ch_PP-OCRv3') #rec_model_name识别模型名称
# res = ocr.ocr(img_fp)
# for i in res:
#     print(i["text"])


# 识别英文
# from cnocr import CnOcr
#
# img_fp = './img/ocr_4.png'
# ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
# res = ocr.ocr(img_fp)
# for i in res:
#     print(i["text"])

# import pyperclip
# # copy paste
# # text="你好"
# # pyperclip.copy(text)
# res=pyperclip.paste() # 获得剪贴板中第一条数据，如果剪贴板中有数据则可以直接获取第一条信息
# print(res)

#   截图功能 +  识别文本信息
import pyautogui as ag
from cnocr import CnOcr
import time


# 1.得到截图
#截图有四个参数，左上角x，y 和 图片 的 宽和高
x=0
y=0
width=0
height=0
# 先找到截图区域的左上角点
for i in range(4):
    print(f"请把鼠标放到第{i+1}个点")
    time.sleep(3)
    loc=ag.position()
    print(loc)
    # 有了四个点之后我们要存储我们左上角的点坐标以及我们截图的宽高
    if i == 0: # 获得左上角的起始位置
        x=loc.x
        y=loc.y
    if i == 2:# 因为右下角的点是第三次获取的 所以 条件为 i==2
        width=loc.x-x
        height=loc.y-y
reg=(x,y,width,height) # 一个截图的基本坐标
# 进行图片截取
ag.screenshot("test.png",region=reg)
# 2.图片识别
img='test.png'
ocr1=CnOcr()
data=ocr1.ocr(img)
for i in data:
    print(i["text"])

