# threadlocal_002.py
# 下面例子展示了使用`ThreadLocal`实现线程之间的数据隔离

import threading


# 全局的ThreadLocal对象：
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print("你好{}（在线程{}中）".format(std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


# 主函数
if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=("A-std", ), name="1")
    t2 = threading.Thread(target=process_thread, args=("B-std", ), name="2")

    t1.start()
    t2.start()
    t1.join()
    t2.join()