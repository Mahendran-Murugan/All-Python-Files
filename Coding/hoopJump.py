# Time complexity is High in hoopJump1
# hoopJump2 has less Time Complexity
def hoopJump1():
    for i in range(int(input())):
        num = int(input())
        li = []
        if num % 2 != 0:
            for i in range(1, num + 1):
                li.append(i)
            for j in range(int((len(li) - 1) / 2)):
                li.pop(0)
                li.pop(-1)
        print(li[0])


def hoopJump2():
    for i in range(int(input())):
        N = int(input())
        if N % 2 != 0:
            print((N//2)+1)


hoopJump1()
hoopJump2()

