# 异常（bug）
"""
异常就是程序运行的过程中出现了错误
异常的捕获
基本语法：try：
            可能发生错误的代码
        except：
            如果出现异常执行的代码
"""
# 基本捕获语法
"""
try:
    f=open("D:/abc.txt","r",encoding="UTF-8")
except:
    print(f"出现异常了，因为文件不存在，我将r模式改为w模式打开")
    f=open("D:/abc.txt","w",encoding="UTF-8")
"""
# 捕获指定异常
"""
try:
    #1/0
    print(name)
except NameError as er:
    print("出现了变量未定义的异常")
"""
# 捕获多个异常
"""
try:
    1/0
    print(name)
except(NameError,ZeroDivisionError) as er:
    print("出现了变量未定义 或 除以0的异常")
"""
# 捕获所有异常
"""
try:
    f = open("D:/123.txt","r")
except Exception as e:
    print("出现异常了")
"""
# 异常的finally
"""
try:
    f = open("D:/123.txt","r",encoding="UTF-8")
except Exception as e:
    print("出现异常了")
else:
    print("好高兴，没有异常")
finally:
    f.close()       # 有没有异常finally后的代码都会执行
"""

# 异常的传递
def func1():
    print("func1开始执行")
    num = 1/0
    print("func1结束执行")
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常信息是：{e}")

# try:
#     f = open("D:/123.txt","r",encoding="UTF-8")
# except Exception as e:
#     print("出现异常了")
#     f = open("D:/123.txt", "w", encoding="UTF-8")
# else:
#     print("好高兴，没有异常")
# finally:
#     f.close()       # 有没有异常finally后的代码都会执行

# 模块（module）
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
只引用模块中某个函数，而无需引用整个模块时使用，调用时不需要再加上命名空间（也就是直接写函数就行，不需要在前面加上模块.）
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
# 制作自定义模块
# 详见文件夹“pytestandcase”中的python文件
# 自定义python包
"""
包就是一个文件夹，里面可以存放许多python的模块
有“__init__.py”文件的才是包，否则就只是一个普通的文件夹
包中__all__变量类似模块，写在“__init__.py”文件中,可以控制使用import *时包里那些模块可以被导入
如何导入包中的模块，具体实例请看文件夹“pytestandcase”中的test_my_module.py
"""
# 练习案例：自定义工具包
"""
创建一个自定义包，名称为：my_utils（我的工具）
在包里提供两个模块：
str_util.py 字符串相关工具，内含：
函数：str_reverse(s) 接收传入字符串，将字符串反转返回
函数：substr(s,x,y),按照下标x和y，对字符串切片
file_util.py 文件处理相关工具，内含：
函数：print_file_info(file_name) 接收传入文件的路径，打印文件的全部内容，若文件不存在则捕获异常，输出提示信息，
通过finally关闭文件对象
函数：append_to_file(file_name,data) 接收文件路径及传入数据，将数据追加写入到文件中
"""

