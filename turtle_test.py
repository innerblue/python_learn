import turtle
t = turtle.Turtle()
w = turtle.Screen()
def square():
    t.pencolor("green")
    t.pensize(3)
    for i in range(4):
        t.forward(100)
        t.left(90)
    w.exitonclick()
def points5_star():
    t.pensize(5)
    t.pencolor("red")
    for i in range(5):
        t.forward(100)
        t.right(144)
    w.exitonclick()
"""
def tree(branchLen,sz):
    if branchLen > 5:
        t.pensize(sz)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15,sz - 2)
        t.left(20)
        tree(branchLen - 15, sz - 2)
        t.left(20)
        tree(branchLen - 15, sz - 2)
        t.right(20)
    t.backward(branchLen)
def main(a,b):
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.pencolor("brown")
    t.pensize(b)
    t.forward(100)
    tree(a,b)
    w.exitonclick()
"""
# 大佬画的
import turtle
import random
from turtle import *
from time import sleep


def tree(branchLen, t):
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                # 淡珊瑚色
                t.color('lightcoral')
            t.pensize(branchLen / 2)
        else:
            # 赭(zhě)色
            t.color('sienna')
            t.pensize(branchLen / 10)

        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branchLen - 10 * b, t)
        t.left(40 * a)
        tree(branchLen-10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branchLen)
        t.down()


def petal(m, t):  # 树下花瓣
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 30 - 40 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        # 淡珊瑚色
        t.color("lightcoral")
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def main():
    t = turtle.Turtle()
    w = turtle.Screen()
    t.hideturtle() # 隐藏画笔
    t.getscreen().tracer(5, 0)
    w.screensize(bg='wheat') # wheat小麦
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    # 画樱花的躯干
    tree(62, t)
    # 掉落的花瓣
    petal(255, t)
    w.exitonclick()

main()
