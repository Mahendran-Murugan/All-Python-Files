n = int(input("How many no do you want:"))
no_1 = 0
no_2 = 1
print(no_1, no_2, sep='\n')
for i in range(2, n):
    next_no = no_1+no_2
    print(next_no)
    no_1 = no_2
    no_2 = next_no
