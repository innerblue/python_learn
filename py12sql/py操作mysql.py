# 基础使用
"""
python中使用pymysql库操作MySQL（第三方库）
获取链接对象：
from pymysql import Connection
类对象实例Connection(主机，端口，账户，密码)即可获得链接对象
链接对象.close关闭和MySQL数据库的连接

执行SQL查询：
通过连接对象调用cursor()方法，得到游标对象
游标对象.execute()执行SQL语句
游标对象.fetchall()得到全部的查询结果封装到元组内
"""
from pymysql import Connection

conn = Connection(
    host="localhost",       # 主机名（也可以写ip地址）
    port=3306,              # 端口
    user="root",            # 管理员账户
    password="wjy123456",   # 密码
    autocommit=True
)
# print(conn.get_server_info())     # 得到服务器版本
# conn.close()
# 执行非查询性质SQL
cursor = conn.cursor()      # 获取游标对象
conn.select_db("students")  # 选择数据库
# cursor.execute("create table my_student(id int);")  # 执行SQL
# 执行查询性质的SQL
cursor.execute("select * from student;")
results:tuple = cursor.fetchall()
# print(results)
for result in results:
    print(result)
# 关闭链接
# conn.close()

# 数据插入
"""
pymysql在执行数据插入或其他产生数据更改的SQL语句时，默认是需要提交更改的
1、可以通过commit提交
2、可以在构建链接对象时，设置自动commit属性 -> autocommit = True
"""
# cursor.execute("insert into student values('艾山江',1010,26,'男');")
# 通过commit确认（手动）
# conn.commit()
conn.close()

# 自动确认，见构建对象conn中
