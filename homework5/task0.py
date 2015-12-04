__author__ = 'sir_osric'
import sys
import re

data = sys.stdin.read()
results = re.findall("you", data)
print(len(results))