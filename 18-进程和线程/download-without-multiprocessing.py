from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载%s ' % filename)
    download_time = randint(5, 10)
    sleep(download_time)
    print('%s 下载完成， 共耗时 %d 秒' % (filename, download_time))

def main():
    start = time()
    download_task('编程从入门到放弃.pdf')
    download_task('机器学习_周志华.pdf')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()