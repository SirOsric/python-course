# Euclidean algorithm


def euclidus(n, m):
    if n % m == 0:
        return m
    else:
        return euclidus(m, n % m)

data = input().split(' ')
data = sorted(data)
n = int(data[0])
m = int(data[1])

if n > 0 and m > 0:
    print(euclidus(n, m))
