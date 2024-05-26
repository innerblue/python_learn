# sortBy算子
"""
接收一个处理函数（可用lambda）
函数表示用来决定排序的依据
可以控制升序或降序
全局排序需要设置分区数为1
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
# 按单词数降序
rdd_order = rdd_num.sortBy(lambda x: x[1],ascending=False,numPartitions=1)      # 降序ascending为False
print(rdd_order.collect())
sc.stop()