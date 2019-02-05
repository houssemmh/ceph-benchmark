#!/usr/bin/python2


#this script starts tracing on all nodes and then collects the traces 


import logging
from remoto.process import run
from remoto import Connection
import uuid
import os



uuidstr=str(uuid.uuid4())
print(uuidstr)
os.mkdir("/home/houssemmh/ceph-traces/"+uuidstr)

logging.basicConfig(level=logging.DEBUG)
hosts = ['osd1','osd2','osd3','mon']
lttngcreate = ['sudo', 'lttng', 'create', 'ceph']
lttngenableevent = ['sudo', 'lttng', 'enable-event', '-u', '-a']
lttngstart = ['sudo', 'lttng', 'start']
lttngstop = ['sudo', 'lttng', 'stop']
lttngdestroy = ['sudo', 'lttng', 'destroy']
sendtrace = ['./send.sh', uuidstr]

for host in hosts:
        logger = logging.getLogger(host)
        conn = Connection(host, logger=logger)
        try:
                run(conn, lttngdestroy)
        except:
                pass


for host in hosts:
        logger = logging.getLogger(host)
        conn = Connection(host, logger=logger)
        #run(conn, ['sudo', 'lttng', '--version'])
        run(conn, lttngcreate)
        run(conn, lttngenableevent)
        run(conn, lttngstart)

raw_input("Press Enter to stop tracing...")
for host in hosts:
        logger = logging.getLogger(host)
        conn = Connection(host, logger=logger)
        run(conn, lttngstop)
        run(conn, lttngdestroy)
        run(conn, sendtrace)
