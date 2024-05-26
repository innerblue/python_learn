# 基础方法
"""
什么是正则表达式：
是一种字符串验证的规则，通过特殊的字符串组合来确立规则
用规则去匹配字符串是否满足

re模块的三个主要方法：
re.match,从头开始匹配，匹配第一个命中项
re.search,全局匹配，匹配第一个命中项
re.findall,全局匹配，匹配全部命中项
"""
import re
s = "python 666"
result = re.match("python",s)
print(result)
print(result.span())
print(result.group())

x = "1python 666"
result = re.search("python",x)
print(result)

y = "1python 2python sanpython 666"
result = re.findall("python",y)
print(result)

# 元字符匹配
