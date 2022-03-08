# 生产者-消费者模式    
# 数据通常保留在一个消息队列中，提供队列进行数据共享 Multiprocessing.Queue
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def producer(q):
    for value in range(5):
        print("Produce %d" % value)
        q.put(value)
        time.sleep(1)

# 读数据进程执行的代码
def consumer(q):
    while True:
        value = q.get(True)
        print("Consume %d" % value)
        time.sleep(1)

if __name__ == "__main__":
    t0 = time.time()
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=producer, args=(q, ))
    pr = Process(target=consumer, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # pr进程里是死循环，无法等待结束，只能强行终止
    print("Take %ss." % (time.time() - t0))
