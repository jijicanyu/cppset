#! /usr/bin/env python
#coding=utf-8
# 解析redis的二进制数据，通过友好的方式展示
#默认的redis二进制数据如下显示：
# \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00777\x00S
# 这个脚本实现了将多个\x00替换为1个空格，从而让有用的信息清晰可见

import subprocess
import sys

if len(sys.argv) < 2:
    print 'please input key'
    exit(0)
cmdPre = './redis-cli -p $REDIS_LOCAL_PORT '
cmd = '%s type %s' % (cmdPre,sys.argv[1])
data = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
types = ''.join(data.stdout.readlines())
if 'string' in types:
    cmd = '%s get %s' % (cmdPre,sys.argv[1])
elif 'set' in types:
    cmd = '%s smembers %s' % (cmdPre,sys.argv[1])
else:
    print 'none'
    exit(0)
    
data = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
for line in data.stdout.readlines():
    print ' '.join(line.strip('\n').replace('\x00',' ').split())

