# 多线程并行执行概念
"""
什么是进程：
程序在操作系统内运行，即成为一个运行进程

什么是线程：
进程内部可以有多个线程，程序的运行本质就是由进程内部的线程实际工作的

什么是多线程执行：
多个进程同时在运行，即不同的程序同时运行，称之为多任务并行执行
一个进程内的多个线程同时在运行，称之为多线程并行执行
"""

# 多线程编程
"""
threading模块的使用：
thread_obj = threading.Thread(target = func)创建线程对象
thread_obj.start()启动线程执行

传参：
thread_obj = threading.Thread([group [,target [,name [,args [,kwargs]]]]])
group：暂时无用，未来功能的预留参数
target：执行的目标任务名
args：以元组的方式给执行任务传参
kwargs：以字典的方式给执行任务传参
"""
import time
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

# 单线程
if __name__ == '__main__':
   # sing()
   # dance()
   import threading
   # 创建一个唱歌的线程
   sing_thread = threading.Thread(target=sing,args=("我在唱歌",))   # 只有一个元素的元组后面必须接逗号
   # 创建一个跳舞的线程
   dance_thread = threading.Thread(target=dance,kwargs={"msg":"我在跳舞"})
   # 让线程去干活
   sing_thread.start()
   dance_thread.start()