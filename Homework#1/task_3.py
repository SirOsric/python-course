#List
string = input()
lst = string.split()
i = 0 # odd
odd = []
even = []
j = 1 # even
while i <= (len(lst) - 1):
    odd.append(lst[i])
    i += 2
odd_sorted = sorted(odd, key = int)
while j <= (len(lst)):
    even.append(lst[j])
    j += 2
even_sorted = sorted(even, key = int, reverse = True)
k = 0
m = 0
edited = list()
for n in range(len(lst)):
    if n % 2 != 0:
        edited.insert(n, even_sorted[k])
        k += 1
    else:
        edited.insert(n, odd_sorted[m]) 
        m += 1
result = ' '.join(edited)
#print(odd_sorted) - just checking both
#print(even_sorted)
print(result)
