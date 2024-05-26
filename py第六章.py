"""数据容器：
一种可以容纳多份数据的数据类型，容纳的每一份数据称为元素
每一个容器可以是任意类型的数据，如字符串，数字，布尔等
数据容器根据特点的不同，如：
是否可以支持重复元素
是否可以修改
是否有序，等
分为五类：
列表，元组，字符串，集合，字典
"""
# 列表（list）
a_list = ["wjyzd",123456,False]     # 元素是字符串，数字，布尔都行
print(a_list)
print(type(a_list))
b_list = [[1,2,3],[2,3,4],[3,4,5]]
print(b_list)
print(type(b_list))
# 列表的下标索引
a_list = ["wjyzd",123456,False]
print(a_list[0])    # 从前向后，编号从0开始递增
print(a_list[1])
print(a_list[2])    # 错误示范：print(a_list[3]).下标索引注意不要超出范围
print(a_list[-1])   # 从后往前，编号从-1开始递减
print(a_list[-2])
print(a_list[-3])
# 嵌套列表的下标索引
b_list = [[1,2,3],[2,3,4],[3,4,5]]
# 取外层列表第二个元素（即第二个内层列表）的第二个元素
print(b_list[1][1])
# 取外层列表第三个元素（即第三个内层列表）的第三个元素
print(b_list[-1][-1])
# 列表的常用操作
# 列表的方法
"""
方法的概念:方法和函数功能一样，有传入参数，有返回值，只是方法的使用格式不同
函数的使用：num = add(1,2
方法的使用：student = Student()
          num = student.add(1,2)  """
# 查询某元素的下标，使用index方法
a_list = ["wjyzd",123456,False]
index = a_list.index(123456)
print(f"123456在列表a_list中的下标索引值是：{index}")
# 修改特定下标索引的值
a_list[1] = "fdf"
print(f"列表被修改元素值后，结果是{a_list}")
# 在指定下标位置插入新元素
a_list.insert(2,"best")
print(f"列表插入新元素后，结果是{a_list}")
# 在列表尾部追加（单个）新元素
a_list.append("bjd")
print(f"列表插入新元素后，结果是{a_list}")
# 在列表尾部追加（一批）新元素
b_list = [1,2,3]
a_list.extend(b_list)
print(f"列表追加一批新元素后，结果是{a_list}")
# 删除元素
# 1.del 列表[下标]
a_list = ["wjyzd", 123456, False]     # 重新赋值
del a_list[2]
print(f"列表删除元素后结果是{a_list}")
# 2.列表.pop(下标)
a_list = ["wjyzd",123456,False]     # 重新赋值
element = a_list.pop(1)
print(f"通过pop取出元素后列表：{a_list}，取出的元素{element}")
# 列表.remove(元素)
a_list = ["wjyzd",123456,False,False,123456]    # 重新赋值
a_list.remove(123456)
print(f"通过remove方法移除元素后，列表的结果是:{a_list}")   # 移除的是从左往右第一个指定元素
# 清空列表
a_list.clear()
print(f"列表清空了，结果是{a_list}")
# 统计某元素在列表中的数量
#列表.count(元素)
a_list = ["wjyzd",123456,False,False,123456]
count = a_list.count(123456)
print(f"列表中元素123456的数量是{count}")
# 统计列表中全部的元素数量
a_list = ["wjyzd",123456,False,False,123456]
count = len(a_list)
print(f"列表中有{count}个元素")
# 练习
c_list = [21,25,21,23,22,20]
c_list.append(31)
print(c_list)
d_list = [29,33,30]
c_list.extend(d_list)
print(c_list)
element1 = c_list.pop(0)
print(f"取出列表第一个元素:{element1}")      # 标准答案：num1 = c_list[0]
element2 = c_list.pop(-1)
print(f"取出列表最后一个元素:{element2}")     # 标准答案：num2 = c_list[-1]
index = c_list.index(31)
print(f"元素31在列表中的下标位置:{index}")
print(c_list)
# 列表的循环遍历(将数据容器内的元素依次取出并处理，就叫遍历)
# 1.while循环遍历
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    a_list = ["传智教育","黑马程序员","python"]
    index = 0
    while index < len(a_list):  # 循环条件：下标索引变量 < 列表的元素数量;len函数表示列表长度
        element = a_list[index]
        print(f"列表的元素:{element}")
        index += 1
# 2.for循环遍历
def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    a_list = [1,2,3,4,5]
    # for 临时变量 in 数据容器:
    for element in a_list:
        print(f"列表的元素:{element}")
