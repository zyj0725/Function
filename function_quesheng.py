'''
    缺省参数
'''

def queSheng(name,age=15,gender='女生'):
    return name,age,gender

print(queSheng(name='小红'))
print(queSheng(name='小明',gender='男生'))