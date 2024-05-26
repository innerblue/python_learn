"""
什么是工厂模式：
将对象的创建由使用原生类本身创建转换到由使用特定的工厂方法创建

好处：
大批量创建对象时有统一的入口，易于代码维护
当发生修改，仅修改工厂类的创建方法即可
"""

class person:
    pass

class worker(person):
    pass

class student(person):
    pass

class teacher(person):
    pass

class personFactory:
    def get_person(self,job):
        if job == "w":
            return worker()
        elif job == "s":
            return student()
        else:
            return teacher()

pf = personFactory()
wk = pf.get_person("w")
sd = pf.get_person("s")
tc = pf.get_person("t")