#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(',')
    date_time = data[-1]
    date_time = date_time + data[0]
    print "%s\t%s\t%s" % (date_time, data[9],data[1])


