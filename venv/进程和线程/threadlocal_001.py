# threadlocal_001.py


class Student:
    def __init__(self, name):
        self.name = name


# 下面代码演示了多线程环境下，某线程使用局部变量时传参的方式
def process_student(name):
    std = Student(name)
    # std 是局部变量，但是每个函数都要用它，因此必须传进去
    do_task_1(std)
    do_task_2(std)


def do_task_1(std):
    do_sub_task_1(std)
    do_sub_task_2(std)


def do_task_2(std):
    do_sub_task_2(std)
    do_sub_task_2(std)