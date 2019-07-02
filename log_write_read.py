# -*- coding:utf-8 -*-
from threading import Thread
from threading import Condition
import random

log_list = []
maxnum = 1000
condition = Condition()

class log_producer(Thread):
    def __init__(self,filename):
        Thread.__init__(self)
        self.f = filename
        self.fo = open(filename,'r')
    def __del__(self):
        self.fo.close()
    def run(self):
        global log_list
        tmp = self.fo.readline()
        while tmp:
            condition.acquire()
            if len(log_list) == maxnum:
                print "producer wait:" + str(self.f)
                print log_list
                condition.wait()
            log_list.append(str(self.f) + ":" + tmp)
            tmp = self.fo.readline()
            condition.notify()
            condition.release()

class log_consumer(Thread):
    def __init__(self,filename):
        Thread.__init__(self)
        self.fo = open(filename,'w')
    def __del__(self):
        self.fo.close()
    def run(self):
        global log_list
        flag = True
        while flag or log_list:
            condition.acquire()
            if not log_list:
                print "consumer wait"
                condition.wait()
            wtmp = log_list.pop(0)
            self.fo.write(wtmp)
            flag = False
            condition.notify()
            condition.release()

if __name__ == "__main__":
    a = log_producer("./newsgateway.log.20190627")
    b = log_producer("./newsgateway.log.20190628")
    c = log_producer("./newsgateway.log.20190629")
    d = log_consumer("./newsgateway.log")
    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    d.join()
