#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
from Queue import Queue
from multiprocessing.managers import BaseManager
import time


class Master:
    def __init__(self):
        self._dispatched_job_queue = Queue()
        self._finished_job_queue = Queue()

    def get_dispatched_job_queue(self):
        return self._dispatched_job_queue

    def get_finished_job_queue(self):
        return self._finished_job_queue

    def start(self):
        BaseManager.register('get_dispatched_job_queue', callable=self.get_dispatched_job_queue)
        BaseManager.register('get_finished_job_queue', callable=self.get_finished_job_queue)
        manager = BaseManager(address=('192.168.0.50', 8888), authkey='test')
        manager.start()
        print('Manager server started')
        while True:
           time.sleep(100)


if __name__ == '__main__':
    master = Master()
    master.start()