# 输出为python对象
"""
spark的编程流程：
将数据加载为RDD（数据输入）
对RDD进行计算（数据计算）
将RDD转换为python对象（数据输出）
数据输出的方法：
collect：将RDD内容转换为list
reduce：对RDD内容进行自定义聚合
take：取出RDD的前n个元素组成立list
count：统计RDD元素个数
数据输出可用方法很多，这里只介绍4个
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# collect算子
rdd = sc.parallelize([1,2,3,4,5])
rdd_list:list = rdd.collect()
print(rdd_list)

# reduce算子      func:(T,T) -> T
num = rdd.reduce(lambda a,b: a + b)
print(num)

# take算子
take_list = rdd.take(3)     # 前3个算子
print(take_list)

# count算子
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")

sc.stop()

