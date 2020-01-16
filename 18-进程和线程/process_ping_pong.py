from multiprocessing import Process
from time import time, sleep

counter = 0

def task(string):
    global counter
    while counter < 10:
        print(string, end=' ', flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=task, args=('ping', )).start()
    Process(target=task, args=('pong', )).start()

if __name__ == '__main__':
    main()