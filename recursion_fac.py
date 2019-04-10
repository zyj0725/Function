"""
    递归函数
"""

def f(n):
    print("进入第",n,"层")
    if n == 3:
        return
    f(n+1)
    print("退回第",n,"层")

f(1)
print("递归结束")