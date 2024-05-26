# 引用扩展模块
"""
模块（Module）就是程序
每个扩展名为.py的python程序都是一个独立的模块
模块能定义函数，类和变量
组织模块
包(Package)是放在一个文件夹里的模块集合
模块引用方式
import <模块> [as <别名>]  别名即替换成一个新名字
调用模块中的函数时，需要加上模块的命名空间
from <模块> import <函数>
只引用模块中某个函数，而无需引用整个模块时使用，调用时不需要再加上命名空间
from <模块> import <*>
表示导入模块的全部功能，和直接import模块的区别是，举例：
# 1.直接import
import time
print("hello")
time.sleep(10)
print("bye")
# 2.from <模块> import <*>
from time import *
print("hello")
sleep(10)
print("bye")
"""
import random

# 命名空间
"""
表示标识符的可见范围
一个标识符可以在多个命名空间中定义，在不同命名空间中的含义互不相干
dir(<名称>)函数：列出名称的属性
help(<名称>)函数：显示参考手册
"""
# datetime模块
"""
主要的类
获取现在的时间
时间戳
时间的加减法
"""
# 主要的类
"""
datetime.date()      处理日期（年月日）
datetime.time()      处理时间（时分秒毫秒）
datetime.datetime()  处理日期+时间
datetime.timedelta() 处理时段（时间间隔）
"""
import datetime
print(datetime.date.today())    # 获取今天的日期
#使用strftime()格式化，Y代表年，m月，d日，以此类推
time_str = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
print(time_str)
t_now = datetime.datetime.now()     # 获取当前的时间
print(t_now)
tnow_str = t_now.isoformat()    # 标准的ISO格式(同strftime，也是输出字符串)
print(tnow_str)
# 时间戳
"""
指1970年1月1日00时00分00秒到现在的总秒数
将日期转换为时间戳
timetuple()     将时间转换为struct_time格式
time.mktime()   返回用秒数记录时间的浮点数
"""
import time,datetime
today = datetime.date.today()
print(today.timetuple())      # 是个元组
print(time.mktime(today.timetuple()))
print(datetime.date.fromtimestamp(1702396800.0))    # 用fromtimestamp()输入秒数返回一个时间对象

today_now = datetime.datetime.now()
yesterday = today_now - datetime.timedelta(days = 1)    # 算昨天是什么时候
print(yesterday)
hours = today_now - datetime.timedelta(hours = 1)       # 算一小时前是什么时候
print(hours)

# calendar模块
"""
制作电子日历
将日历列表化
与日历相关的计算
"""
# 制作电子日历
"""
常用函数：calendar.calendar(<年>)，calendar.month(<年>,<月>)，calendar.prmonth(<年>,<月>)，calendar.prcal(<年>)
这里的pr表示直接打印出来而不是返回
"""
import calendar
print(calendar.month(2023,12))
calendar.prmonth(2023,12)
print(calendar.calendar(2023))                  # 生成2023一整年的日历
print("--------------------------------分--隔----------------------------------")
calendar.prcal(2023)
# 将日历列表化
print(calendar.monthcalendar(2023,12))    # 返回某一年的某一个月份日历，是个嵌套列表
# 里层的列表有七个元素，代表一周。如果没有本月的日期，则为0
# 判别闰年
print(calendar.isleap(2023))    # 返回布尔值
# 计算某月共有多少天，从周几开始
print(calendar.monthrange(2023,12)) # 返回元组(4,31),4表示该月第一天是周4,31表示该月有31天
print(calendar.weekday(2023,12,21)) # 计算这一天是周几
print()
# time模块(time.py这个代码文件)
"""
获取时间戳
获取日期格式
利用索引获取时间信息
让程序睡会
"""
import time
t1 = time.time()        # 获取当前时间，也可以time.asctime();time.ctime()
s = 0
for i in range(100000):
    s += 1
print(s)
t2 = time.time()
print(t2-t1)            # 两个“当前时间”相减，就得到了中间这段代码运行的时间
t = (2023,12,14,13,6,45,0,0,0)
print(time.asctime(t))  # 把元组变成日期
# 利用索引获取时间
# struct_time类
t = time.localtime()
print(t)
print(t[0])     # 通过索引得到年
# 让程序睡会
# time.sleep()
#for i in range(3):
#    print(i)
#   t1 = time.time()
#   time.sleep(1)
#    t2 = time.time()
#    print(t2 - t1)

# 基本算数模块
# math模块：支持浮点数运算
"""
math.sin()/math.cos()/math.tan()
math.pi
math.log(x,a)   以a为底的x的对数
math.pow(x,y)   x的y次幂
"""
# cmath模块：支持复数运算
"""
cmath.polar()   极坐标
cmath.rect()    笛卡尔坐标
cmath.exp(x)    e的x次幂
cmath.sqrt(x)   x的平方根
"""
# decimal模块:处理小数——固定精度的浮点值（直接十进制计算转为二进制时可能会出现一些问题）
from decimal import Decimal
print(Decimal("0.1"))       # 输入字符串,生成小数
s = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")   # 小数计算
print(s)
# fractions模块:分数——实现了一个有理数对象
from fractions import Fraction
num = Fraction(1,4)/Fraction(0.25)    # 前一个里，1是分子，4是分母
print(num)
# 浮点数转换为分数
print(Fraction.from_float(1.75))    # 不精确
# random模块：生成（伪）随机数
"""
计算机中的随机数是按照一定算法模拟产生的，其结果是确定的，是可预见的
随机数种子
随机种子相同，随机数的序列也是相同的
random.seed(a=None)  可以用这个设定随机数种子
常见函数：
random()    生成范围[0,1)之间的随机实数
uniform()   生成指定范围内的随机浮点数
randint(m,n)   生成指定范围[m,n]内的整数
randrange(a,b,n) [a,b)范围内，按n递增的集合中随机选择一个数
getrandbits(k)   生成k位二进制的随机整数
"""
colors = ["red","yellow","blue","white"]
print(random.choice(colors))    # 从指定序列中随机选择一个数
print(random.sample(colors,2))  # 能指定每次随机元素的个数
print(random.shuffle(colors))   # 将可变序列中所有元素随机排序

