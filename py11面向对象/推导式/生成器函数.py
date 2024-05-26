"""
如果要创建一个比较大的序列，生成器推导式将会比较复杂，一行表达式无法容纳，这时可以定义生成器函数
生成器函数和普通函数：
生成器函数的定义和普通函数一样，只是将return换成yield
yield和return：
yield语句：立即返回一个值，下一次迭代生成器函数时，从yield语句后的语句继续执行，直到再次yield返回，或终止
return语句：终止函数的执行，下一次调用会重新执行函数
协同程序：可以运行的独立函数调用，函数可以暂停或挂起，并在需要的时候从离开的地方继续或重新开始
"""
def even_number(max):
    n = 0
    while n < max:
        yield n
        n += 2

for i in even_number(10):
    print(i)