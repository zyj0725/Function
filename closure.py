'''
	闭包
	1.必须有内嵌函数
	2.内嵌函数必须引用外部函数的变量
	3.外部函数返回值必须是内嵌函数
'''
def fn(x):
	def in_fn(y):
		return x + y
	return in_fn
f = fn(2)
print(f(3))