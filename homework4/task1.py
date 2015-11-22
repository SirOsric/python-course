import re

__author__ = 'sir_osric'

f = open("/home/sir_osric/Python/yazkora.txt", 'r')
example = f.read()
example = example.replace('\n', ' ')
# print(example)
f.close()
res = re.findall('[^.]+\.', example)  # I tried to solve the whole task using re, but I screwed it up.

# \s*\w+yo[^.]+\.
# [^.]+\.
# print(res)

answerlist = []
f = open("/home/sir_osric/Python/res.txt", 'w')
f.write('\n'.join(res))
f.close()

f = open("/home/sir_osric/Python/res.txt", 'r')
for line in f:
    words = line.split(' ')
    for word in words:
        if word.endswith('yo'):
            answerlist.append(word + ' ')
    answerlist.append('\n')
f.close()
# print(answerlist)
with open('answer.txt', 'w') as answerfile:
            for word in answerlist:
                answerfile.write(word)
answerfile.close()

# ^– метасимвол начала строки
# $ – метасимвол конца строки
# ( ) – позволяют группировать группы символов
# * – несколько (или ноль) вхождений
# + – один или более вхождений
# | – (a|b) – a или b
# \d – метасимвол любой цифры
# \D – метасимвол любой НЕцифры
# \s – метасимвол любого пробельного символа (\t\n \r \f \v и пробел)
# \S – метасимвол любого НЕпробельного символа
# \w – метасимвол для букво-циферного символа
# \W – метасимвол для НЕ букво-циферного
