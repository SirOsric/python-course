__author__ = 'sir_osric'
import re
import sys

data = sys.stdin.read()
data = data.split('\n')
line_num = 0
pattern = ' *([\w,. ]+) = '
for line in data:
    line_num += 1
    test = re.match(pattern, line)
    if test is not None:
        matching = list(test.groups())
        for var in matching:
            result = ' '.join(var.split(', '))
            print(line_num, result)
