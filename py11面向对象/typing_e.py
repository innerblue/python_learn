# 类型注解
"""
作用：
帮助开发工具对代码做类型推断协助做代码提示
开发者自身做类型的备注
类型注解支持：
变量的类型注解
函数（方法）的形参和返回值的类型注解
变量的类型注解语法：
1、变量：类型
2、在注释中：# type：类型
注意：
类型注解只是提示性的，非决定性的。数据类型和注解类型无法对应也不会报错
"""
# 基础数据类型注解
var_1:int = 10
var_2:str = "hello"
var_3:bool = True
# 类对象类型注解
class Student:
    pass
stu:Student = Student()
# 基础容器类型注解
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {"test":98}
# 容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool] = (1,"hello",True)
my_dict:dict[str,int] = {"test":98}
# 在注释中进行类型注解
import random
import json
var_1 = random.randint(1,10)    # type:int
var_2 = json.loads('{"name":"wjy"}')    # type:dict[str,str]
def func():
    return 10

var_3 = func()  # type:int
# 一般，无法直接看出变量类型时才写类型注解

# 函数和方法的类型注解
"""
函数（方法）添加类型注解：
形参的类型注解
返回值的类型注解
函数（方法）的类型注解语法:
def 函数（方法）名(形参:类型,...,形参:类型) -> 返回值类型:
    函数体 
"""
# 对参数进行类型注解
def add(x:int,y:int):
    return x + y
# 对函数返回值进行类型注解
def func(data:list) -> list:
    return data

# Union联合类型注解
# 导包
from typing import Union
my_list:list[Union[int,str]] = [1,2,"abc"]    # Union[int,str]表示要么是int类型，要么是str类型
my_dict:dict[str,Union[str,int]] = {"name":"ecx","age":17}  # 表示key都是str，value要么str要么int
def func(data: Union[int,str]) -> Union[int,str]:
    return data
# print(func(10))

# 多态（详见多态.py）