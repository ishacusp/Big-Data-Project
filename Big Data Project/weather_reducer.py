 #!/usr/bin/env python
import sys
(current_key, current_temp, cond) = (None, 0, None)
key = None

for line in sys.stdin:
    (key,  temp, conditons) = line.strip().split("\t")
    if current_key == key:
        current_temp = temp
        cond = conditions
    else:
        if current_key:
            print '%s\t%s\t%s' % (current_key, current_temp, cond)
        current_key = key
        current_temp = temp
        cond = conditions

# if current_key == key:
#     print('%s\t%s' % (current_key, current_temp))
