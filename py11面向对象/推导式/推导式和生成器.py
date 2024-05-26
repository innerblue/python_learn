"""
什么是推导式：
推导式是从一个或多个迭代器快速简洁的创建数据结构的一种方法
将循环和条件判断结合，从而避免语法冗长的代码
可以用来生成列表，字典和集合

列表推导式：
[<表达式> for <变量> in <可迭代对象> if <逻辑条件>]
字典推导式：
{<键值表达式>:<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>}
集合推导式：
{<表达式> for <变量> in <可迭代对象> if <逻辑条件>}   # 可以去重

生成器推导式：
(<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>)
返回一个生成器对象，也是可迭代对象
生成器仅在要用到元素时生成元素，可以极大节省内存
生成器是用来创建数据序列的一种对象
使用它可以迭代庞大的序列，且不需要在内存中创建和存储整个序列
通常生成器是为迭代器产生数据的，是迭代器的一种实现
"""
print([x*x for x in range(10)])     # 输出0-10各数的平方
print({f"K{x}":x**3 for x in range(10)})
print([x+y for x in range(10) for y in range(x)])   # 循环嵌套
print([x*x for x in range(10) if x%2 == 0])
print([x.upper() for x in [1,'abc','xyz',True] if isinstance(x,str)])   # isinstance(对象实例，类名),返回bool
agen = (x*x for x in range(5))
for i in agen:
    print(i)
