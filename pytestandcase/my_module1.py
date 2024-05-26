__all__ = ['test1']     # 这时若使用import *进行调用就只能调用test1了
def test1(a,b):
    print(a + b)
def test2(a,b):
    print(a - b)
#if __name__ == '__main__':      # 测试函数，并确保调用此模块时不会直接输出测试内容
#     test(1,2)