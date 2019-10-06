# multithreading_003.py
import time, threading

# balance为全局变量
balance = 0

# 实例化一个Lock对象
lock = threading.Lock()


# 修改balance值
def change_balance(n):
    global balance
    # 对balance进行先+n再-n的操作，预期结果仍然为0
    balance = balance + n
    balance = balance - n


# 线程任务
def run_thread(n):
    # 线程中调用change_balance 10万次
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            # 修改数据
            change_balance(n)
        finally:
            # 释放锁
            lock.release()


# 主函数
if __name__ == "__main__":
    # 创建第一个子线程，执行子进程时+-balance值为5
    t1 = threading.Thread(target=run_thread, args=(5,))
    # 创建第二个子线程，执行子进程时+-balance值为8
    t2 = threading.Thread(target=run_thread, args=(8,))
    # 启动线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 执行完毕打印balance值
    print(balance)

