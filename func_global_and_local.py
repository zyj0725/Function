'''
    globals()函数和locals()函数得使用
'''

a = 10
b = 20
def global_local(c,b):
    d = 40
    print("全局变量字典：",globals())
    print("局部变量字典：",locals())
    return c,b,d,a

print(global_local(60,50))
print(b)
