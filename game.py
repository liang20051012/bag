# 1.菜单选择    开始游戏  退出游戏
# 2.让程序随机生成一个字符串 供我们进行打字计时 测试我们的打字速度
# 3.显示随机生成得字符串 提示用户进行输入
# 4.是否输入正确
# 5.计时，平均每个字符花费的时间
import random
import string
import time


# 展示菜单
def show_menu():
    print("请输入你逍遥的功能")
    print("1.开始游戏")
    print("2.退出游戏")


# 生成随机字符串
def random_str():
    len = 10
    str_list = string.ascii_letters  # 得到一个列表， 这个列中中时所有的大小写字母得集合
    random_str = ""
    random_list = random.sample(str_list, len)  # 随机抽取列表中len个字母组成一个列表
    rand_str = random_str.join(random_list)  # 生成了 随机字符串
    return rand_str  # 返回 随机得字符串


show_menu()
ac = input()  # 录入用户选择得功能
# 通过选择的不同实现不同的效果   这里是不是就出现了分支   所以要用 if
if ac == "1":
    # 开始游戏
    rand_str1 = random_str()  # 调用生成随机字符串的函数
    # 展示随机字符串
    print(rand_str1)
    # 记录开始时间
    began_time = time.time()
    in_str = input("请输入相同的字符串")
    # 记录结束时间
    end_time = time.time()
    use_time = end_time - began_time
    avg_time = use_time / 10
    # 判断输入结果是否正确
    if in_str == rand_str1:
        print("输入正确")
        print("所花时间为", use_time, "平均每个字符花费时间", avg_time)
    else:
        print("输入错误")
elif ac == "2":
    # 退出游戏
    print("退出成功")
else:
    print("功能选择错误")
