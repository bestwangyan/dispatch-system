#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
from Queue import Queue
from multiprocessing.managers import BaseManager
import time
from config import config


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
        manager = BaseManager(address=(config.config_info['server_ip'], config.config_info['server_port']),
                              authkey=config.config_info['authkey'])
        manager.start()
        self.dispatched_queue = manager.get_dispatched_job_queue()
        self.finished_queue = manager.get_finished_job_queue()
        print('Manager server started')
        while True:
            print('\n'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+':')
            print('\tdispatched job :{0}'.format(self.dispatched_queue.qsize()))
            print('\tfinished job :{0}'.format(self.finished_queue.qsize()))
            time.sleep(3)


if __name__ == '__main__':
    master = Master()
    master.start()