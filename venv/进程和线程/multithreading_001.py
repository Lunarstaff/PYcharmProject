# multithreading_001.py

import time, threading

# 线程要执行的内容：
def loop():
    print("正在执行线程{}".format(threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print("正在执行的线程{0}>>>{1}".format(threading.current_thread().name, n))
        time.sleep(1)
    print("线程{}执行完毕".format(threading.current_thread().name))

if __name__ == "__main__":
    print("线程{}正在执行".format(threading.current_thread().name))

    # 创建第二个线程
    t = threading.Thread(target=loop, name="Loop()")
    t.start()
    t.join()
    print("线程{}执行完毕".format(threading.current_thread().name))