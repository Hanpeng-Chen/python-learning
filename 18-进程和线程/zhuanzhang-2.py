from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        super().__init__()
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续代码
        self._lock.acquire()
        try:
            balance_tmp = self._balance + money
            sleep(0.01)
            self._balance = balance_tmp
        finally:
            # 释放锁
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为： ￥%d元' % account.balance)

if __name__ == '__main__':
    main()