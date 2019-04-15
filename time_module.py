#! /usr/bin/python3
# _*_ coding:utf8 _*_
'''
    运用时间模块算出自己已经出生了多少天，出生当天星期几
'''
import time

year = int(input("请输入出生年份:"))
month = int(input("请输入出生月份:"))
day = int(input("请输入出生日:"))
t = (year,month,day,0,0,0,0,0,0)    # 出生时间元组
b_s = time.mktime(t)        # 从出生到1970年计算机元年秒数
t_s = time.time()       # 现在距离1970年秒数
d = (t_s - b_s)/60/60//24   # 通过秒差计算出生天数
w = time.localtime(b_s)[6]  # 出生当天星期几
week = {0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期天',}
print("您从出生到现在已经%d天" % d)
print("您出生当天是%s" % week[w])

# 电子格式不停显示时分秒
while True:
    print(time.asctime()[10:19])
    time.sleep(1)

