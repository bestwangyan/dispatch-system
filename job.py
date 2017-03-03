#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# purpose:
# Author:Wang Yan
# CreationDate:20160909
class Job:
    def __init__(self,file_id,file_type,file_status='p'):
        self.file_id=file_id
        self.file_type=file_type
        self.status= file_status
