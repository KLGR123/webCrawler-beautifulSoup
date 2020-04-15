from random import randrange
from time import ctime, sleep, time
from threading import Lock, Thread
from queue import Queue

lock = Lock()

class MyThread(Thread):
    def __init__(self, func, args):
        super().__init__(target=func, args=args)

#向队列中添加产品
def writeQ(queue):
    lock.acquire()
    print('generate one object and append it to the queue', end=" ")
    queue.put(1)
    print('the queue size: %d' % queue.qsize())
    lock.release()
#从队列中获取商品
def readQ(queue):
    lock.acquire()
    queue.get(1)
    print('consume one object, the queue size: %d' % queue.qsize())
    lock.release()
#建造消费者函数
def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randrange(1, 4)) #消费间隔时间不确定

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randrange(2, 6)) #生产间隔时间不确定

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    q = Queue()
    nloops = randrange(2, 6) #消费与生产次数
    #构建序列
    threads = []
    #把线程迭代初始化，并放入序列中
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops))
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('the whole process is done')

if __name__ == "__main__":
    main()
