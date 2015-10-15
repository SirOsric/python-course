# Plural tools
def plural(n, words):
    n %= 100
    n1 = n % 10
    if 10 < n < 20:
        return words[2]
    elif 1 < n1 < 5:
        return words[1]
    elif n1 == 1:
        return words[0]
    else:
        return words[2]

words_iron = ['утюг', 'утюга', 'утюгов']
words_spoon = ['ложка', 'ложки', 'ложек']
words_harmonica = ['гармошка', 'гармошки', 'гармошек']
words_kettle = ['чайник', 'чайника', 'чайников']

word = input()
count = int(input())

if word == 'утюг':
    proper_word = plural(count, words_iron)
elif word == 'ложка':
    proper_word = plural(count, words_spoon)
elif word == 'гармошка':
    proper_word = plural(count, words_harmonica)
else:
    proper_word = plural(count, words_kettle)

print('%d %s' % (count, proper_word))
