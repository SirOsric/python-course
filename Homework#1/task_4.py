s = input()
def counter(s):
    d = {}
    lst = sorted(list(s))
    c = 0
    i = 0
    while i < len(s):
        if lst[c] not in d:
            d[lst[c]] = lst.count(lst[c])
        c += 1
        i += 1
    lst = list(d.keys())
    lst.sort()
    for letter in lst:
        print(letter, d[letter])

s = counter(s)
