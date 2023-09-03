def modifyMatrix():
    R = int(input())
    arr1 = []
    arr2 = []
    for i in range(2 * R):
        li = list(map(int, input().split()))
        if i < R:
            arr1.append(li)
        else:
            arr2.append(li)

    def showMatrix(matrix):
        for j in matrix:
            for k in j:
                print(k, end=" ")
            print()


modifyMatrix()
