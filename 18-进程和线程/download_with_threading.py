from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print('开始下载 %s' % filename)
    download_time = randint(5, 10)
    sleep(download_time)
    print('%s 下载完成，耗时 %d 秒' % (filename, download_time))

def main():
    start = time()
    t1 = Thread(target=download, args=('编程从入门到放弃.pdf', ))
    t1.start()
    t2 = Thread(target=download, args=('机器学习_周志华.pdf', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('下载完成，共耗时 %.df秒' % (end - start))

if __name__ == '__main__':
    main()