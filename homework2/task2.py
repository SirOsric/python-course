# Trial division


def prime(n):
    j = True
    i = 2
    while i <= n ** 0.5:
        if i * i <= n and j is True:
            if n % i != 0:
                i += 1
            else:
                j = False
                break
    return j

lines = int(input())
for line in range(lines):
    print(prime(int(input())))
