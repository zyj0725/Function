"""
    匿名函数lambda
"""

f = lambda n : (n ** 2 + 1) % 5 == 0
print(f(3))
print(f(4))

mymax = lambda x,y : max(x,y)
print(mymax(100,200))