__author__ = 'sir_osric'
import re
import sys

data = sys.stdin.read()
pattern = '([\W]+|_)'
result = re.sub(pattern, ' ', data)
print(result)
