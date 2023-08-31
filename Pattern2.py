def pattern():
    for i in range(0, 5):
        for j in range(i):
            if i % 2 == 0:
                if j % 2 == 0:
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            else:
                if j % 2 == 0:
                    print(0, end=' ')
                else:
                    print(1, end=' ')
        print()


def pattern1():
    for i in range(0, 5):
        if i % 2 == 0:
            in1 = 1
            in2 = 0
        else:
            in1 = 0
            in2 = 1
        for j in range(i):
            if j % 2 == 0:
                print(in1, end=' ')
            else:
                print(in2, end=' ')
        print()


pattern1()
pattern()
