# coroutine_001.py


def consumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print("【消费者】正在消费{}".format(n))
        r = "200 OK"


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("【生产者】正在生产{}".format(n))
        r = c.send(n)
        print("【生产者】消费者返回{}".format(r))
    c.close()


# 主函数
if __name__ == "__main__":
    c = consumer()
    produce(c)
