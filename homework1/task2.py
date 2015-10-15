string = input()
lst = string.split()
lst_sum = 0
for i in range(len(lst)):
    lst_sum += int(lst[i])
print(lst_sum / len(lst))
