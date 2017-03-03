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

    def _get_new_id(self):
        x=1
        while True:
            yield x
            x+=1

    def _work(self):
        print('start to work')
        #for i in xrange(0, 100):
        for i in self._get_new_id():
            new_job = {
                'file_id':i,
                'file_name':r.random(),
                'file_type':i%3,
                'status':'P'
            }#job.Job(r.random(), i)
            self.dispatched_queue.put(new_job)
            print('dispatched_queue put new job :{0}'.format(i))
            while self.finished_queue.qsize()>0:
                done_job=self.finished_queue.get()
                print('Job {0} done . The status is {1}'.format(done_job['file_id'],done_job['status']))
            time.sleep(1)

    def start(self):
        self.manager.connect()
        print('slave producer connected server')
        self.dispatched_queue = self.manager.get_dispatched_job_queue()
        self.finished_queue = self.manager.get_finished_job_queue()
        self._work()
        self.manager.shutdown()


if __name__ == '__main__':
    producer = SlaveProd('192.168.0.50', 8888, 'test')
    producer.start()
