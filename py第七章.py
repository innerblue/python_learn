# 函数进阶
"""目录
函数的多返回值
函数多种传参方式
匿名函数"""
# 函数的多返回值
def test_return():
    return 1,2
result = test_return()
print(f"函数返回结果{result}，类型{type(result)}")   # 用一个变量接收，结果是元组
x,y = test_return()
print(x)                                          # 可以用多个变量分别接收
print(y)
def test2_return():
    return 1,"hello",True
x,y,z = test2_return()
print(x)
print(y)
print(z)
# 定义函数的参数
"""
1、在参数表中写明了参数名key的参数，固定了顺序和数量的固定参数
def func(key1,key2,key3...):
def func(key1,key2 = value2...):
2、定义时不知道会传入多少参数的可变参数
def func(*args):        不带key的多个参数
def func(**kwargs):     key=value形式的多个参数
"""
# 固定参数
def func_test(key1,key2,key3=23):
    print("k1=%s,k2=%s,k3=%s"%(key1,key2,key3))

func_test("v1","v2")    # 没有传入key3，使用了缺省值
func_test("ab","cd",123)    # 传入了key3
func_test(key2=2,key1=1)            # 使用参数名称就可以不管顺序
# 可变参数
def func_test2(*args):
    for arg,i in zip(args,range(len(args))):
        print(f"arg{i} = {arg}")

func_test2(12,"hello",34,True)
print()
def func_test3(**kwargs):
    for key,value in kwargs.items():
        print("%s = %s"%(key,value))

func_test3(myname="wjy",myage=20,say="hello" )
# 调用函数时的参数
"""
1、位置参数
没有名字，如：func(arg1,arg2,arg3...)
2、带key的关键字参数，如：func(key1=arg1,key2=arg2...)
如果混用，位置函数必须在前，关键字函数必须在后"""
# 练习案例：水仙花数判定
"""
创建一个函数，接收一个参数n（n>=100），判断这个数是否为水仙花数
水仙花数：如果这个数为m位数，则每个数位上的数字的m次幂之和等于他本身
如：1**3+5**3+3**3 = 153
结果返回True或False
"""
# 我的（错误）答案(啥b)
"""
def judge_hana(n):                         #有点问题...
    if n < 100:
        result = False
    else:
        m = len(str(n))
        sum = (n%10)**m
        for i in range(1,m):
            j = n // (10**i)
            sum += j**m
        if sum == n:
            result = True
        else:
            result = False

    return result
    """
# 别人的正确答案(流b)

def judge_hana(n):
    m = len(n)
    s = sum(int(n[i])**m for i in range(m))
    return s == int(n)


# print(judge_hana(input("请输入一个数：")))

# 创建一个函数，接受一个参数max（max>=1000）,调用上题编写的判断函数，求100到max间的水仙花数
def search_hana(max):
    if max < 1000:
        return False
    else:
        alist = []
        for j in range(100,max+1):
            if judge_hana(str(j)):
                alist.append(j)
        return print(f"100到{max}间的水仙花数是：{alist}")

#r = int(input("请输入一个数："))
#print(search_hana(r))
# 创建一个函数，接受两个字符串作为参数，返回两个字符串字符集合的并集
def uni_set(astr,bstr):
    alist=[]
    blist=[]
    for i,j in zip(astr,bstr):
        alist.append(i)
        blist.append(j)
    alist.extend(blist)
    return set(alist)
#print(uni_set("123","345"))

# 函数作为参数传递
def test_func(computer):
    result = computer(1,2)  # 确定computer是函数
    print(f"computer参数的数据类型是{type(computer)}")
    print(f"计算结果:{result}")
# 定义一个函数，准备作为参数传入另一个函数
def computer(x,y):
    return x + y
#test_func(computer)
# 将函数传入的作用在于：传入计算逻辑而非数据
# lambda匿名函数
"""
def关键字，定义带有名称的函数——可重复使用
lambda关键字，可以定义匿名函数（无名称）——只能使用一次
"""
# 使用匿名函数调用刚写的test_func
test_func(lambda x,y:x + y)     # lambda不能写多行

