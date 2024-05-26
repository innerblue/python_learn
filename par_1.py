# 注释 练习
"""
-你好世界！
-晚安世界。
"""
print("Hello World!")
print("Goodnight World.")
# 变量 练习
fingers = 10
print("手指头有",fingers,"根")

# 数据类型 练习
print(type("hello world!"))
print(type(666))
name = "wang"
name_type = type(name)
print(name)
print(name_type)

# 数据类型转换 练习
number_str = str(24)
print(type(number_str),number_str)
float_str = str(114.514)
print(type(float_str),float_str)
number_2 = int("11")
print(type(number_2),number_2)
number_3 = float("114.514")
print(type(number_3),number_3)
"""
错误案例:
number4=int("Hello World!")
print(type(number4),number4)
文字无法转成数
"""
# 整数转浮点数
num5 = float(24)
print(type(num5),num5)
# 浮点数转整数
num6=int(114.514)
print(type(num6),num6)

# 标识符 练习
"""
1、内容限定，只能：英文，中文，数字，下划线（不推荐用中文，不能用数字开头）
错误案例：1_number = 24
2、大小写敏感
3、不可使用关键字
错误案例：False = 3
"""
# 运算符 练习
# 1、标准赋值
print("1+1 =",1+1)
print("2-1 =",2-1)
print("2*3 =",2*3)     # 乘法
print("6/3 =",6/3)     # 除法
print("5//2 =",5//2)   # 除法取整
print("5%2 =",5%2)     # 取余数
print("3**3 =",3**3)    # 指数（3的3次方；同理，3**2即为3的2次方）
# 2、复合赋值
num = 1
num += 1    # 等同于：num = num + 1
print("num += 1: ",num)
num -= 1
print("num -= 1: ",num)
num *= 4    # 等同于num = num * 4
print("num *= 4: ",num)
num /= 2
print("num /= 2: ",num)
num = 7    # 重新给num赋值，因为之前的结果我忘了，，
num //= 2
print("num //= 2: ",num)
num %= 2
print("num %= 2: ",num)

"""
字符串的三种定义方式 
name = 'Wang'
name = "Wang"
"""
# name = """Wang"""
name = """Wang"""
print(type(name),name)
# 字符串内包含双引号
name = '"Wang"'
print(name)
# 字符串内包含单引号
name = "'Wang'"
print(name)
# 使用转义字符\解除引号的效用
# name = "Wang"",如此定义会导致报错，使用转义字符\使后面的一个引号失效；name = ''Wang'' 同理
name = "Wang\""     # \是转义他后面的引号
name_2 = "\"Liu\""
name_3 = '\'Li\''

# 字符串拼接，用+号，比如字面量和变量拼接；但仅字符串之间，无法和其他格式如此拼接,如想与数字拼接，需要改变格式
name = "wjy"
age = str(20)
print("Hello everyone,my name is "+name+",and I am "+age+" years old.")
# 字符串格式化，变量拼接
name = "朝夕家园"
message = "工人子女托管班，找%s"%name    # 第一种字符串格式化方式：%s 表示把变量变成字符串的格式放到占位的位置
print(message)
name_2 ="wjy"
age = 20
message_2 = "Hello everyone,my name is %s,and I am %s years old."%(name_2,age)
print(message_2)
# %s:把变量变成字符串类型占位； %d：把变量变成整数类型占位； %f:把变量变成浮点数类型占位
# 字符串格式化之数字精度控制
# %5d 表示将整数宽度控制在5位；%5.2f表示将小数宽度控制在5位，小数点精度设置为2；%.2f表示不控制宽度，只设置小数点精度为2
num_1 = 114
num_2 = 114.514
print("将整数宽度控制为5，输出：%5d"%num_1)
print("将小数宽度控制为7，精度设置为2，输出：%7.2f"%num_2)    # 精度部分会对小数作四舍五入
# 如果宽度限制比数字本身的宽度还小，则宽度控制不生效，如：
print("将整数宽度控制为2，输出：%2d"%num_1)     # 输出结果为114
# 第二种字符串格式化方式：f"{占位}"
name_mine = "wjy"
age_mine = 24
stature_mine = 172.5    # 不同于%的方式，这种方式既不关心类型也不进行精度控制
print(f"Hello,everyone,I am {name_mine},and I am {age_mine},{stature_mine} high.")
"""对表达式进行格式化
1.了解什么是表达式
2.对表达式进行字符串格式化"""
# 表达式：一条具有明确执行结果的代码语句
print("算式 2*3 的结果是：%d"%(2*3))
print(f"算式 2*3 的结果是：{2*3}")
print("字符串在python中的类型名是：%s"%type("字符串"))
# 数据输入 input（）语句
name = input("你的名字是？")
print("早上好，%s!"%name)
age = input("请问你今年几岁？")
age = int(age)
print("哦，你今年%s岁,你年龄的类型是：%s"%(age,type(age)))
# 使用 input 无论输入什么类型的数据，获取到的数据永远是字符串，除非使用数据类型转换
