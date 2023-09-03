def replaceNoWithStar():
    N = input().lstrip('-')
    if int(N[0]) % 2 == 0:
        print("*" * len(N))
    else:
        print(N)


replaceNoWithStar()
replaceNoWithStar()

