'''
    局部变量和全局变量
      创建一个全局变量:
  L = []
  写一个函数:
  def input_number():
      读入正整数 放到L列表内

  # ......   input_number()  # 输入1 2 3
  print(L)  # [1, 2, 3]
  # ..... input_number()  # 输入4, 5
  print(L)  # [1, 2, 3, 4, 5]

'''

L = []
def input_number():
    L1 = []
    while True:
        num = int(input("请输入一个正整数:"))
        if num < 0:
            break
        L1.append(num)
    return L1

L += input_number()
print(L)
L += input_number()
print(L)

#global的使用
def hello(name):
    global count
    count += 1
    return count

count = 0  # 此变量用来记录hello函数被调用的次数
hello("小张")
hello("小李")
print("函数hello已经被调用%d次" % count)  # 2
hello("小赵")
print("函数hello已经被调用%d次" % count)  # 3

#nonlocal的使用
a = 1
def f1():
    a = 2
    print("f1中的a",a)
    def f2():
        nonlocal a
        a = 3
        print("f2中的a",a)
    f2()

print("全局的a",a)
f1()