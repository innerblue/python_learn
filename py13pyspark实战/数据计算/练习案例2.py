"""
副职以上内容到文件中，使用Spark读取文件进行计算：
各个城市销售额排名，从大到小
全部城市，有哪些商品在售卖
北京市有哪些商品类别在售卖
"""
import json
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\python_learn\venv\Scripts\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("D:/orders.txt")

json_str_rdd = file_rdd.map(lambda x: x.split("|"))
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))   # json字符串转字典
tuple_rdd = dict_rdd.map(lambda x: (x["areaName"],int(x["money"])))
city_money_rdd = tuple_rdd.reduceByKey(lambda a,b: a+b)
sort_rdd = city_money_rdd.sortBy(lambda x: x[1],ascending=False,numPartitions=1)    # 这里的x是字典
print(f"需求1的结果：{sort_rdd.collect()}")

thing_rdd = dict_rdd.map(lambda x: x["category"]).distinct()
print(f"需求2def结果是{thing_rdd.collect()}")

bejing_rdd = dict_rdd.filter(lambda x: x["areaName"]=="北京")
bj_thing_rdd = bejing_rdd.map(lambda x: x["category"]).distinct()
print(f"需求3的结果是{bj_thing_rdd.collect()}")
