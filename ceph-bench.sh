#!/bin/bash

sizes=(2 3 4 5)

for i in "${sizes[@]}"
do
	echo "Set size to $i"

#ceph osd pool set mypool size 2