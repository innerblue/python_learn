# 练习:取出列表中的偶数
"""定义一个列表，内容是[1,2,3,4,5,6,7,8,9,10]
遍历列表，取出列表内的偶数，并存入一个新的列表对象中
使用while和for循环各操作一次"""
# while循环
a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = []
index = 0
while index < len(a_list):
    element = a_list[index]
    if element % 2 == 0:
        print(f"列表内的偶数:{element}")
        b_list.append(element)
    index += 1
print(f"新的列表:{b_list}")
# for循环
a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = []
for element in a_list:
    if element %2 == 0:
        print(f"列表内的偶数:{element}")
        b_list.append(element)
print(f"新的列表:{b_list}")
a = [[0,0,0],[0,0,0],[0,0,0]]
a[0][0] = 1
print(a)
print([id(x) for x in a])