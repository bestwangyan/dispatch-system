#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
import random as r
import time
from Queue import Queue
from multiprocessing.managers import BaseManager
from jobs.job import Job
from config import config



class SlaveProd:
    def __init__(self, server, port, authkey):
        self.dispatched_queue = Queue()
        self.finished_queue = Queue()
        BaseManager.register('get_dispatched_job_queue')
        BaseManager.register('get_finished_job_queue')
        self.manager = BaseManager(address=(server, port), authkey=authkey)

    def _get_new_id(self):
        x=1
        while True:
            yield x
            x+=1

    def _work(self):
        print('start to work')
        for i in self._get_new_id():
            new_job= Job(i,r.random())
            self.dispatched_queue.put(new_job)
            print('dispatched_queue put new job :{0}'.format(i))
            time.sleep(1)

    def start(self):
        self.manager.connect()
        print('slave producer connected server')
        self.dispatched_queue = self.manager.get_dispatched_job_queue()
        self.finished_queue = self.manager.get_finished_job_queue()
        self._work()
        self.manager.shutdown()


if __name__ == '__main__':
    producer = SlaveProd(config.config_info['server_ip'],
                         config.config_info['server_port'],
                         config.config_info['authkey'])
    producer.start()
