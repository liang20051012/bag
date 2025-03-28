import pyautogui
import pyperclip
import time
from cnocr import CnOcr
import random

# 微信信息识别与回复
# 思路
# 1、根据微信图片去打开微信
# 2、检测是否有新消息
# 3、将消息区域截图
# 4、识别截图的信息
# 5、根据识别的信息回复对方

friend = ['你好','哈哈']  # 朋友发过来的信息
me = ['我很好','嘿嘿']    # 我回复的信息
elsemsg = ['对对对','没毛病','在下佩服','甘拜下风','哎呦不错哦']
# print(len(elsemsg) - 1)
# for i in range(10):
#     index = random.randint(0,len(elsemsg) - 1)  # 包左包右
#     print(index)
#     print(elsemsg[index])


# 1、根据微信图片去打开微信
loc = pyautogui.locateCenterOnScreen('VX.png',confidence=0.95)
pyautogui.doubleClick(loc)
time.sleep(1)
# 2、检测是否有新消息  等待新消息  1、程序运行太快了，还没打开微信就定位     2、加上confidence匹配度
while True:
    try:
        new_loc = pyautogui.locateCenterOnScreen('new.png',confidence=0.95)
        print(new_loc)
        pyautogui.doubleClick(new_loc)
        print('有新消息来啦')
        loc_value = (new_loc.x + 150,new_loc.y)
        pyautogui.click(loc_value,duration=1)
        # 3、将消息区域截图
        wenzi_loc = pyautogui.locateOnScreen('gjl.png',confidence=0.95)
        # print(wenzi_loc)  # 聊天文字区域下面的工具栏坐标
        # 根据工具栏的坐标，计算出消息区域的坐标
        reg = (int(wenzi_loc.left),int(wenzi_loc.top) - 60,260,45)
        pyautogui.screenshot('msg.png',region=reg)
        # 4、识别截图的信息
        ocr = CnOcr()
        res = ocr.ocr('msg.png')
        msg = res[-1]['text']  # 取出识别结果中最后一个数据中text键对应的值
        # 5、根据识别的信息回复对方
        if msg in friend:
            print('朋友发过来的信息：',msg)
            index = friend.index(msg)  # 获取元素在列表中的索引
            print('我回复过去的信息：',me[index])
            pyperclip.copy(me[index])
            pyautogui.hotkey('ctrl','v')
            pyautogui.press('enter')
        else:
            print('朋友发过来的信息：', msg)
            index = random.randint(0, len(elsemsg) - 1)
            print('随机回复信息：',elsemsg[index])
            pyperclip.copy(elsemsg[index])
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        pyautogui.click(loc_value[0],loc_value[1] + 50,duration=1)
    except:
        print('目前没有新消息')
    time.sleep(5)