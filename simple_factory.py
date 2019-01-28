# -*- coding:utf-8 -*-

class wheeled_machine(object):
    def __init__(self,wheeled_factory = None):
        self.wheeled_factory = wheeled_factory

    def run_wheeled(self):
        wheeled = self.wheeled_factory
        print 
