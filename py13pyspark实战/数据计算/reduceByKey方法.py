# reduceByKey算子
"""
接收一个处理函数，对数据进行两两计算
针对kv型RDD，自动按照key分组，根据我提供的的聚合逻辑，完成value的聚合,二元元组而非字典
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([("男",99),("女",100),("男",88),("女",66)])
# (v,v) -> v
rdd2 = rdd.reduceByKey(lambda a,b : a + b)      # 自动分组，组内聚合（两两计算）
print(rdd2.collect())
sc.stop()