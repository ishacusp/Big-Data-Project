#!/usr/bin/env python
import sys
(current_key, current_count) = (None, 0)
key = None

for line in sys.stdin:
    (key, count) = line.strip().split(",")
    if current_key == key:
        current_count += int(count)
    else:
        if current_key:
            print '%s\t%s' % (current_key, current_count)
        current_key = key
        current_count = int(count)
if current_key == key:
    print '%s\t%s' % (current_key, current_count)
