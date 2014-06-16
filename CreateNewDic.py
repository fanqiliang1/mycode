#!/usr/bin python
#coding:utf-8

fp1 = open('/home/qiliangfan/taskfan/自然语言分析/新字典/NTUSD_positive_simplified.txt', 'r')
fp2 = open('/home/qiliangfan/taskfan/自然语言分析/新字典/中文正.txt', 'r')
fp3 = open('/home/qiliangfan/taskfan/自然语言分析/新字典/中文正极性词语.txt', 'w')

fn1 = open('/home/qiliangfan/taskfan/自然语言分析/新字典/NTUSD_negative_simplified.txt', 'r')
fn2 = open('/home/qiliangfan/taskfan/自然语言分析/新字典/中文负.txt', 'r')
fn3 = open('/home/qiliangfan/taskfan/自然语言分析/新字典/中文负极性词语.txt', 'w')


d1 = set()
d2 = set()

for line in fp1:
    d1.add(line)
fp1.close()

for line in fp2:
    d1.add(line)
fp2.close()

for key in d1:
    fp3.write(key)

for line in fn1:
    d2.add(line)
fn1.close()

for line in fn2:
    d2.add(line)
fn2.close()

for key in d2:
    fn3.write(key)

fn3.close()


