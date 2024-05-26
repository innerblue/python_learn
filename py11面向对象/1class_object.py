# 使用对象组织数据
"""
程序中可以像生活中一样以设计表格、生产表格、填写表格的组织形式来进行
class Student:      # 在程序中设计表格，称为：设计类——也可以类比零件、结构体啥的
    name = None
基于类创建对象：       # 在程序中打印生产表格，称为：创建对象
stu_1 = Student()
stu_2 = Student()
# 在程序中填写表格，称为：对象属性赋值
stu_1.name = "wjy"  # 为学生1对象赋予名称属性值
stu_2.name = "scx"  # 为学生2对象赋予名称属性值
"""
# 设计一个类
class Student:
    name = None             # 记录学生姓名
    gender = None           # 记录学生性别
    nationality = None      # 记录学生国籍
    native_place = None     # 记录学生籍贯
    age = None              # 记录学生年龄
# 创建一个对象
stu_1 = Student()
# 对象属性赋值(相当于给类里的变量赋值)
stu_1.name = "wjj"
stu_1.gender = "女"
stu_1.nationality = "中国"
stu_1.native_place = "河北"
stu_1.age = 20

print(stu_1.name)   # 可以输出，以此类推...

# 类的定义和使用
"""
class 类名称：      # class关键字定义类
    类的属性        # 类的属性，及定义在类中的变量（成员变量）
    
    类的方法        # 类的方法，及定义在类中的方法（成员方法）
创建类对象的语法：对象 = 类名称
成员方法的定义语法：
def 方法名(self,形参1,...,形参n):
    方法体
self关键字：（成员方法定义时必须填写）
他表示类对象自身
当我们使用类对象调用方法时，self会自动被python传入
在方法内部，想要访问类的成员变量，就必须通过self
self尽管在参数列表中，但传参时可以忽略它
"""
class Student:
    name = None
    def func_nm(self):
        print(f"大家好啊，我是{self.name}！")
    def func_nm2(self,msg):
        print(f"大家好，我是{self.name},{msg}")   # 调用内部变量要用self，这里没事干是外部传入的，不需要用self

stu_1 = Student()
stu_1.name = "说的道理"
stu_1.func_nm()

stu_2 = Student()
stu_2.name = "otto"
stu_2.func_nm()

# 类和对象
"""
类和对象的关系：
类是程序中的设计图纸，
对象是基于图纸生产的具体实体
"""
# 构造方法
"""
__init__()方法，称为构造方法
"""
class Student:
    def __init__(self,name,age,tel):
        self.name = name        # 将外部传入的参数赋值给内部的变量
        self.age = age          # 这个语句声明变量同时给变量赋值，即具备定义和赋值的功能
        self.tel = tel
        print("----测试运行----")

stu_1 = Student("otto",20,11111111111)
print(stu_1.name)

# 练习案例
"""
开学了有一批学生信息要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址这3类信息
请实现：
通过for循环，配合input语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，使用print语句，完成信息的输出
"""
class student:
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr
        self.msg_dict = {"学生姓名": name, "年龄": age, "地址": addr}

def main_stu(num):
    for i in range(1,num+1):
        print(f"当前录入第{i}位学生信息，总共录入10位学生信息")
        nm = input("请输入学生姓名：")
        ag = int(input("请输入学生年龄:"))
        ad = input("请输入学生地址：")
        stu = student(nm, ag, ad)
        print(f"学生{i}信息录入完成，信息为：{stu.msg_dict}")

# 魔术方法
"""
__init__：构造方法，__str__：字符串方法，__lt__：<、>符号比较，__le__：<=、>=符号比较，__eq__：==符号比较
"""
# __str__字符串方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):              # 类对象返回字符串
        return f"Student类对象：name:{self.name},age:{self.age}"
    def __lt__(self,other):         # other表示另外一个用于比较的类对象
        return self.age < other.age
    def __le__(self,other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age

stu_1 = Student("小A",24)
stu_2 = Student("小B",28)
print(stu_1)
print(stu_1 < stu_2)
print(stu_1 <= stu_2)
print(stu_1 == stu_2)
print(stu_1.__lt__(stu_2))      # 相当于上面的print(stu_1 < stu_2)
# 封装
"""
面向对象编程：基于模板（类）去创建实体（对象），使用对象完成功能开发
面向对象包含三大主要特征：封装，继承，多态
封装：将现实世界事物的 属性、行为 封装到类中，描述为：成员变量、成员方法
"""
# 定义一个类，内含私有成员变量和私有成员方法
class Phone:

    __current_voltage = 0.5    # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为省电模式")
phone = Phone()
#print(phone.__current_voltage)
#print(phone.__keep_single_core(self))      # 私有成员变量和方法都无法被类对象使用
phone.call_by_5g()      # 类对象无法访问私有成员，但类中其他成员可以访问私有成员（相当于“仅对内部人员开放”）
# 练习案例:设计带有私有成员的手机
"""
设计一个手机类，内部包含：
私有成员变量：__is_5g_enable,类型bool，True表示开启5g，False表示关闭5g
私有成员方法：__check_5g(),会判断私有成员__id_5g_enable的值：
    若为True，输出：5g开启
    若为False，输出：5g关闭，使用4g网络
公开成员方法：call_by_5g(),调用它会执行:
    调用私有成员方法：__check_5g(),判断5g网络状态
    打印输出：正在通话中
运行结果：5g关闭，使用4g网络
        正在通话中
"""
class Phone:

    __is_5g_enable = False
    def __check_5g(self,msg):
        self.__is_5g_enable = msg
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
    def call_by_5g(self,msg):
        self.__check_5g(msg)
        print("正在通话中")

# my_phone = Phone()
# my_phone.call_by_5g(False)

# 继承（详见inherit.py）