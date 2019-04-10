'''
    写一个函数 input_number
      此函数用来获取用户循环输入的整数,当输入负数时结束输入.
      将用户输入的数字以"列表"的形式返回,再用内建函数max, min, sum求出用户输入的最大值,最小值和平均值
      利用input_number获取用户输入的数字列表
      写一个函数split_number(L) 传入得到的列表
    将所有的数字分为奇数和偶数,分别放在两个列表odds 和 evens 中
  同时返回这两个列表打印其中的数据
'''

def input_number():
    l = []
    while True:
        num = int(input("请输入一个整数:"))
        if num < 0:
            break
        else:
            l.append(num)
    return l

def split_numbers(L):
    odds = []
    evens = []
    for x in L:
        if x % 2 == 1:
            odds.append(x)
        if x % 2 == 0:
            evens.append(x)
    return odds,evens

L = input_number()
T = split_numbers(L)
odds,evens = T
print(L)  # 打印用户输入的列表
print("用户输入的最大值是:", max(L))
print("用户输入的最小值是:", min(L))
print("用户输入的平均是:", sum(L)/len(L))
print("奇数为:",odds)
print("偶数为:",evens)
