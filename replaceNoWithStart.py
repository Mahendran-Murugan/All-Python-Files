def replaceNoWithStar():
    N = abs(int(input()))
    startingDigit = N
    while startingDigit >= 10:
        startingDigit = startingDigit // 10
    if startingDigit % 2 == 0:
        print("*" * len(str(N)))
    else:
        print(N)


replaceNoWithStar()
replaceNoWithStar()
