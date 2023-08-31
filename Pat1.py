def normalway():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
    print('------------')

def anotherway():
    li = []
    for i in range(1, 6):
        li.append(str(i))
        print(' '.join(li))
    print('------------')


def Mostsimple_for_difficult_pat():
    s = "Mahendran"
    for i in range(len(s) + 1):
        print(s[0:i])
        i += 1
    for j in range(10):
        print(s[0:i])
        i -= 1
    print('------------')


normalway()
anotherway()
Mostsimple_for_difficult_pat()
