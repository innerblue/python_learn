"""布尔类型
布尔类型的字面量：True表示真，False表示假
定义变量存储布尔类型：变量名称 = 布尔类型字面量
布尔类型的数据也可以通过比较运算符进行内容比较得到"""
bool_1 = True
bool_2 = False
print(f"bool_1的内容是:{bool_1},类型是{type(bool_1)}")
print(f"bool_2的内容是:{bool_2},类型是{type(bool_2)}")

result = 3 > 2
print(f"3 > 2的结果是:{result},输出数据类型是:{type(result)}")
# 比较运算符：==,<,>,!=,<=,>=
num_1 = 2
num_2 = 3
print(f"2 == 3的结果是：{num_1 == num_2}")
print(f"2 >= 3的结果是：{num_1 >= num_2}")
print(f"2 <= 3的结果是：{num_1 <= num_2}")
print(f"2 != 3的结果是：{num_1 != num_2}")

# if，if else，if elif else 语句
"""if语句格式：
if 要判断的条件：
    条件成立时要做的事"""
# if else 语句
#age = input("你的年龄是？")
#age = int(age)
#if age >= 18:
#    print("我已经成年了。")
#    print("时光飞逝。 :(")
#else:
#    print("好想快点长大。")

#stature = int(input("您的身高是？"))
#if stature >= 120:
#    print("您的升高高于120cm，请购买成人票，祝您游玩愉快！")
#else:
#    print("您的身高低于120cm，可以免费游玩，祝您游玩愉快！")
# if elif else 语句
#height = int(input("您的身高是？"))
#VIP_level = int(input("您的VIP级别是？"))
#if height <= 120:
#    print("身高小于120cm，可以免费进入")
#elif VIP_level >= 3:
#    print("vip级别大于等于3级，可以免费进入")
#else:
#    print("您需要购票并出示")
"""多条件判断中，条件之间是互斥的，即如果满足if的条件，则elif就没用了，即从上到下挨个判断;
elif 语句可以写多个;如果不写else，则elif语句就相当于独立的if语句"""
"""
height = int(input("您的身高是？"))
VIP_level = int(input("您的VIP级别是？"))
if height <= 120:
    print("身高小于120cm，可以免费进入")
elif VIP_level >= 3:
    print("vip级别大于等于3级，可以免费进入")
#else:
    #print("您需要购票并出示")"""

""" input也可以直接写入判断条件中,如:
if int(input("您的身高是？")) <= 120:
    print("身高小于120cm，可以免费进入")
elif int(input("您的VIP级别是？")) >= 3:
    print("vip级别大于等于3级，可以免费进入")
else:
    print("您需要购票并出示")"""

"""判断语句的嵌套
if 条件1:
    满足条件1 做的事情1
    满足条件1 做的事情2
    if 条件2:
        满足条件2 做的事情1
        满足条件2 做的事情2
        （只有第一个if满足条件，才会执行第2个if）"""
#if int(input("您的身高是：")) >= 120:
 #   print("身高超限，无法享受儿童优惠套餐。如果您的VIP等级是2级及以上，可以享受VIP优惠")
 #   if int(input("您的VIP等级是：")) >= 3:
  #      print("恭喜，您可以享受VIP优惠")
   # else:
    #    pirnt("不好意思，您无法享受VIP优惠")
#else:
 #   print("可以享受儿童优惠，祝您游玩愉快！")   # 双层次的if嵌套。一定要注意缩进，缩进决定层次关系

#age = 20
#year = 1
#level = 3
#if age >= 18:
#    print("你是成年人")
#    if age <= 30:
#        print("你的年龄达标了")
#        if year >= 2:
#            print("恭喜，年龄和入职时间都达标，可以领取礼物")
#       elif level > 3:
#            print("恭喜，年龄和等级达标，可以领取礼物")
#       else:
#            print("不好意思，尽管年龄达标，但入职时间和级别不够，无法领取礼物")
#    else:
#        print("不好意思，你的年龄超过了，无法领取礼物")
#else:
#    print("年龄不够，无法领取礼物")

#import random
#num = random.randint(1,10)
#num_guess = int(input("请输入你猜测的数字："))
#if num_guess == num:
#    print("恭喜，第一次就猜对了")
#else:
#    if num_guess > num:
#        print("你猜大了，请再次猜测")
#    else:
#        print("你猜小了，请再次猜测")
#    num_guess = int(input("请输入你第二次猜测的数字："))

#    if num_guess == num:
#        print("恭喜，第二次猜对了")
#        else:
#        if num_guess > num:
#            print("你猜大了，请再次猜测")
#        else:
#            print("你猜小了，请再次猜测")
#        num_guess = int(input("请输入你第三次猜测的数字："))

#        if num_guess == num:
#            print("恭喜，第三次猜对了")
#        else:
#            print("对不起，你猜错了，所有机会已用完")



