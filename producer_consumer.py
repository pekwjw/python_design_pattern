# -*- coding:utf-8 -*-

from threading import Thread
from threading import Condition
import time
import random

queue = []
max_num = 10
condition = Condition()
timestamp = int(time.time()) + 100

class Producer(Thread):
    def run(self):
        global queue
        while time.time() <= timestamp:
            condition.acquire()
            if len(queue) == max_num:
                print "producer before waiting"
                condition.wait()
                print "producer after waiting"
            num = random.random()
            queue.append(num)
            print "produced: ", num
            condition.notify()
            condition.release()
            time.sleep(num)

class Consumer(Thread):
    def run(self):
        global queue
        while time.time() <= timestamp:
            condition.acquire()
            if not queue:
                print "    consumer before waiting"
                condition.wait()
                print "    consumer after waiting"
            num = queue.pop(0)
            print "    consumed: ", num
            condition.notify()
            condition.release()
            time.sleep(num) 

from Queue import Queue
queue = Queue(max_num)
class q_producer(Thread):
    def run(self):
        global queue
        while time.time() <= timestamp:
            num = random.random()
            queue.put(num)
            print "q_produced: ", num
            time.sleep(num)

class q_consumer(Thread):
    def run(self):
        global queue
        while time.time() <= timestamp:
            num = queue.get()
            queue.task_done()
            print "    q_consumed: ", num
            time.sleep(num)

if __name__ == '__main__':
    #Producer().start()
    #Consumer().start()
    
    q_producer().start()
    q_consumer().start()    
