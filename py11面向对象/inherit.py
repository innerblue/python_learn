# 继承
"""
class 类名(父类名):
    类内容体
继承分为多继承、单继承
"""
# 单继承
class Phone:
    IMEI = None         # 序列号
    producer = "XM"     # 厂商
    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10000"
    def call_by_5g(self):
        print("2022新功能，5g通话")

# phone = Phone2022()
# print(phone.IMEI)
# print(phone.call_by_4g())
# print(phone.face_id)
# print(phone.call_by_5g())     # 都可以输出

# 多继承
class NFCreader:    # 读卡器
    nfc_type = "第五代"
    producer = "AM"
    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class Remote_control:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone,NFCreader,Remote_control):
    pass                    # pass补全空白

phone1 = MyPhone()
print(phone1.producer)     # 多个父类中，如果有同名的成员，继承顺序按从左到右为优先级
print(phone1.control())    # （先继承的保留，后继承的被覆盖）

# 复写父类成员和调用父类成员
"""
复写表示：对父类的成员属性或成员方法进行重新定义
复写的语法：在子类中重新实现同名成员属性或成员方法即可
在子类中如何调用父类成员：
1、调用父类成员：
使用成员变量：父类名.成员变量
使用成员方法：父类名.成员方法(self)
2、使用super()调用父类成员
使用成员变量：super().成员变量
使用成员方法：super().成员方法()
注意：只可以在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写的
"""
class Phone:
    IMEI = None         # 序列号
    producer = "XM"     # 厂商
    def call_by_5g(self):
        print("使用5g进行通话")

class MyPhone(Phone):
    producer = "SM"
    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 方式1（子类中调用父类）
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
print(phone.producer)
phone.call_by_5g()
# 在子类中调用父类成员(参考伤面子类的内容)

# 类型注解（详见typing_e.py）
