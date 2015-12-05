# Main whisperer

import re
import operator

f = open("C:/Users/Roma/PycharmProjects/python-course/exam2/hp5.txt", 'r')
data = f.read()
f.close()
data = data.split('\n')
pattern = '([A-Z][a-z]+ [A-Z][a-z])* whispered|whispered ([A-Z][a-z]* [A-Z][a-z]+)'
main_d = {}
line_d = {}
c = 0
i = 0
for line in data:
    test = re.findall(pattern, line)
    if test is not []:
        while i < len(test):
            if test[c] not in line_d:
                line_d[test[c]] = test.count(test[c])
            c += 1
            i += 1
        main_d = sum(main_d.items(), line_d.items())
print(max(main_d.items(), key=operator.itemgetter(1))[0], main_d[max(main_d.items(), key=operator.itemgetter(1))[0]])
print(test)
# print(data)