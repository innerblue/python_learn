"""
将py11面向对象数据分析案例中的数据集，使用py语言读取数据，并将数据写入MySQL
"""
from py11面向对象.数据分析案例 import data_define,file_define
from pymysql import Connection
csvreader = file_define.csvFileReader("path1")
jsonreader =file_define.jsonFileReader("path2")
csvlist:list[data_define.Record] = csvreader.read_data()        # 这几个列表里面存的都是类对象
jsonlist:list[data_define.Record] = jsonreader.read_data()
all_list:list[data_define.Record] = csvlist + jsonlist

conn = Connection(
    host="localhost",       # 主机名（也可以写ip地址）
    port=3306,              # 端口
    user="root",            # 管理员账户
    password="wjy123456",   # 密码
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("py_sql")
for record in all_list:
    sql = f"insert into market_data(order_date,order_id,money,province) "\ 
          f"values('{record.date}','{record.order_id}',{record.money},'{record.province}');"
    cursor.execute(sql)

# 查询sql
cursor.execute("select * from market_data;")
results:tuple = cursor.fetchall()

from 把SQL写入文件 import WriterJson
writer = WriterJson(results,"D:\桌面desktop\数据结构_py")
writer.Writer()

conn.close()
