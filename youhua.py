import pyautogui
import pyperclip
import time
from cnocr import CnOcr
import random


friend = ['你好','哈哈']  # 朋友发过来的信息
me = ['我很好','嘿嘿']    # 我回复的信息
elsemsg = ['对对对','没毛病','在下佩服','甘拜下风','哎呦不错哦']

# 复制信息并发送给朋友
def copy_send(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

# 检查是否有新消息
def get_news():
    new_loc = pyautogui.locateCenterOnScreen('new.png', confidence=0.95)
    pyautogui.doubleClick(new_loc)
    print('有新消息来啦')
    loc_value = (new_loc.x + 150, new_loc.y)
    pyautogui.click(loc_value, duration=1)
    return loc_value

# 将消息区域截图
def get_region():
    wenzi_loc = pyautogui.locateOnScreen('gjl.png', confidence=0.95)
    # print(wenzi_loc)  # 聊天文字区域下面的工具栏坐标
    # 根据工具栏的坐标，计算出消息区域的坐标
    reg = (int(wenzi_loc.left), int(wenzi_loc.top) - 60, 260, 45)
    pyautogui.screenshot('msg.png', region=reg)

# 识别截图信息
def get_ocr_text():
    ocr = CnOcr()
    res = ocr.ocr('msg.png')
    msg = res[-1]['text']  # 取出识别结果中最后一个数据中text键对应的值
    return msg

# 根据识别到的信息回复对方
def reply_friend(msg,loc_value):
    if msg in friend:
        print('朋友发过来的信息：', msg)
        index = friend.index(msg)  # 获取元素在列表中的索引
        print('我回复过去的信息：', me[index])
        copy_send(me[index])
    else:
        print('朋友发过来的信息：', msg)
        index = random.randint(0, len(elsemsg) - 1)
        print('随机回复信息：', elsemsg[index])
        copy_send(elsemsg[index])
    pyautogui.click(loc_value[0], loc_value[1] + 50, duration=1)

def run():
    # 1、根据微信图片去打开微信
    loc = pyautogui.locateCenterOnScreen('VX.png')
    pyautogui.doubleClick(loc)
    time.sleep(1)
    while True:
        try:
            # 2、检测是否有新消息  等待新消息
            loc_value = get_news()
            # 3、将消息区域截图
            get_region()
            # 4、识别截图的信息
            msg = get_ocr_text()
            # 5、根据识别的信息回复对方
            reply_friend(msg,loc_value)
        except:
            print('目前没有新消息')
        time.sleep(5)

if __name__ == '__main__':
    run()
