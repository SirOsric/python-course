__author__ = 'sir_osric'
import sys
import re

data = sys.stdin.read()
results = re.findall("(\d*(111|222|333|444|555|666|777|888|999|000)\d*)", data)
for phone in results:
    print(phone[0])
