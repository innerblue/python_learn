"""
RDD输出到文件的方法
rdd.saveAsTextFile(路径)
输出结果是一个文件夹
有几个分区就输多少个结果文件

如何修改RDD分区
SparkConf对象设置conf.set("spark.default.parallelism","1")
创建RDD时，sc.parallelize方法传入numSlices参数为1
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1")   # 设置分区方法1
sc = SparkContext(conf=conf)

# rdd1 = sc.parallelize([1,2,3,4,5],numSlices = 1)    # 设置分区方法2
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize([("hello",3),("bye",4),("ok",5)])
rdd3 = sc.parallelize([[1,3,5],[2,4,6],[7,8,9]])

rdd1.saveAsTextFile("D:/wjy/output1")
rdd2.saveAsTextFile("D:/wjy/output2")
rdd3.saveAsTextFile("D:/wjy/output3")
