# filter算子
"""
接收一个处理函数（可以用lambda）
函数对RDD逐个处理，得到True的保留至返回值的RDD中（相当于一种过滤器）
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 返回偶数RDD
rdd = sc.parallelize([1,2,3,4,5])
rdd2 = rdd.filter(lambda num: num%2 == 0)   # 该函数返回bool
print(rdd2.collect())
sc.stop()