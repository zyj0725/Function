#! /usr/bin/python3
# _*_ coding:utf-8 _*_
'''
     猜数字游戏:
    随机生成一个0~100的整数,用变量x绑定
    让用户输入一个数y,输出猜数字的结果.
       1) 如果y等于x,则提示"恭喜您猜对了!", 退出程序
       2) 如果y大于x,同提示"您猜大了"
       3) 如果y小于x,同提示"您猜小了"
      让用户循环输入，直到猜对为止，同时显示用户猜数字的次数后退出程序
    Author:zyj
    Time:2019.4.16
'''
import random

count = 0
x = random.randint(0,100)
while True:
    y = int(input("请输入一个数字:"))
    count += 1
    if y == x:
        print("恭喜您答对了")
        print("您一个猜了%d次" % count)
        break
    elif y > x:
        print("您猜大了")
    else:
        print("您猜小了")

