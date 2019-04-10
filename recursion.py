"""
	练习递归
	 1. 已知:
      第五个人比第四个人大2岁
      第四个人比第三个人大2岁
      第三个人比第二个人大2岁
      第二个人比第一个人大2岁
      第一个人说他10岁
    编写程序算出第5个人几岁?
    使用递归和循环两种方式来做
"""

# 使用简单的递归
def fifth(num):
	if num == 5:
		return 10
	return fifth(num+1) + 2
print("第五个人年龄为:",fifth(1))

# 用循环方法
first = 10
for year in range(1,6):
	if year == 5:
		break
	first += 2
print("第五个人年龄为:",first)