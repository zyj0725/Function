'''
    装饰器
'''

def log_in(li):
    def log(name,num):      # 先登录
        print(name,'先生/女士，您正在登录手机银行')
        li(name,num)
    return log

def print_password(pw):
    def pwd(name,num):     # 输入密码
        print("请输入密码:")
        pw(name,num)
    return pwd

@log_in
@print_password
# 存钱过程
def save_money(name,num):
    print(name,'先生/女士，您转入了',num,'元')

# 取钱过程
@log_in
@print_password
def withdraw(name,num):
    print(name,'先生/女士，您转出了',num,'元')

save_money('张晓明',2000)
withdraw('唐小红',1000)