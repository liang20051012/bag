#识别微信图标
import pyautogui
res=pyautogui.locateCenterOnScreen("VX.png")
pyautogui.click(res.x,res.y,clicks=1)
#是否有新消息
news=()
try:
    news=pyautogui.locateCenterOnScreen("new.png")
#print(news)
except:
    print("没有新信息")

#点击news这个位置前提是有新消息
#pyautogui.click(news.x,news.y,clicks=1)
         #指定区域进行消息截图
         #识别消息
         #根据消息回复
