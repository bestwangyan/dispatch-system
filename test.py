#! /usr/bin/python
# coding=utf-8
import Queue

from jobs import job

new_job= job.Job(123, '.jpg')
print(new_job.file_id)

q=Queue.Queue()
q.put(new_job)
another_job=q.get()

print(another_job.file_type)