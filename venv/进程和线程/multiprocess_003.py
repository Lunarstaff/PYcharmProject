# multiprocess_003.py

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程
def write(q):
    print("执行写数据进程：pid-{0}".format(os.getpid()))
    for value in ["A","B","C","D"]:
        print("正在写{}到队列中...".format(value))
        q.put(value)
        time.sleep(random.random())


# 读数据进程
def read(q):
    print("执行读取数据进程：pid-{}".format(os.getpid()))
    while True:
        value = q.get(True)
        print("从队列中读取到数据：{}".format(value))


# 主函数
if __name__ == "__main__":
    # 父进程创建队列（Queue），并传给各个子进程
    q = Queue()
    process_write = Process(target=write, args=(q,))
    process_read = Process(target=read, args=(q,))

    # 启动子进程process_write，写入
    process_write.start()
    # 启动子进程process_read，读取
    process_read.start()

    # 等待写入结束
    process_write.join()

    # process_read进程是死循环，要强制终止
    process_read.terminate()
