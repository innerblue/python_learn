# 综合案例：数据分析案例
"""
某公司有两份数据文件，现需要对其进行分析处理，计算每日销售额并以柱状图表的形式进行展示
思路：
读取数据 -> 封装数据对象 -> 计算数据对象 -> pyecharts绘图
用面向对象的思想：
读取数据：设计FileReader类；
封装数据对象：设计数据封装类；
计算数据对象：对对象进行逻辑计算
pyecharts绘图：以面向对象思想重新认识pyecharts

具体实现步骤：
1、设计一个类，可以完成数据的封装
2、设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能（有文本文件和json文件）
3、读取文件，生产数据对象
4、进行数据需求的逻辑计算（计算每一天的销售额）
5、通过pyecharts进行图形绘制
"""
from file_define import FileReader,csvFileReader,jsonFileReader
from data_define import Record
csvreader = csvFileReader("path1")
jsonreader = jsonFileReader("path2")
csvlist:list[Record] = csvreader.read_data()        # 这几个列表里面存的都是类对象
jsonlist:list[Record] = jsonreader.read_data()
all_list:list[Record] = csvlist + jsonlist
# 数据计算
all_dict = {}      # 日期对应销售额
for record in all_list:
    if record.date in all_dict:     # 判断日期是否在字典中
        all_dict[record.date] += record.money
    else:
        all_dict[record.date] = record.money
print(all_dict)

# 数据可视化
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
bar = Bar()
bar.add_xaxis(list(all_dict.keys()))
bar.add_yaxis("销售额",list(all_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")
