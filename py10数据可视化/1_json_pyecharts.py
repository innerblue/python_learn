# json
"""
json是一种轻量级的数据交互格式，采用完全独立于编程语言的文本格式来存储和表示数据（就是字符串）
对于python使用者来说，json无非就是一个单独的字典或内部元素都是字典的列表
所以json可以和python的字典或列表进行无缝转换
通过json.dumps(data)方法把python数据转化为了json数据
data = json.dumps(data)，如果有中文可以带上ensure_ascii=False参数来确保中文的正常转换
通过json.loads(data)方法把json数据转化为python列表或字典
data = json.loads(data)
"""
import json
data = [{"name":"王大锤","age":20},{"name":"小明","age":15},{"name":"李华","age":28}]
json_str = json.dumps(data,ensure_ascii=False)
print(json_str,type(json_str))
d = {"name":"周杰轮","addr":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(json_str,type(json_str))
# 将json字符串转换为python数据类型
ds = '[{"name":"王大锤","age":20},{"name":"小明","age":15},{"name":"李华","age":28}]'
l = json.loads(ds)
print(l,type(l))
# pyecharts模块
# 导入line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 得到折线图对象
# line = Line()
# # 添加x轴数据
# line.add_xaxis(["王大锤","小明","李华"])
# line.add_yaxis("成绩",[70,80,90])
# # 生成图表
# #line.render()
# # pyecharts配置
# """
# 全局配置，系统配置
# 全局配置：set_global_ops方法
# """
# line.set_global_opts(
#     title_opts=TitleOpts(title="成绩展示",pos_left="center",pos_bottom="3%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )   # 分别是：标题，图例，工具箱，视觉映射
# line.render()
# 数据可视化
from pyecharts.charts import Map
# 准备地图对象
# map = Map()
# # 准备数据
# data = [
#     ("北京市",99),
#     ("上海市",199),
#     ("湖南省",299),
#     ("台湾省",399),
#     ("广东省",499)
# ]
# # 添加数据
# map.add("测试地图",data,"china")      # 这个data这里必须是列表
# # 设置全局选项
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(                                   # 设置地图的视觉指示器
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":9,"label":"1-9","color":"#00EE00"},      # 调整颜色，RGB16位的编码
#             {"min":10,"max":99,"label":"10-99","color":"#FFFF00"},
#             {"min": 100, "max":299, "label": "100-299", "color": "#FF6347"},
#             {"min": 300, "max": 399, "label": "300-399", "color": "#FF6347"},
#             {"min": 400, "max": 499, "label": "400-499", "color": "#FF0000"},
#         ]
#     )
# )
# # 绘图
# map.render()

# 全国疫情地图构建
# 河南省疫情地图构建（详见视频）
"""
先open打开json文件，把数据读出来，然后索引处信息：
1、全国的就索引到省，用for循环拿到各省的信息，再用map进行绘图
2、省级的就用for循环拿到各市的信息，再用map绘图
"""

# 基础柱状图构建
"""
通过Bar绘制
"""
from pyecharts.charts import Bar
from pyecharts.options import *
bar = Bar()
# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10],
              label_opts=LabelOpts(position="right"))   # 让数字标签都到右侧
# 反转x和y轴
bar.reversal_axis()
bar.render("基础柱状图.html")
# 总之，和折线图差不多

# 基础时间线柱状图
from pyecharts.charts import Timeline   # 导入时间线
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,50,50],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[70,60,60],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
# 构建时间线对象
timeline = Timeline({"theme":ThemeType.DARK})     # 设置主题(这里的“DARK是一个（颜色）主题，还有LIGHT等等”)
# 在时间线内添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")


# 自动播放设置
timeline.add_schema(
    play_interval=1000,      # 表示自动播放的时间间隔，单位ms
    is_timeline_show=True,
    is_auto_play=True,       # 是否自动播放
    is_loop_play=True        # 是否循环播放
)
# 绘图是用时间线对象，而不是bar对象了
timeline.render("基础时间线柱状图.html")

# 动态GDP柱状图绘制
# 准备列表
#my_list = [["a",33],["b",55],["c",11]]
# 用sort方法排序
# 排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]       # 也就是按照数字大小排序
# my_list.sort(key=choose_sort_key,reverse=True)
# print(my_list)
# 排序，基于lambda匿名函数
#my_list.sort(key=lambda element:element[1],reverse=True)
#print(my_list)
# 练习案例：全球GDP柱状图
f = open("D:\桌面desktop/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()      # 取出后放入列表（每一行是列表中的一个元素）
f.close()
# 删除第一行
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 这里line是字符串，用split方法按，将字符串分隔放入列表
    state = line.split(",")[1]
    GDP = float(line.split(",")[2])
# 用捕获异常来判断这里的key（这里也就是year）是否存在，用line遍历data_lines时会有部分line的年份重复,
# 年份已经有了就append添加，还没有就字典新增
    try:
        data_dict[year].append([state,GDP])
    except KeyError:
        data_dict[year] = [[state,GDP]]
year_list = sorted(data_dict.keys())
timeline = Timeline({"theme": ThemeType.LIGHT})
for year in year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    gdp_8_list = data_dict[year][0:8]
    x_data = []
    y_data = []
    for state_gdp in gdp_8_list:
        x_data.append(state_gdp[0])
        y_data.append(state_gdp[1]/100000000)  # 以亿为单位
    x_data.reverse()
    y_data.reverse()
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    timeline.add(bar,time_point=str(year))
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("1960-2019全球GDP柱状图.html")