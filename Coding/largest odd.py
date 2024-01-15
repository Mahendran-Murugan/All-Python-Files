n = input().strip(" \" ")
flag = 0
li = []
if int(n) % 2 != 0:
    print(n)
else:
    for i in n:
        if int(i) % 2 == 0:
            continue
        else:
            flag = 1
            li.append(int(i))
    if flag == 1:
        print(max(li))
    else:
        print("")


