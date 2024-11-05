import time
import threading
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        x = randint(50, 500)
        for i in range(100):
            self.balance += x
            print(f'Пополнение: {x}. Баланс: {self.balance} \n')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep(0.001)


    def take(self):
        x = randint(50, 500)
        print(f'Запрос на {x} \n')
        for i in range(100):

            if self.balance < x:
                print(f'Запрос отклонён, недостаточно средств \n')
                self.lock.acquire()
            else:
                self.balance -= x

                print(f'Снятие: {x}. Баланс: {self.balance} \n')
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()



