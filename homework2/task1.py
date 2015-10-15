# The number of combinations

import math


def combinations_number(n, k):
    if k > n:
        return 0
    elif n == k or k == 0:
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    else:
        return combinations_number(n - 1, k - 1) + combinations_number(n - 1, k)

data = input().split(' ')
n = int(data[0])
k = int(data[1])

print(int(combinations_number(n, k)))
