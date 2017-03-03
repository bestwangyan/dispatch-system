#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
from Queue import Queue
from multiprocessing.managers import BaseManager
import random as r
import job
import time


class SlaveProd:
    def __init__(self, server, port, authkey):
        self.dispatched_queue = Queue()
        self.finished_queue = Queue()
        BaseManager.register('get_dispatched_job_queue')
        BaseManager.register('get_finished_job_queue')
        self.manager = BaseManager(address=(server, port), authkey=authkey)

    def _work(self):
        print('start to work')
        while True:
            new_job=self.dispatched_queue.get()
            print('Got new job :{0}'.format(new_job['file_id']))
            new_job['status']='S'
            time.sleep(3)
            self.finished_queue.put(new_job)


    def start(self):
        self.manager.connect()
        print('slave consumer connected server')
        self.dispatched_queue = self.manager.get_dispatched_job_queue()
        self.finished_queue = self.manager.get_finished_job_queue()
        self._work()


if __name__ == '__main__':
    producer = SlaveProd('192.168.0.50', 8888, 'test')
    producer.start()