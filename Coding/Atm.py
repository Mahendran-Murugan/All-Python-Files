for i in range(int(input())):
    amount_list=[]
    no_of_persons,total_amount=map(int,input().split())
    amount_list=list(map(int,input().split()))
    for k in amount_list:
        if k<=total_amount:
            total_amount-=k
            print("1",end="")
        else:
            print("0",end="")
    print()



