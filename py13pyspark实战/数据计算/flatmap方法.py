# flatmap算子
"""
计算逻辑和map一样
比map多出接触一层嵌套的功能
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["shut up","get on","dont forget"])
# 将RDD数据里的单词一个个提取出来
rdd2 = rdd.flatMap(lambda x : x.split(" "))
print(rdd2.collect())
sc.stop()