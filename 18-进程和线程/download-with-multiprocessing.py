from random import randint
from time import time, sleep
from os import getpid
from multiprocessing import Process

def download_task(filename):
    print('开始下载，进程：[%d]' % getpid())
    print('开始下载 %s' % filename)
    download_time = randint(5, 10)
    sleep(download_time)
    print('%s 下载完成，耗时 %d 秒' % (filename, download_time))

def main():
    start = time()
    p1 = Process(target=download_task, args=('编程从入门到放弃.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('机器学习_周志华.pdf', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗时 %.2f 秒' % (end - start))

if __name__ == '__main__':
    main()