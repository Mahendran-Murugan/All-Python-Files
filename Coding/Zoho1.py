n = int(input())
li = list(map(int, input().split()))

for i in range(n):
    small = -1
    for j in range(i+1, n):
        if li[i] > li[j]:
            small = li[j]
            break
    if i != n-1:
        print(small, end = " ")
    else:
        print(small)
