tool = input()
x = input()


def iron(x):
    if x == 0:
        print(x, 'утюгов')
    else:
        e = int((x[(len(x)-2):]))
        if 11 <= e <= 19:
            print(x, 'утюгов')
        else:
            end = int((x[(len(x)-1):]))
            if end == 1:
                print(x, 'утюг')
            elif 2 <= end <= 4:
                print(x, 'утюга')
            elif 5 <= end <= 9 or end == 0:
                print(x, 'утюгов')


def spoon(x):
    if x == 0:
        print(x, 'ложек')
    else:
        e = int((x[(len(x)-2):]))
        if 11 <= e <= 19:
            print(x, 'ложек')
        else:
            end = int((x[(len(x)-1):]))
            if end == 1:
                print(x, 'ложка')
            elif 2 <= end <= 4:
                print(x, 'ложки')
            elif 5 <= end <= 9 or end == 0:
                print(x, 'ложек')
if tool == 'утюг':
    iron(x)
elif tool == 'ложка':
    spoon(x)
