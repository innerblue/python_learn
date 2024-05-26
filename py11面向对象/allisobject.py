"""
python中，对象（object）是指在内存中具有唯一标识符、类型和值的实例
换句话说，他是一个具有属性和方法的实体，这些属性和方法可以被访问和操作
"""
# 唯一标识符其实是内存地址
num = 10
print(id(num))

def print_info(name):
    print(name)

print(id(print_info))       # 注意不要带上括号，带括号是调用函数
my_func = print_info        # 对象其实就是保存在内存中的一段数据，对象可以用变量接收
my_func("张维为")
# 声明一个类
class Person:
    def __init__(self):
        print("维维豆奶")

print(id(Person))
my_cls = Person
my_cls()        # 进行实例化
# 将上面的函数对象和类对象添加到数据容器中
obj_list = list()
obj_list.append(print_info)
obj_list.append(Person)
for item in obj_list:
    print(item)
# 通过装饰器的方式讲解函数作为一个参数进行传递以及返回一个函数对象
def my_wrapper(func_obj):   # 把外部函数对象拿到内部函数进行一次调用
    def wrapper():
        print("这是一个装饰器")
        func_obj()          # 调用外部函数接收到的函数对象
    return wrapper        # 外部函数返回的是内部函数对象/引用

# 装饰器用法(和下面注释掉的那个用法效果是一样的)：
@my_wrapper
def print_wrapper():
    print("这是一个测试函数")
print_wrapper()
# 将定义的普通函数传递给my_wrapper
# func_obj = my_wrapper(print_wrapper)
# func_obj()

# type object class的关系
a = 1
b = ("abc")
# type可以判断一个对象的类型，并且type也可以用于创建类
print(type(a))
# 一切皆对象，对象是由类创建出来的
print(type(int))    # a是整型，是由class int这个类创建出来的，而int这个类型又是由type创建出来的
"""
python中的数据类型是由类型类创建出来的
python中的类型是由type创建出来的
python中所有对象都是由type创建的
"""
# 探究对象是被谁创建的
# 创建一个类
class Student:
    pass
# 实例化
stu = Student()
print(type(stu))    # 作为Student的实例，stu是被Student创建的

class MyStudent(Student):      # 创建一个类来继承Student
    pass
my_stu = MyStudent()
print(type(my_stu))
print(type(MyStudent))

# 探究object（python中object是所有类的基类）
print(int.__bases__)        # 该方法用于查询一个类的继承关系
print(str.__bases__)
print(Student.__bases__)    # python3中，自定义的类如果没写继承关系默认继承object
print(MyStudent.__bases__)

print(type(object))     # object基类也是被type创建的
print(type.__bases__)   # 可以看出type继承了object
print(object.__bases__) # object是最底层的基类，它没继承任何的类
print(type(type))       # type是由自身创建的

"""
总结：
1、type创建了所有对象，也包括了类对象（object）
2、type创建object基类同时也继承了object
3、type是由自身创建的
"""
