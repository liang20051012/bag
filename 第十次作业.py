#2使用 BS4 获取   https://www.thepaper.cn/newsDetail_forward_26649723  文章内容
import requests
from bs4 import BeautifulSoup
def text():
    url="https://www.thepaper.cn/newsDetail_forward_26649723"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    div1=soup.find("div",{"class":"index_cententWrap__Jv8jK"})
    print(div1.text)
text()