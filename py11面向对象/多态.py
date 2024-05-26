# 多态
"""
1、什么是多态
多态指的是，同一个行为，使用不同的对象获得不同的状态
如：定义函数（方法），通过类型注解声明需要父类对象，实际传入子类对象进行工作，从而获得不同的工作状态

多态常作用在继承关系上，比如：
函数（方法）形参声明接收父类对象
实际传入父类的子类对象进行工作
即：以父类做定义声明，以子类做实际工作
用以获得统一行为不同状态

2、什么是抽象类（接口）
包含抽象方法的类，称为抽象类。抽象方法指的是：没有具体实现的方法（pass），称之为抽象方法

3、抽象类的作用
多用于做顶层设计（设计标准），以便子类做具体实现
也是对子类的一种软性约束要求子类必须复写（实现）父类的一些方法
并且配合多态使用，就能获得不同的工作状态
"""
class AC:
    def cold_wind(self):    # 抽象类
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_sw(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cold_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_sw(self):
        print("美的空调摆风")

class GREE_AC(AC):
    def cold_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_sw(self):
        print("格力空调摆风")

# 多态
def make_cool(ac:AC):
    ac.cold_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()
make_cool(midea_ac)

# 综合案例（详见objcls_case.py）