# 持久化模块shelve
"""
对象持久化：对象在创造他们的程序退出后依然存在
pickle模块：任意python对象格式化和解格式化
dbm模块：实现一个通过键访问的文件系统，以存储字节串
shelve模块：按照键把pickle处理后的对象放到一个文件中
"""
# shelve模块
"""
通过构造一个简单的数据库，像操作字典一样按照键存储和获取本地的python对象，使其可以跨程序运行而保持持久化
键：必须是字符串且唯一（与字典不同）
值：任何类型的python对象
一开始必须打开shelve，修改后要关闭它
常用操作：
将任何数据对象，保存到文件中去
d = shelve.open(filename)   # filename是文件名
open函数调用时返回一个shelf对象，通过该对象可以存储内容
访问类似字典形式
d[key] = data   写到文件中
value = key     索引
del d[key]      删除
d.close()       关闭
"""
# 文本文件读写
"""
对于普通的最简单的流式文件
open()函数:f = open(filename[,mode[,buffering]])
f:open返回的文件对象
filename:文件的字符串名
mode:可选参数,打开模式和文件类型
buffering:可选参数，文件的缓冲区，默认-1

mode里第一个字母表示对其的操作：
'r'：读模式
'w'：写模式
'x'：在文件不存在的情况下新创建并写文件
'a'：在文件末未追加写内容（'w','x'都是先清空文件内容重新写）
'+'：表示读写模式
mode第二个字母是文件类型
't'：文本类型
'b'：二进制文件
文件的写操作：f.write(str);f.writelines(strlist):写入字符串列表
文件的读操作：f.read();f.readline():返回一行；f.readlines():返回所有行，列表
"""
f = open("my.txt","w")
f.writelines(["apple\n","pie\n"])
f.close()               # 文件打开后记得关闭
f = open("my.txt","r")
print(f.readlines())
f.close()
# 结构化文本文件：纯文本文件，以","分隔符
"""
csv文件
值没有类型，所有值都是字符串
不能指定字体颜色等样式
不能指定单元格的宽、高，不能合并单元格
没有多个工作表
不能嵌入图像图表
import csv
# 读操作
re = csv.reader()   # 文件读取，返回一个生成器
re = csv.DictReader()   # 用于带表头的csv，返回的每一个单元格都放在一个元组的值内
# 写操作
w = csv.writer()        # 文件不存在时，自动创建；支持单行写入和多行写入
w = csv.writerow(rows)
字典数据写入
w = csv.DictWriter()
w.writerheader()
w.writerow(rows)
"""
# Excel
"""
openxl模块（是第三方库）
"""
# PDF
"""
PyPDF2模块
"""
# 简单的图形界面
"""
图形用户界面（GUI）
easygui模块：第三方模块，可以现实各种对话框、文本框、选择框与用户交互
easygui.egdemo():模块各种功能演示
easygui.msgbox():显示一条消息和提供一个“OK”按钮。用户可以指定任意的消息和标题，甚至重写“OK”按钮的内容
按钮选项
easygui.choicebox():为用户提供了一个可选择的列表，使用序列作为选项
显示文本
easygui.textbox():text参数可以是字符串，列表或元组类型
输入密码
easygui.passwordbox():用户输入的内容用“*”显示
打开文件
easygui.fileopenbox():返回用户选择的文件名（带完整路径）
"""
#import easygui
#easygui.msgbox(msg="(your message goes here)",title=" ",ok_button="OK",image=None,root=None)
#easygui.choicebox(msg = "Pick an item",title=" ",choices=["choice1","choice2","choice3","..."])
#easygui.textbox(msg="Show text message",title=" ",text="Hello World",codebox=False)
#easygui.passwordbox(msg="Enter your password",title=" ",default="",image=None,root=None)

# 海龟作图
"""
画一个边长100像素的等边三角形
turtle模块
import turtle
p = turtle.Pen()    #和 t = turtle.Turtle()效果一样 
p.pencolor("blue")
p.pensize(5)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
可以循环代替
画个正方形
t = turtle.Turtle()
w = turtle.Screen()     # 创建画布
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()
"""
# 画二叉树
"""
需要使用到递归
大叔 = 树干 + 左小树 + 右小树
"""
import turtle
def tree(branchLen,t):  # branchLen代表树干长度
    if branchLen > 5:   # 设定控制条件(最小规模)，避免无限递归
        t.forward(branchLen)    # 画树干
        t.right(20)     # 画右小树
        tree(branchLen-15,t)    # 减小规模
        t.left(40)      # 画左小树
        tree(branchLen-15,t)
        t.right(20)     # 方向回正
    t.backward(branchLen)   # 海龟回原位置
# 调用该函数
def main(num):
    t = turtle.Turtle()     # 生成海龟
    w = turtle.Screen()
    t.left(90)              # 海龟位置调整
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(num,t)
    w.exitonclick()         # 点击画面时画布才会消失

main(90)