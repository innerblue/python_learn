"""
SQL大小写不敏感
SQL可以单行或多行书写，最后以;结束
SQL支持注释：
单行注释：-- 注释内容
单行注释：# 注释内容
多行注释：/* 注释内容 */
"""
# DDL库管理
"""
查看数据库:show databases;
使用数据库:use 数据库名称;
创建数据库:create database 数据库名称 [charset UTF8]; 中括号里的表示可写可不写
删除数据库:drop database 数据库名称;
查看当前使用的数据库:select database();
"""
# DDL表管理
"""
查看有哪些表（先选择数据库）:show tables;
删除表:
drop table 表名称;
drop table if exist 表名称;
创建表:
creat table 表名称(
    列名称 列类型,
    列名称 列类型,
    ...
);
列类型:
int     整数
float   浮点数
varchar(长度)     文本，长度为数字，做最大长度控制
date    日期类型
timestamp        时间戳
"""
