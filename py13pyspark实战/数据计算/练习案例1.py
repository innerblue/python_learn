"""
使用学过的知识，完成：
读取文件
统计文件内，单词的出现数量
"""
# 构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 读取数据文件
rdd = sc.textFile("D:/hello.txt")
# 取出全部单词
rdd_word = rdd.flatMap(lambda x:x.split(" "))
# 将单词放入二元组方便计数，key为单词，value为1
rdd_w_num = rdd_word.map(lambda word : (word,1))
# 分组并求和
rdd_num = rdd_w_num.reduceByKey(lambda a,b:a+b)
print(rdd_num.collect())
sc.stop()