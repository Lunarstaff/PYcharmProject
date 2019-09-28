# multiprocess_002.py
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print("执行进程{0}({1})...".format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("进程{0}执行了{1:.2f}秒".format(name, (end - start)))


if __name__ == "__main__":
    print("父进程为：{0}".format(os.getpid()))
    p = Pool(5)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print("等待所有的子进程执行完毕...")
    # 调用join()方法会等待所有的子进程执行完毕，调用join()之前必须先调用close(),
    # 调用close()后就不能继续添加新的Process了。
    p.close()
    p.join()
    print("所有的子进程已执行完毕！")
