# while循环的基础语法
i = 0
while i < 10:
    print("小A，我喜欢你")
    i += 1
    # 必须设置终止循环的条件；注意缩进
# 1-100求和
i = 1
s = 0
while i <= 100:
    s += i
    i += 1
print(f"1-100累加结果是：{s}")
# 公比为2的等比数列前10项求和
i = 1
s = 0
a = 1
q = 2
while i <= 10:
    s += a
    a *= q
    i += 1
print(f"公比为2的等比数列前10项的和：{s}")
# while 循环猜数字
#import random
#num = random.randint(1,100)
# 范例如下
#flag = True
#count = 0
#while flag:    # 直接用布尔类型
#    guess_num = int(input("请输入你猜测的数字："))
#    count += 1
#    if guess_num == num:
#        print("你猜对了")
#        flag = False   # 设置False为终止循环的条件
#    else:
#        if guess_num > num:
#            print("你猜大了")
 #       else:
#            print("你猜小了")
#print(f"你一共猜了{count}次")
# 另寻他法:
#import random
#num = random.randint(1,100)
#guess_num = int(input("请输入你猜测的数字："))
#count = 0
#while guess_num != num:
#    count += 1
#    if guess_num > num:
#        print("你猜大了")
#    else:
#        print("你猜小了")
#    guess_num = int(input("请输入你猜测的数字："))

#print(f"猜对了，你一共猜了{count}次")

# while循环的嵌套
#i = 1
#while i <= 100:
#    print(f"向小A表白的第{i}天...")
#    j = 1
#    while j <= 10:
#        print(f"向小A送的第{j}支玫瑰")
#        j += 1
#    i += 1
#    print("小A，我喜欢你！")
#print(f"向小A表白的第{i-1}天，表白成功了")   # 直接用i天会出现101天
"""注意条件的控制，注意空格缩进"""
# 补充1：print语句不换行功能
print("Hello")
print("World")     # 这样输出会换行

#print("Hello",end = '')
#print("World",end = '')     # 这样输出不换行
# 补充2：制表符
print("Hello World")
print("Byebye World")   # 这样输出对不齐

print("Hello\tWorld")
print("Byebye\tWorld")  # 这样就能对齐
# 输出九九乘法表
# 我的答案：
print()
i = 1
while i <= 9:
    j = 1
    while j <= i:
        if j < i:
            print(f"{j}*{i}={i * j}\t", end='')
        else:
            print(f"{j}*{i}={i * j}\t")     # 不输出 end
        j += 1
    i += 1
print()
# 标准答案：
i = 1   # 定义外层循环的控制变量
while i <= 9:
    j = 1   # 定义内层循环的控制变量
    while j <= i:
        print(f"{j}*{i}={i*j}\t",end='')
        j += 1
    i += 1
    print()     #换行

"""for循环（遍历循环），for 临时变量 in 序列:"""
#name = "wjefasd"
#for x in name:
#    print(x)    # 无法定义循环条件
# 练习：数一数有几个a
name = "asgahajsdfaghahhgaeg"
count = 0
for x in name:
    if x == "a":
        count += 1
print(f"{name}中共含有{count}个a")
# range语句
# 序列类型 指其内容可以一个个依次取出的类型
# 序列类型包括 字符串 列表 元组
"""
1、range(num) 获得一个从0开始，到num结束的数字序列（不含num本身）
如range(10)获得[0,1,2,3,4,5,6,7,8,9]
2、range(num1,num2) 获得一个从num1开始，到num2结束的数字序列（不含num2本身）
如 range(5,10)获得[5,6,7,8,9];
3、range(num1,num2,step) 获得一个从num1开始，到num2结束的数字序列（不含num2本身）,step为数字之间的步长
如 range(5,10,2)获得[5,7,9]"""
# for x in range(10):
#     print(x)
for x in range(5,10):
    print(x)
print()
for x in range(5,10,2):
    print(x)
# 练习：有几个偶数
# 我的答案1：
#num = int(input("输一个数："))
#count = 0
#for x in range(1,num):
 #   if x%2 == 0:
#        count += 1
#    if x != num-1:
#        print(f"{x},",end = '')
#    else:
#        print(x)

#print(f"1~{num}的范围内（不含{num}本身），有{count}个偶数")

#我的答案2：
num = int(input("输一个数："))
count = 0
for x in range(1,num):
    print(f"{x},", end='')
for x in range(2,num,2):
    count += 1
print(f"1~{num}的范围内（不含{num}本身），有{count}个偶数")
# 变量作用域
# for循环中的临时变量规范上只应该作用在循环内部，但不遵守也能运行

# for循环的嵌套
#i = 0
#for i in range(1,11):
#    print(f"今天是给小A表白的第{i}天，加油坚持")
#   for j in range(1,11):
#       print(f"给小A送的第{j}朵花")
#    print("小A，我喜欢你")
#print(f"给小A表白的第{i}天，表白成功啦")
# for循环 可以和 while循环 相互嵌套

# 练习：用for循环输出九九乘法表（可以对比之前while循环同样的练习）
for i in range(1,10):   # 外层循环控制行数，内层循环控制每一行的内容
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()     # 换行

# 循环中断，break和continue
"""
continue:中断所在循环的当前执行，直接进入下一次；
break:直接结束所在的循环
注意：continue和break在for和while循环中作用一致；
在嵌套循环中，只能作用于所在的循环，无法对上层循环起作用
"""
# continue演示
#for i in range(1,6):
#    print("语句1")
#    for i in range(1,6):
#        print("语句2")
#       continue
#        print("语句3")
#    print("语句4")    # 得到的结果是输出5次语句1，25次语句2,5次语句4
# break演示
for i in range(1,6):
    print("语句1")
    for i in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")    # 得到的结果是输出5次语句1,5次语句2,5次语句4
# 案例：发工资


money = 10000
for i in range(1,20):
    import random
    score = random.randint(1,10)

    if score < 5:
        print(f"员工{i},绩效分{score},不满足，不发工资，下一位")
        continue    # “下一位”，即跳过发放，用continue
    if money >= 1000:
        money -= 1000   # 原来的余额去掉发放的工资等于剩下的余额
        print(f"员工{i},满足条件，发放工资1000元，账户余额：{money}元")
    else:
        print(f"余额不足，当前余额:{money}元，不足以发工资，不发了，下个月再来领取")
        break   # 余额不足所以结束发放，用break结束循环




