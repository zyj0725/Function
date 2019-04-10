"""
    位置传参，序列传参，关键字传参，字典关键字传参
"""

def myargs(a,b):
    return a,b

def keyword_args(c,d):
    return c,d

l = [1,2]
s = 'py'
t = (3,4)
print(myargs(5,6))
print(myargs(*l))
print(myargs(*s))
print(myargs(*t))
d = {'c':7,'d':8}
print(keyword_args(d=10,c=9))
print(keyword_args(**d))