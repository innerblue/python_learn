"""
pyspark的功能都是从sparkcontext对象作为执行入口
pyspark编程模型：
数据输入：通过sparkcontext完成数据读取
数据计算：读取到的数据都转换为RDD对象，调用RDD的成员方法完成计算
数据输出：调用RDD的数据输出相关成员方法，将结果输出到列表，元组，字典，文本文件，数据库等
"""
# 导包
from pyspark import SparkConf, SparkContext
import os
os.environ['JAVA_HOME'] = r"C:\Program Files\Java\jdk-21"
# 创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 链式调用，适用于成员方法返回值仍是SparkConf的情况
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印pyspark的运行版本
print(sc.version)
# 停止sparkcontext对象的运行（停止pyspark运行）
sc.stop()
