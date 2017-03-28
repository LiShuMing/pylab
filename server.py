#! /usr/bin/env python
# -#- coding: utf-8 -#-
#
# vim           : fenc=utf-8
# author	: lishuming01@baidu.com
# file		: server.py
# cdatetime     : 2017-01-05 13:28
#

"""

"""
import socket
import os
import sys

PORT = 8083

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sd.bind(('0.0.0.0', PORT))
sd.listen(5)

for i in range(10):
    if os.fork() == 0:
        sd.close()
        cd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cd.connect(('127.0.0.1', PORT))
        sys.exit()

print "Server process pid=%i" % (os.getpid(),)
sockets = []
for i in range(10):
    (cd, address) = sd.accept()
    sockets.append(cd)
    cd.shutdown(socket.SHUT_WR)

os.system("/usr/sbin/lsof -p %i" % (os.getpid(),))
#os.system("netstat -nt|grep :%i" % (PORT,))
