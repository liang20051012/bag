#爬取当前网址第一页的图片 保存到本地
# https://pic.netbian.com/uploads/allimg/250306/162113-174124927333d0.jpg
# https://pic.netbian.com/tupian/37938.html
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
#向网页发送请求
url="https://pic.netbian.com/4kdongman/"
#res=requests.get(url)
# res.encoding=res.apparent_encoding
import pyhttpx
#以另一种方式发送请求
# headers = {':authority':'music.163.com',
# ':ethod':"GET",
# ":path": "/discover/toplist?id=2884035",
# ':scheme':'https',
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# 'Accept-Encoding':"gzip, deflate, br, zstd",
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# "Cookie":"NMTID=00OaY2OSviGn9l8MUEZrtPV8XAvor8AAAGVxg_9zw; _iuqxldmzr_=32; _ntes_nnid=a7846ce32321cd1e809be69a63c5f477,1742784692465; _ntes_nuid=a7846ce32321cd1e809be69a63c5f477; WEVNSM=1.0.0; WNMCID=qrhhdn.1742784693103.01.0; WM_TID=YfqSVX2UQX1EBVVBFUfDc%2FU9E1RAzVjR; sDeviceId=YD-OinjcdivF15EBhQFRVeDdqQpBhFV2M%2BP; ntes_utid=tid._.2cT9aa3dPLtFFxAEBFeTY%252FRoAxFA2JuL._.0; JSESSIONID-WYYY=p9S5J80%2FrMiTtl%5CBruxa5vr08BVVDPf4ABTaffPoT%2FyORSVr91igIubeC9S5IIpu3UjMy6dzA2aaxo5ggxyEo9FWZg7ZidAcPfqk8A6Ve8wqBy8hbC16G5JJQuTiyW14XvShHqYxHo2TMTz38ctBRMarBJPpE22rEJ4kU7DDDnfPc6rc%3A1742880984103; WM_NI=RrV3ofj%2FDnQ5Z1%2BNLNcrJnwIR3x1I1ott837Cut5COzJzU8ZWvayHdT8wyYiTv450XJwq3IE6qoHeDnll3KWSeirm56MKVkwCelMlYEzRGdao2xaAhKEZNNVluxs5FRJYVY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4b24eb69eab91e668a9a88bb7d44e839e9a86db47b78cab9aeb6bf2eea1ace82af0fea7c3b92a92ae9ad4ee6eaaf18c8fd43f9aefe5afcf46a1ae868ff64392edb8d2cc3badacbcd9b23d81abbcd6c245ba96b6b6bb5295aaaf9acb7098e8b99adc6398aafcd6b3548aa9bfd4cc4ff6afa1a9e850aeb4a4d4ca5d91bba793f03ff69385b7ea7d81bba4aeef5387a69ea8e76badeeb882c464899b96afcd5eb0abb894b84e929697b7dc37e2a3",
# 'Priority':'u=0, i',
# 'Referer':'https://music.163.com/',
# 'Sec-Ch-Ua':""Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"",
# "Sec-Ch-Ua-Mobile": '?0',
# "Sec-Ch-Ua-Platform":'"Windows"',
# "sec-fetch-dest":"iframe",
# "sec-fetch-mode":"navigate",
# "sec-fetch-site":"same-origin",
# "Upgrade-Insecure-Requests":'1',
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}
# session = pyhttpx.HttpSession()
# res = requests.get(url,headers=headers)
# print(res)
#解析网页，定位标签
# soup=BeautifulSoup(res.text,"html.parser")
# div=soup.find("div",{"class":"slist"})
# ul=soup.find("ul",{"class":"clearfix"})
# li_list=ul.find_all("li")
# #拿取数据并保存
# j=1
# for i in li_list:
#     img=i.find("img")
#     foot=img["src"]
#     head="https://pic.netbian.com/"
#     url=head+foot
#     res=requests.get(url)
#     with open(f"{j}.png","wb")as f:
#         f.write(res.content)
#     j+=1
#招聘网页拿取
#第一页：url="https://yiqifu.baidu.com/g/aqc/joblist?q=python"
#第二页：url="https://yiqifu.baidu.com/g/aqc/joblist?q=python"
#对于不同页数网址一样
# import requests
#
# for i in range(1, 2):
#     url = f"https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?q=python&page={i}&pagesize=20&district=100000&salaryrange="
#     head = {'accept': 'application/json, text/plain, */*',
#             'accept-encoding': 'gzip, deflate, br, zstd',
#             'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#             'connection': 'keep-alive',
#             'cookie': 'BAIDUID_BFESS=495446C74536FAEEA09F99C4BF447EA5:FG=1; RT="z=1&dm=baidu.com&si=aea694c0-10b6-489c-93fb-54f63662b1ec&ss=m8fq7cje&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=15qa&nu=17c7h8r1a&cl=1rje&ul=1rf5u&hd=1rf65"; log_guid=61446ecc7337009e72738bdd6cf492c8; clue_site=pc; log_first_time=1742643572446; Hm_lvt_37e1bd75d9c0b74f7b4a8ba07566c281=1742433728,1742643573; HMACCOUNT=2C6D46683668C87A; Hm_lpvt_37e1bd75d9c0b74f7b4a8ba07566c281=1742643614; log_last_time=1742643726225',
#             'host': 'yiqifu.baidu.com',
#             'referer': 'https://yiqifu.baidu.com/g/aqc/joblist?q=python',
#             'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-origin',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
#             'x-requested-with': 'XMLHttpRequest'}
#     res = requests.get(url, headers=head)
#     res_json = res.json()
#     jobs = []
#     for i in res_json["data"]["list"]:
#         job = {}
#         job["职位"] = i['jobName'].replace("<em>", "").replace("</em>", "")
#     #以上是第一页，以下是点进去
#         bid = i["bid"]
#         jobId=i["jobId"]
#         url =f"https://yiqifu.baidu.com/g/aqc/jobDetailAjax?jobId={jobId}&bid={bid}"
#         job_xiangqing=requests.get(url,headers=head)
#         job_xiangqing_json=job_xiangqing.json()
#         job_xiangqing_data=job_xiangqing_json['data']
#         job["职业详情"]=job_xiangqing_data['desc']
#         jobs.append(job)
# print(jobs)
