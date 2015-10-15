# Coprime test


def euclidus(n, m):
    if n % m == 0:
        return m
    else:
        return euclidus(m, n % m)


def rpfilter(a, *args):
    fltr = []
    for arg in args:
        if euclidus(a, arg) == 1:
            fltr.append(arg)
    return fltr

arg_list = (int(x) for x in input().split())
result = rpfilter(*arg_list)
if result == []:
    print('None')
else:
    for i in result:
        print(i, end=' ')
