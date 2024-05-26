# RDD对象
"""
RDD对象称为分布式弹性数据集，是pyspark中数据计算的载体，作用：
提供数据存储
提供数据计算的各种方法
数据计算的方法，返回值依旧是RDD（RDD迭代计算）
后续对数据进行各种计算都是基于RDD对象
"""
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 通过parallelize方法将python对象加载到spark内，成为RDD类对象
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1":"value1","key2":"value2","key3":"value3"})
# 查看RDD内容，用collect()方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())       # 字符串每个字母拆出来了，字典只取了key

# sc.stop()
# 通过textfile方法，读取文件加载到spark内，成为RDD对象
rdd = sc.textFile("D:/hello.txt")
print(rdd.collect())

sc.stop()