"""for循环和while循环对比:
1.for更简单，while更灵活
2.for用于从容器内依次取出元素并处理，while用于任何需要循环的场景"""
# 元组tuple
# 元组和列表的区别：列表可以修改，元组一旦定义完成，就不可修改
t1 = (1,"hello",True)   # 元素是字符串，数字，布尔都行（同列表）
# 定义空元组
t2 = ()
t3 = tuple()
# 定义单个元素的元组
t4 = ("hello",)     # 后面必须单独加一个逗号
# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
# 下标索引取出内容
print(t5[1][-1])
# 元组的相关操作
# 1.index查找
t6 = ("hello","bye","yes")
index = t6.index("hello")
print(f"列表t6中元素hello的下标是：{index}")   # 下标是0
# 2.count统计
t7 = ("hello","bye","yes","bye","python","java","c++")
num = t7.count("bye")
print(f"在列表t7中统计元素bye的数量：{num}")
# 3.len函数统计元组元素数量
t8 = ("hello","bye","yes","bye","python","java","c++")
num = len(t8)
print(f"t8元组中的元素有 {num} 个")
# 元祖的遍历：while和for循环
# 1.while循环遍历
index = 0
while index < len(t8):
    element = t8[index]
    print(f"元组t8的元素有:{element}")
    index += 1
print()     # 和以下for的结果隔开
# 2.for循环遍历
for element in t8:
    print(f"元组t8的元素有{element}")

# 元组本身不可修改（不能增加，删改元素），但可以修改其内部的列表
t9 = ("wjy","me",[123,456])
t9[2][0] = True
t9[2][1] = False
print(t9)
print()
# 练习案例：定义一个元组:('周杰轮'，11，['football','music']),记录的是一个学生的信息（姓名，年龄，爱好）
"""
1.查询年龄所在的下标位置
2.查询学生的姓名
3.删除学生爱好中的football
4.增加爱好：coding到爱好list内"""
tuple_student = ('周杰轮',11,['football','music'])
index_age = tuple_student.index(11)
print(f"元组中年龄元素的下标:{index_age}")
index_name = tuple_student.index('周杰轮')
print(f"元组中姓名元素的下标:{index_name}")
tuple_student[2].remove('football')
tuple_student[2].append('coding')
print(tuple_student)
print()
# 字符串的定义和操作
# 字符串也是数据容器，可以存放多个字符
# 字符串的下标索引（和列表、元组一样，从左往右从0开始；从右往左从-1开始）
a_str = "Yo soy un hombre"
# 通过下标索引取值
value1 = a_str[1]
value2 = a_str[-5]   # 取"o"字符
print(f"从字符串{a_str}中取下标为1的元素:{value1},下标为-5的元素:{value2}")
# 同元组一样，字符串是无法修改的
# 查询下标
# index方法
index = a_str.index("soy")
print(f"在字符串{a_str}中 soy 的下标:{index}")
# 字符串的替换
# replace方法
"""
语法:字符串.replace(字符串1，字符串2)
功能:将字符串内的全部：字符串1，替换为字符串2
不是修改了字符串，而是得到了一个新的字符串"""
new_a_str = a_str.replace("soy","是")
print(f"将字符串{a_str}进行替换后得到：{new_a_str}")
# 字符串的分割
# split方法
"""
语法:字符串.split(分隔符字符串)
功能:按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
字符串本身不变，而是得到了一个新的列表对象"""
a_str = "la mujer el hombre"
a_str_list = a_str.split(" ")
print(f"将字符串进行split分割后得到列表{a_str_list},类型是{type(a_str_list)}")
# 字符串的规整方法
# strip方法
# 1.去前后空格
"""语法:字符串.strip()"""
# 2.去前后指定字符串
"""语法:字符串.strip(字符串)"""
a_str = "  la mujer el hombre  "
b_str = a_str.strip()   # 不传入参数，去除首尾空格
print(f"字符串{a_str}被strip后:{b_str}")
print()
a_str = "12la mujer el hombre21"
b_str = a_str.strip("12")   # 这里去除的是字符串"1"和"2"
print(f"字符串{a_str}被strip后:{b_str}")
# 统计字符串中某字符串出现的次数
a_str = "la mujer el hombre"
num = a_str.count("e")
print(f"字符串{a_str}中字符串e出现了{num}次")
# 统计字符串的长度
num = len(a_str)
print(f"字符串{a_str}的长度：{num}")
# 字符串的遍历：while和for循环
index = 0
while index < len(a_str):
    element = a_str[index]
    index += 1
    print(f"字符串{a_str}的元素：{element}")
for element in a_str:
    print(f"字符串{a_str}的元素：{element}")
