"""函数
目标：1.快速体验函数的使用；2.了解函数的作用"""
# 函数是组织好的，可重复使用的，用来实现特定功能的代码块。可以重复使用，提高复用性，减少重复代码，更高效
# 函数的定义
# def 函数名(传入参数):
#     函数体
#     return 返回值
# 案例
#def say_hi():
#    print("hi,I am wjy.")   # 先定义函数
#say_hi()                    # 后调用函数
# 参数和返回值如不需要均可省略
# 练习
#def COVID_19():
#    print("欢迎来到河南！")    # 这里也可以用换行符\n，即 print("欢迎来到河南！\n请出示您的健康码以及72小时核酸证明")
#    print("请出示您的健康码以及72小时核酸证明")
#COVID_19()

# 函数的传入参数
def add(x,y,z):
    result = x + y + z                     # 此处“x，y，z”被称为形式参数
    print(f"{x}加{y}加{z}的结果是{result}")   # 定义函数

add(3,4,5)                         # 调用函数，传入被计算的数字，此处的数字被称为实际参数，形式参数和实际参数要一一对应
# 练习
#def temp(x):
#    if x <= 37.5:
#        print(f"欢迎来到荷兰，请出示您的健康码和24小时核酸证明，并配合测量体温。\n体温测量中，您的体温是{x}度，体温正常请进")    #\n是换行符
#    else:
#        print(f"欢迎来到荷兰，请出示您的健康码和24小时核酸证明，并配合测量体温。\n体温测量中，您的体温是{x}度，需要隔离")
#temp(39)

# 定义一个两数相加的函数
def add(x,y):
    result = x + y
    return result   # 通过返回值，将两数相加的结果返回给调用者。函数体遇到return就结束了，所以写在return后的代码不会执行
r = add(3,4)  # 函数的返回值，可以通过变量去接收
print(r)
# 函数返回值之None用法
#def say_hi():
#    print("你好")     # 该函数无返回值

#result = say_hi()
#print(f"无返回值函数返回的内容是：{result}")              # 返回 None
#print(f"无返回值函数返回的内容类型是：{type(result)}")     # 返回类型 <class 'NoneType'>

#def say_hi():
#    print("你好")     # 该函数无返回值
#    return None
#result = say_hi()
#print(f"无返回值函数返回的内容是：{result}")              # 返回 None，表示空，无意义
#print(f"无返回值函数返回的内容类型是：{type(result)}")     # 返回类型 <class 'NoneType'>
# 在if判断中，None等同于False
# None用于if判断，案例
def check_age(age):
    if age >= 18:
        result = "success"
        return result
    else:
        return None

result = check_age(19)
if not result:
# 此处涉及if not语句。根据上面定义的函数，返回值是None，这里相当于False，而只有True才能进入if，前面加not就相当于反转False为True了
    print("未成年，请勿进入")
# None可以用于声明无初始内容的变量
#num = None

# 函数说明文档
def add(x,y):
    """
    add函数可以接受两个参数，进行两数相加的功能
    :param x:形参x表示两数相加的其中一个数字
    :param y:形参y表示两数相加的另一个数字
    :return:返回值是两数相加的结果
    """
    result = x+y
    print(f"{x}加{y}的结果是{result}")
    return result

message = add(3,4)
# 函数的嵌套调用
# 在一个函数中调用另一个函数就叫函数的嵌套调用
def func_b():
    print("--2--")
def func_a():
    print("--1--")
    func_b()    # 在func_a中调用函数func_b
    print("--3--")

func_a()    # 调用函数func_a
# 变量在函数中的作用域
# 1.局部变量
def test_a():
    num = 100
    print(num)
# 调用函数
test_a()    # 此处num是函数体中的局部变量。出了函数体，局部变量就无法使用
#print(num)
print()     # 空一行
# 2.全局变量
num = 200
def test_a():
    print(f"test_a:{num}")
def test_b():
    print(f"test_b:{num}")
# 调用函数
test_a()
test_b()
print(num)      # 定义在函数体外，在函数体内外都能使用的变量
print()     # 空行
#函数内修改全局变量
#num = 200
#def test_a():
#    print(f"test_a:{num}")
#def test_b():
#    num = 500
#    print(f"test_b:{num}")
# 调用函数
#test_a()
#test_b()
#print(num)      # 此处结果会变成200,500,200.test_b()中的 num 只是临时变量
# global关键字
num = 200
def test_a():
    print(f"test_a:{num}")
def test_b():
    global num  # 设置内部定义的变量为全局变量。结果从test_b()函数体内部修改了全局变量
    num = 500
    print(f"test_b:{num}")
# 调用函数
test_a()
test_b()
print(num)


