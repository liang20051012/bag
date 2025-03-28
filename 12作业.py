#爬取网易云音乐原创榜
# 网易云音乐排行榜  https://music.163.com/#/discover/toplist?id=2884035
# 网易云音乐外链格式  http://music.163.com/song/media/outer/url?id=xxxxx.mp3
# http://music.163.com/song/media/outer/url?id=2643813746.mp3
#获得id
import os
import requests
from bs4 import BeautifulSoup
#分析数据从哪个url来
#解析分析数据
# url="https://music.163.com/discover/toplist?id=2884035"
# head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
# res=requests.get(url,headers=head)
# soup=BeautifulSoup(res.text,"html.parser")
# a_list=soup.find_all("a",href=True)
# for a in a_list:
#     href=a["href"]
#     if "/song?id=" in href and "$" not in href:
#         id=a["href"]
#         id=id.replace("/song?id=",'')
#         music_url=f"https://music.163.com/discover/toplist?id={id}.mp3"
#         name=a.text
#         res1=requests.get(music_url,headers=head)
#         if not os.path.exists("mp3"):
#             os.mkdir("mp3")
#         path=f"./mp3/{name}.mp3"
#         with open(path,"wb") as f:
#             f.write(res1.content)
#起点中文网爬取
#"https://www.qidian.com/book/1010868264/"                          小说首页
#“https://www.qidian.com/chapter/1010868264/402733549/”             小说第一页
#“https://www.qidian.com/chapter/1010868264/402760766/”             小说第二页
url="https://www.qidian.com/book/1010868264/"
head={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0","cookie":"e1=%7B%22l6%22%3A%221%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A%22%22%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; e2=%7B%22l6%22%3A%221%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_H_shuyouclass%22%7D; traffic_utm_referer=; newstatisticUUID=1743032700_1318905565; fu=1419191537; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A2%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A2%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%7D; supportwebp=true; supportWebp=true; traffic_search_engine=; _gid=GA1.2.1553497795.1743032893; _ga=GA1.1.779935482.1743032847; _ga_PFYW0QLV3P=GS1.1.1743032847.1.1.1743034613.0.0.0; _ga_FZMMH98S83=GS1.1.1743032847.1.1.1743034613.0.0.0; _csrfToken=UATH9yv6jjXSrJ8Yiqm9BBBl6YST0TwET1SiXimV; Hm_lvt_f00f67093ce2f38f215010b699629083=1743032701,1743060403; Hm_lpvt_f00f67093ce2f38f215010b699629083=1743060403; HMACCOUNT=2C6D46683668C87A; w_tsfp=ltvuV0MF2utBvS0Q7anpkkyqFzslfTk4h0wpEaR0f5thQLErU5mB0oZ8uc/1M3Ha4cxnvd7DsZoyJTLYCJI3dwNFF8iWdY4TjwnCm9QtjtoUBRAzEZiKCFIbdb90vjMVfXhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5TfYsF7yL1wiVrsR1UPB3X1NCHwn50K5du5bYU+vdcb9SqA="}
res=requests.get(url,headers=head)
soup=BeautifulSoup(res.text,"html.parser")
a_list=soup.find_all("a",{"class":"chapter-name"})
index=1
for a in a_list:
    chap_url="https:"+a["href"]
    chap_name=a.text
    chap_res=requests.get(chap_url,headers=head)
    chap_suop=BeautifulSoup(chap_res.text,"html.parser")
    main=chap_suop.find("main",{"data-type":"cjk"})
    p_list=main.find_all("p")
    if not os.path.exists("txt"):
        os.mkdir("txt")
    print(chap_name)
    path=f"./txt/{chap_name}.txt"
    with open(path,"w",encoding="utf-8")as f:
        for p in p_list:
            f.write(p.text)
            f.write("\n")
        if index==3:
            break
        index+=1