# 练习案例
"""给定一个字符串："itheima itcast boxuegu"
统计字符串有多少个"it"字符
将字符串内的空格，全部替换为"|"
并按照"|"进行分割，得到列表"""
b_str = "itheima itcast boxuegu"
num = b_str.count("it")
print(f"字符串{b_str}中，有{num}个it字符")
new_b_str = b_str.replace(" ","|")
print(f"字符串{b_str}被替换空格后，结果：{new_b_str}")
new_b_list = new_b_str.split("|")
print(f"字符串{new_b_str}按照|分隔后，得到：{new_b_list}")
# 数据容器（序列）的切片操作
"""切片：从一个序列中，取出一个子序列
语法：[起始下标:结束下标:步长]   表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列
起始下标表示从何处开始，可以留空，留空视作从头开始
结束下标（不含）表示何处结束，可以留空，留空视作截取到结尾
步长表示，依次去元素的间隔
步长1表示一个个取
步长2表示每次跳过一个元素取
步长n表示每次跳过n-1个元素取
步长为负数，表示反向取"""
# 对列表切片
a_list = [1,2,3,4,5,6]
result1 = a_list[1:4]     # 步长默认是1，可以省略不写
print(f"结果1：{result1}") # 取到下标4的元素5，不包含它本身
# 对元组切片
a_tuple = (1,2,3,4,5,6)
result2 = a_tuple[:]    # 起始和结束不写表示从头到尾，步长不写表示取默认值1
print(f"结果2：{result2}")
# 对字符串切片
a_str = "01234567"
result3 = a_str[::2]    # 从头到尾，步长2
print(f"结果3：{result3}")

a_str = "01234567"
result4 = a_str[::-1]
print(f"结果4：{result4}")     # 相当于将序列反转

a_list = [1,2,3,4,5,6]
result5 = a_list[3:1:-1]
print(f"结果5：{result5}")     # 从3开始，到1结束，不包含1,。步长1
# 内容连续，有序的数据容器就叫序列
# 练习案例：序列的切片
test_str = "万过薪月，员序程马黑来，nohtyp学"
my_str = test_str[::-1]
print(f"倒序字符串，结果：{my_str}")
fin_str = my_str[9:14]
print(f"最终结果：{fin_str}")

# 集合的定义和操作
"""集合：内容不重复且无序
{元素,元素,...,元素}
变量名称：set()，类型：set  定义空集合可以直接输入set()"""
# 因为集合是无序的，所以不支持下标索引，不是序列。但可以进行修改（同列表）
# 添加新元素
a_set = {"hello","bye",123,321,True}
print(a_set)
a_set.add("python")
print(f"添加新元素后：{a_set}")
# 移除元素
a_set.remove(321)
print(f"移除元素后：{a_set}")
# 随机取出一个元素
a_set.pop()
print(f"随即取出元素后：{a_set}")
# 清空集合
a_set.clear()
print(f"清空集合后：{a_set}")
# 取两个集合的差集
"""
语法：集合1.difference(集合2)
功能：取出集合1和集合2的差集（集合1有而集合2没有的）
结果：得到一个新集合，集合1和集合2不变
"""
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是：{set3}")
# 保留集合的差集，消除两个集合的交集
"""
语法：集合1.difference_update(集合2)
功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
结果：集合1被修改，集合2不变"""
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"消除后，集合1的结果是：{set1}")
print(f"消除后，集合2的结果是：{set2}")
# 2个集合合并为1个（并集）
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"两集合合并后结果：{set3}")
print(f"合并后集合1：{set1}")
print(f"合并后集合2：{set2}")     # 集合1和集合2不变，得到一个新集合，是他俩的并集
# 统计集合元素数量
set1 = {1,2,3,4,5}
num = len(set1)
print(f"集合{set1}的元素数量：{num}")
# 集合的遍历
# 集合不支持下标索引，所以不支持while循环遍历
for element in set1:
    print(f"集合{set1}的元素：{element}")
# 练习案例：信息去重
"""有如下列表对象：
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
请定义一个空集合
通过for循环遍历列表
在for循环中将列表的元素添加至集合
最终得到元素去重后的集合对象，并输出"""
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
test_set = set()
for element in my_list:
    print(f"列表{my_list}中的元素：{element}")
    test_set.add(element)
