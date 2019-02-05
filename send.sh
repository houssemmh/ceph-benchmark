#!/bin/bash

#this script sends the trace to the trace analysis machine
#this script has to be put in the home folder of each node.
#Before using it, we have to make sure that we have passwordless acess (ssh-keygen and ssh-copy-id)


folder=$1
sudo chown -R cephuser:cephuser lttng-traces
tracename=`ls -rt lttng-traces/ | tail -1`
echo $tracename

scp -r lttng-traces/$tracename houssemmh@192.168.122.1:ceph-traces/$folder/`hostname`.$tracename
rm -r lttng-traces/*
