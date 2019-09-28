# multiprocess_001.py
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print("执行子进程 {0}({1})".format(name, os.getpid()))


if __name__ == "__main__":
    print("父进程{}在执行...".format(os.getpid()))
    # 创建子进程，需要输入一个执行函数和函数的参数，创建一个Process实例
    p = Process(target=run_proc, args=("test",))
    print("接下来执行子进程")
    # 用start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用地进程间的同步
    p.join()
    print("子进程执行结束！~")