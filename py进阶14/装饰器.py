"""
什么是装饰器
装饰器就是使用创建一个闭包函数，在闭包函数内调用目标函数
可以达到不改变目标函数的同时，增加额外内容的功能

装饰器的写法
def outer(func:)

    def inner():
        print("内容1")
        func()
        print("内容2")

    return inner

@outer
def hello():
    print("hello world!")

hello()
"""
def outer(func):

    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner
# 使用装饰器方法1
# def sleep():
#     import time
#     import random
#     print("睡眠中")
#     time.sleep(random.randint(1,10))


# fn = outer(sleep)
# fn()

# 方法2:语法糖
@outer
def sleep():
    import time
    import random
    print("睡眠中")
    time.sleep(random.randint(1,10))

sleep()