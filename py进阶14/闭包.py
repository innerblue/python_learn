

"""
什么是闭包：
定义双层嵌套函数，内层函数可以访问外层函数的变量
讲内层函数作为外层函数的返回值，此内层函数就是闭包函数

闭包的好处和缺点：
优点；
不定义全局变量，也可以让函数持续修改和访问一个外部变量
闭包函数引用的外部变量，是外层函数的内部变量。作用域封闭难以被误操作修改
缺点：额外的内存占用（因为持续的调用外部函数）

nonlocal关键字的作用：
在闭包内部函数中想要修改外部函数的变量值，要用nonlocal声明这个外部变量
"""
# 简单闭包
def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("我")
fn1("是")

fn2 = outer("他")
fn2("喜欢")

# 用nonlocal关键字修改外部函数参数的值
def outer(num1):

    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner

fn3 = outer(10)
fn3(10)
fn3(10)
fn3(10)

# 使用闭包完成ATM小案例（存钱取钱）
def account_create(initial_amount=0):       # 默认参数

    def atm(num,deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款，存{num}，余额{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款，取{num},余额{initial_amount}")

    return atm

atm = account_create(100)
atm(50)
atm(20,False)