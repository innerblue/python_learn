"""
读取文件转换成RDD，并完成：
打印输出：热门搜索时间段（小时）TOP3
打印输出：热门搜索词TOP3
打印输出：统计黑马程序员在哪个时段被搜索最多
将数据转为json格式，写出为文件
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)

rdd = sc.textFile("path")
# 需求1：热门搜索时间段（小时）TOP3
"""
思路：
1、提取出小时并放入双元组内
2、计数（分组聚合）
3、按降序排序
4、取前3
"""
result1 = rdd.map(lambda x: x.split("\t")).\
    map(lambda x: x[0][:2]).map(lambda x: (x,1)).\
    reduceByKey(lambda a,b: a + b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)

print(f"需求1的结果：{result1}")

# 需求2：热门搜索词前三
"""
思路：
1、取出所有搜索词
2、放入双元组，分组聚合
3、降序排序
4、取出前3
"""
result2 = rdd.map(lambda x: x.split("\t")).\
    map(lambda x: x[2]).map(lambda x: (x,1)).\
    reduceByKey(lambda a,b: a + b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)

print(f"需求2的结果{result2}")

# 需求3：统计黑马程序员哪个时段搜索最多
"""
思路：
1、提取所有元素到列表
2、从列表中过滤出仅有“黑马程序员”的部分
3、将时段和搜索量放入二元组中
4、分组聚合
5、按搜索量排序
6、取出该时段
"""
result3 = rdd.map(lambda x: x.split("\t")).\
    filter(lambda x: x[2] == "黑马程序员").\
    map(lambda x: (x[0],x[4])).\
    reduceByKey(lambda a,b: a + b).\
    sortBy(lambda x: x[0],ascending=False,numPartitions=1).\
    take(1)

print(f"需求3的结果：{result3}")

# 需求4：将数据转换为json格式，写出为文件
"""
思路：
1、RDD转为json     # 对于pyspark，字典即为json格式
2、写入文件
"""
file_rdd = rdd.map(lambda x: x.split("\t")).\
    map(lambda x: {"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]})

file_rdd.saveAsTextFile("path")


