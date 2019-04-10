'''
    高阶函数map,filter,sorted
'''

# 求: 1**9 + 2**8 + 3**7 + .... + 9**1的和
# def fun_sum(x,y):
#     return x ** y
# # fun_sum = lambda x,y:x ** y
# print(sum(map(fun_sum,range(1,10),range(9,0,-1))))

# 用filter函数把100到200的全部素数求出来,放入列表L中
# 求300 ~ 400之间全部素数的和

# L = []
# def is_prime(num):
#     for x in range(2,num):
#         if num % x == 0:
#             return False
#     return True
#
# for num in filter(is_prime,range(100,200)):
#     L.append(num)
# print(L)
# print(sum(filter(is_prime,range(300,400))))


# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 排序的依据为原字符串反序的字符串
# 'moT', 'yrreJ', 'ekipS', 'ekyT'
# 结果:
# ['Spike', 'Tyke', 'Tom', 'Jerry']

names = ['Tom', 'Jerry', 'Spike', 'Tyke']
def func_sorted(n):
    return n[::-1]

L = sorted(names,key=func_sorted)
# L1 = sorted(names,key=lambda n:n[::-1])
print(L)
