#from my_module1 import test1
#test1(1,2)

# __main__变量
"""
__main__变量可以让我们在自定义模块中测试函数，否则在调用模块时会将该模块中的测试结果输出
__all__变量可以控制使用import *时那些功能可以被导入
"""
# 导入自定义包中的模块并使用
# 方法一
# import my_package1.a_module
# import my_package1.b_module
#  调用函数
# my_package1.a_module.info_print1()
# my_package1.b_module.info_print2()

# 方法二
# from my_package1 import a_module
# from my_package1 import b_module
# 调用函数
# a_module.info_print1()
# b_module.info_print2()

# 方法三
# from my_package1.a_module import info_print1
# from my_package1.b_module import info_print2
# 调用函数
# info_print1()
# info_print2()

# 通过__all__变量，控制import *
# from my_package1 import *
# a_module.info_print1()      # 只能导入a_module
# b_module.info_print2()
