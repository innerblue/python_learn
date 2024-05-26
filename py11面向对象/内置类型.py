"""
对象的3个特征：
1、唯一标识符
2、类型
3、值
"""
a = 1
print(id(a))
print(type(a))
print(a)

def func():
    pass

print(id(func))
print(type(func))
print(func)     # 输出的是一种函数的表现形式（相当于一个具体的值）

class mycls:
    pass

print(id(mycls))
print(type(mycls))
print(mycls)    # 输出的是类对象的表现形式

# None类型
data1 = None
data2 = None
print(id(data1)==id(data2))     # 返回True，说明None类型全局只有一个
"""
python中常见的内置类型:
数值:int,float,complex,bool
迭代
序列:列表,字节、字节数组、内存视图，元组，字符串，数组
映射：字典
集合：普通集合，有序集合
上下文管理类型（with）
其他
"""