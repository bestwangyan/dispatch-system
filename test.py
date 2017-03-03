#! /usr/bin/python
# coding=utf-8
import Queue

q=Queue.Queue()

test_str='''伟大的中华人民共和国'''

for i in xrange(10000000):
    q.put(str(i)+test_str)

print(q.qsize())