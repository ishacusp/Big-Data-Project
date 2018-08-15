#!/usr/bin/env python
import re
import sys
for line in sys.stdin:
    lat, lon, datetime = line.strip().split(",")
    datetime=datetime.strip()
    date_list = datetime.split(' ')
    date = date_list[0]+date_list[1].split(':')[0]
    print "%s,%s" %(date, 1)
