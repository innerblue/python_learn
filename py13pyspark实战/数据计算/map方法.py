# map算子（成员方法）
"""
接收一个处理函数，可以用lambda函数快速编写
对RDD内的元素逐个处理，并返回新的RDD
"""
# 链式调用
"""
对于返回值是新RDD的算子，可以用链式调用的方式多次调用算子
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 通过parallelize方法将python对象加载到spark内，成为RDD类对象
rdd1 = sc.parallelize([1,2,3,4,5])
# 通过map方法将全部数据乘10
# def func(data):
#    return data*10
# (T) -> U
# (T) -> T
# rdd2 = rdd1.map(func)

rdd2 = rdd1.map(lambda x:x*10)
print(rdd2.collect())
sc.stop()