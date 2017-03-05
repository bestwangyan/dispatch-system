#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
from Queue import Queue
from multiprocessing.managers import BaseManager
from config import config


class SlaveSave:
    def __init__(self, server, port, authkey):
        self.dispatched_queue = Queue()
        self.finished_queue = Queue()
        BaseManager.register('get_dispatched_job_queue')
        BaseManager.register('get_finished_job_queue')
        self.manager = BaseManager(address=(server, port), authkey=authkey)

    def _work(self):
        print('start to save')
        while True:
            finished_job=self.finished_queue.get()
            finished_job.stop()

    def start(self):
        self.manager.connect()
        print('slave saver connected server')
        #self.dispatched_queue = self.manager.get_dispatched_job_queue()
        self.finished_queue = self.manager.get_finished_job_queue()
        self._work()
        self.manager.shutdown()


if __name__ == '__main__':
    saver = SlaveSave(config.config_info['server_ip'],
                         config.config_info['server_port'],
                         config.config_info['authkey'])
    saver.start()