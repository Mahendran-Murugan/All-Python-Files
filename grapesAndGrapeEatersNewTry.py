eatingCount = list(map(int, input().split()))
count = list(map(int, input().split()))
count[0] -= eatingCount[0]
if count[0] < 0:
    print('No')
else:
    count[0] -= eatingCount[1]
    if count[0] < 0:
        count[1] += count[0]
        count[0] = 0
        if count[1] < 0:
            print('No')
        else:
            count[0] -= eatingCount[2]
            if count[0] < 0:
                count[1] += count[0]
                count[0] = 0
                if count[1] < 0:
                    count[2] += count[1]
                    count[1] = 0
                    if count[2] < 0:
                        print('No')
                    else:
                        print('Yes')