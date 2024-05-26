# 基础查询
"""
基础查询：
select 字段列表 from 表
过滤查询：
select 字段列表 from 表 where 条件判断
"""

# 分组聚合
"""
select 字段|聚合函数 from 表 [where 条件] group by 列
聚合函数有：
sum(列)  求和
avg(列)  求平均值
min(列)  求最小值
max(列)  求最大值
count(列|*)    求数量
注意：
group by中出现了哪个列，哪个列才能出现在select的非聚合中
"""

# 排序分页
"""
select 列|聚合函数|* from 表
where ...
group by ...
order by ... [asc|desc]
limit n[,m]
注意：
where、group by、order by、limit 均可按需求省略
select、from不能省略
执行顺序：
from -> where -> group by和聚合函数 -> select -> order by -> limit
"""
