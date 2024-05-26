# distinct算子
"""
对RDD中数据进行去重（不需要传参）
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,34,5,2,3,7,3,7,5,8,8,0,10])
rdd2 = rdd.distinct()
print(rdd2.collect())
sc.stop()