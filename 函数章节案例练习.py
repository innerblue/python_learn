# 查询，存取款小程序
# 我的答案（未完成）
#money = 5000000
#name = input("请输入您的姓名")
#def check_cash():
#   """
#   该函数用于查询余额
#    :return:
#   """
#    print(f"您当前余额为{money}元")
#def save_cash(x):
#    """
#    该函数用于存钱
#    :param x: 代表存入的钱的数目
#    :return:
#    """
#   global money
#    money += x
#    print(f"您已存入{x}元")
#    check_cash()
#def draw_money(y):
#    """
#    该函数用于取钱
#   :param y: 代表取出的钱的数目
#   :return:
#    """
#    global money
#   money -= y
#   print(f"您已取出{y}元")
#    check_cash()
#def main_menu():

# 标准答案
# 定义全局变量
money = 5000000
name = None     # 待会再要求输入，先赋予一个没有意义的初值
# 要求客户输入姓名
name = input("请输入您的姓名：")
# 定义查询函数
def query(show_header):
    """
    查询存款
    :param show_header:代表“查询余额”这一标头
    :return:
    """
    if show_header:     # show_header等会输入布尔值，True进入if循环，False不进入
        print("-------查询余额-------")
    print(f"{name},您好，您的余额剩余{money}元")

# 定义存款函数
def saving(num):
    global money
    money += num
    print("-------存款-------")
    print(f"{name},您好，您存款{num}元成功")

    query(False)    # 存款结束后查询余额，调用query()函数，输入False意味着不进入query()中的if循环，即不输出标头“查询余额”
def get_money(num):
    global money
    money -= num
    print("-------取款-------")
    print(f"{name},您好，您取款{num}元成功")

    query(False)
def main_menu():
    print("-------主菜单-------")
    print(f"{name}，您好，欢迎来到xxx银行ATM,请选择操作：")
    print("查询余额\t[输入1]")    # \t对齐输出
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("输入您的选择：")
# 设置无限循环，确保程序不没事儿就退出
while True:     # 这就代表无限循环
    keyboard_input = int(main_menu())
    if keyboard_input == 1:
        query(True)
        continue    # 用continue结束本次循环，进入下一次循环，回到主菜单
    elif keyboard_input == 2:
        num = int(input("您要存多少钱；"))
        saving(num)
        continue
    elif keyboard_input == 3:
        num = int(input("您要取多少钱；"))
        get_money(num)
        continue
    else:
        print("程序已退出")
        break       # 用break退出循环


