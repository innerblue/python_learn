# 文件的读取操作
"""
三种基本操作：
打开，读写，关闭
open()打开函数
语法：open(name,mode,encoding)
name:打开的目标文件名的字符串
mode:打开文件的模式：只读，写入，追加等
encoding：编码格式，推荐UTF-8
模式：r，w，a
"""
#f = open("D:\桌面desktop\数据结构_py\数学建模知识点.txt","r",encoding="UTF-8")
#print(type(f))
# 读取文件read()
#print(f"读取10个字节的结果是：{f.read(10)}")
#print(f"读取全部字节的结果是：{f.read()}")     # 多次调用read函数，下一个read会在上一个read的结尾处接着读取
# readlines
#lines = f.readlines()   # 读取文件的全部行，封装到列表中
#print(f"lines对象的类型：{type(lines)}")
#print(f"lines对象的内容是：{lines}")   # readline也会续接之前的read
# readline
#line1 = f.readline()    # 一次读一行
#line2 = f.readline()
#line3 = f.readline()
#print(f"第一行数据是：{line1}")
#print(f"第二行数据是：{line2}")
#print(f"第三行数据是：{line3}")
# for循环读取文件行
#for line in f:
#    print(f"每一行数据是：{line}")
# 文件的关闭
#f.close()
# 上下文管理器
# 通过with open语法可以自动关闭
#with open("D:\桌面desktop\数据结构_py\数学建模知识点.txt","r",encoding="UTF-8") as f:
#    for line in f:
#        print(f"每一行数据是：{line}")
# 练习案例：单词计数
# read()读取，count()对读取到的字符串进行统计

# 写文件
"""
'w'：如果原来没有文件，会创造一个新文件；如果原来有文件，会把原文件内容覆盖掉
"""
import time
#f = open("D:\桌面desktop\数据结构_py\pytest.txt","w",encoding="UTF-8")
# write写入
#f.write("Hello World!")
#time.sleep(50000)       # 判断程序是否把之前的运行完了
# flush刷新
#f.flush()              # 把刚写入内存中的内容，刷新到硬盘里
# close关闭
#f.close()               # close自带flush功能

# 追加
"""
f = open("D:\桌面desktop\数据结构_py\pytest.txt","a",encoding="UTF-8")
f.write("\nGoodbye World.")         # 换一行
f.close()
"""

# 练习案例
"""
读取文件，将文件写出到bill.txt.bak文件作为备份,将文件内标记为测试的数据行丢弃
"""
f1 = open(r"D:\pill.txt","r",encoding = "UTF-8")
f2 = open(r"D:\pill.txt.bak","w",encoding="UTF-8")


for line in f1:
    line = line.strip()
    if line.count("测试") == 1:
        continue
    f2.write(line)
    f2.write("\n")
f1.close()
f2.close()
