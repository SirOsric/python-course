__author__ = 'sir_osric'
import sys
import re

data = sys.stdin.read()
data = data.split('\n')
line_num = 0
for line in data:
    line_num += 1
    results = re.findall('([\w]+) = ', line)
    if not results == []:
        print(line_num, results[0])
