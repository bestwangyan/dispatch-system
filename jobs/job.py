#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
from Queue import Queue
import time


class Job:
    def __init__(self,job_id,file_id):
        self.status = 'P'
        self.job_id=job_id
        self.file_id = file_id

    def get_file(self):
        pass

    def validate_invoice(self):
        pass

    def work(self):
        print('I am working')
        self.status='S'
        time.sleep(2)
        print('Finished')

    def stop(self):
        pass
        print('Job {0} stopped . The status is {1} haha'.format(self.job_id, self.status))
        time.sleep(1)