print(f"最终得到的集合：{test_set}")
# 字典(dict)的定义
"""同样使用{}，存储的是键值对
{key 1:value 1,key 2:value 2,...,key n:value n}
字典不允许key重复，重复添加等同于覆盖原有数据
不可使用下标索引（同集合）"""
my_dict1 = {"wjy":90,"ljj":89,"asd":99}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
my_dict1 = {"wjy":90,"ljj":89,"asd":99,"wjy":92}
print(f"输入重复key的字典，输出结果：{my_dict1}")
# 通过key获取value
my_dict1 = {"wjy":90,"ljj":89,"asd":99}
value1 = my_dict1["wjy"]
value2 = my_dict1["asd"]
print(f"wjy的成绩是：{value1}分")
print(f"asd的成绩是：{value2}分")     # key可以是除字典外的任何类型，value可以是任何类型
# 定义嵌套字典
dict_mine = {       # 换行不影响其定义（只和,有关）
    "wjy":{
        "语文":89,
        "数学":93,
        "英语":90
    },"ljj":{
        "语文":95,
        "数学":89,
        "英语":94
    },"asd":{
        "语文":97,
        "数学":92,
        "英语":88
    }}
print(f"学生考试信息是：{dict_mine}")
score_ljj_math = dict_mine["ljj"]["数学"]
print(f"ljj的数学成绩是：{score_ljj_math}")
# 字典的常用操作
my_dict1 = {"wjy":90,"ljj":89,"asd":99,"wjy":92}
# 新增元素
my_dict1["Jack"] = 76
print(f"新增元素后，结果：{my_dict1}")
# 更新元素
my_dict1["wjy"] = 87
print(f"更新元素后，结果：{my_dict1}")   # key不存在就是新增元素，存在就是更新元素
# 删除元素
score = my_dict1.pop("Jack")
print(f"字典被移除了一个元素，结果是：{my_dict1}，被移除的元素：{score}")
# 清空字典
my_dict1.clear()
print(f"字典被清空了，结果：{my_dict1}")
# 获取全部key
my_dict1 = {'wjy': 87, 'ljj': 89, 'asd': 99}
keys = my_dict1.keys()
print(f"字典的全部keys是：{keys}，数据类型是{type(keys)}")
# 遍历字典（不支持while循环，因为不支持下标索引）
# 法1：通过获取到全部的key来完成遍历
for key in keys:
    value = my_dict1[key]
    print(f"法1 字典的key是：{key}，对应的value是：{value}")
# 法2：直接对字典本身遍历
for key in my_dict1:
    value = my_dict1[key]
    print(f"法2 字典的key是：{key}，对应的value是：{value}")
# 统计字典的元素数量
num = len(my_dict1)
print(f"字典的元素数量是：{num}")
# dict.items()用法
# items()的作用是把字典中的每对key和value组成一个元组，并把这些元祖放在列表中返回
adict = {"key1":"val1","key2":"val2","key3":"val3"}
print(adict.items(),type(adict.items()))
# 练习案例
# 通过for循环，对所有级别为1的员工，级别上升1级，薪水增加1000元
dict_company = {"王力宏":{"部门":"科技部","工资":3000,"级别":1},
                 "周杰轮":{"部门":"市场部","工资":5000,"级别":2},
                 "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
                 "张学友":{"部门":"科技部","工资":4000,"级别":1},
                 "刘德华":{"部门":"市场部","工资":6000,"级别":2}}
print(f"升职加薪前的字典：{dict_company}")
for key in dict_company:
    level = dict_company[key]["级别"]
    salary = dict_company[key]["工资"]
    if level == 1:
        level += 1
        salary += 1000
        dict_company[key]["级别"] = level
        dict_company[key]["工资"] = salary
print(f"升职加薪后的字典:{dict_company}")
"""数据类型分类
序列类型：（支持下标索引，支持重复元素，元素有序）
列表，元组，字符串
非序列类型：
集合，字典

元素可修改：
列表，集合，字典
元素不可修改：
元组，字符串
应用场景：
列表：一批数据，可修改、可重复的存储场景
元组：一批数据，不可修改，可重复的存储场景
字符串：一串字符串的存储场景
集合：一批数据，去重存储场景
字典：一批数据，可用key检索value的存储场景"""

"""通用操作：
遍历：都支持for循环
通用的函数：len()统计元素个数，max()统计最大元素，min()统计最小元素
通用转换功能：list()转列表，tuple()转元组，str()转字符串，set()转集合
通用排序功能:sorted()函数，从小到大排序，排序结果都变成列表；降序就加上reverse=True，例：sorted(my_list,reverse=True)  
"""
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
# 字符串大小比较
# 单个位值根据ASCII码表
print(f"a大于A，结果{'a'>'A'}")
# 字符串大小比较是从左到右一位一位依次比较,有一位更大，整体就更大，它之后的位值就无须再比
print(f"abfg小于acbd，结果{'abfg'<'acbd'}")
# range函数转换为list，tuple,set类型
print(list(range(10)))      # 生成一个1-9的列表
print(list(range(5,10)))
print(tuple(range(5,10)))
print(set(range(5,10)))