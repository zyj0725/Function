"""
    函数变量,函数可作为另一个函数的实参传递
"""
def fa():
    print("调用fa")

def fb():
    print("调用fb")

def fc(fn):
    print("调用fn",fn)
    fn()

fc(fa)
fc(fb)